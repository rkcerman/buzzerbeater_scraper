import redis
from django.db.models import Q

from bbstats.models import Matches

r = redis.StrictRedis(host='localhost', port=6379, db=0, charset="utf-8", decode_responses=True)


# Fetches the schedule from the DB, or if available from redis
# TODO might turn this into redis sorted set
def get_schedule(team, season):
    redis_schedule_key = 'team:{}:schedule'.format(team.id)
    team_id = team.id

    # Let's check if there is an existing schedule in redis
    # If not, it fetches the matches from the DB and creates redis list
    # TODO not robust - passes even if only one match fetched
    redis_schedule = r.lrange(redis_schedule_key, 0, -1)
    if not redis_schedule:
        print('Getting matches from psql')
        matches = Matches.objects.filter(season=season)\
            .filter(Q(away_team_id=team_id) | Q(home_team_id=team_id))\
            .order_by('match_date')
        matches_ids = [match['id'] for match in matches.values('id')]

        r.rpush(redis_schedule_key, *matches_ids)
        set_redis_matches(matches)
        return matches
    else:
        print('Getting matches from redis')
        matches = []
        for match_id in redis_schedule:
            match_id = match_id
            match = get_match(match_id)
            matches.append(match)
        return matches


# Redis HMSET for each match, using values() function to get mapping
def set_redis_matches(matches):
    list_matches = list(matches.values())
    for match in list_matches:
        redis_match_key = 'match:{}'.format(match.pop('id'))
        r.hmset(redis_match_key, match)


# Get all the fields associated with a particular match_id
def get_match(match_id):
    redis_match = r.hgetall('match:{}'.format(match_id))
    if not redis_match:
        return Matches.objects.get(id=match_id)
    else:
        return redis_match
