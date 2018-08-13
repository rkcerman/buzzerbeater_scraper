import redis
from django.db.models import Q

from bbstats.models import Matches, Boxscores, Teams, PlayerSkills

r = redis.StrictRedis(host='localhost', port=6379, db=0)


# Fetches the schedule from the DB, or if available from redis
def get_schedule(team, season):
    redis_schedule_key = 'team:{}:season:{}:schedule'.format(team.id, season)
    team_id = team.id
    schedule_with_bs = []

    # Let's check if there is an existing schedule in redis
    # If not, it fetches the matches from the DB and creates redis list
    redis_schedule = r.lrange(redis_schedule_key, 0, -1)
    if not redis_schedule:
        print('Getting matches from psql')
        schedule = Matches.objects.filter(season=season)\
            .filter(Q(away_team_id=team_id) | Q(home_team_id=team_id))\
            .order_by('match_date')
        matches_ids = [match['id'] for match in schedule.values('id')]

        r.rpush(redis_schedule_key, *matches_ids)
        set_redis_matches(schedule)
    else:
        print('Getting matches from redis')
        schedule = []
        for match_id in redis_schedule:
            schedule.append(get_match(match_id))

    # Append boxscore to each match and tuple them together
    for match in schedule:
        try:
            boxscore = get_boxscore(match.id)
        except Boxscores.DoesNotExist:
            boxscore = None
        match_bs = (match, boxscore)
        schedule_with_bs.append(match_bs)

    return schedule_with_bs


def get_all_teams():
    return Teams.objects.order_by('name')


# Redis HMSET for each match, using values() function to get mapping
def set_redis_matches(matches):
    for match in matches:
        redis_match_key = 'match:{}'.format(match.id)
        r.set(redis_match_key, match)


# Get all the fields associated with a particular match_id
def get_match(match_id):
    return redis_get_all_fields(
        key='match',
        model=Matches(),
        model_id=match_id
    )


# Redis HMSET for each boxscore, using values() function to get mapping
def set_redis_boxscores(boxscores):
    for boxscore in boxscores:
        redis_boxscore_key = 'boxscore:{}'.format(boxscore.match_id)
        r.set(redis_boxscore_key, boxscore)


def get_boxscore(boxscore_id):
    return redis_get_all_fields(
        key='boxscore',
        model=Boxscores(),
        model_id=boxscore_id
    )


def get_player_skills(player_id):
    return PlayerSkills.objects.filter(
        player=player_id
    ).distinct('skill').order_by('-skill', '-date')


def redis_get_all_fields(key, model, model_id):
    redis_item = r.get('{}:{}'.format(key, model_id))
    if not redis_item:
        if isinstance(model, Matches):
            return Matches.objects.get(id=model_id)
        if isinstance(model, Boxscores):
            return Boxscores.objects.get(match_id=model_id)
    else:
        return redis_item


