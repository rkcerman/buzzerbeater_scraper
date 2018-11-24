from django.db.models import Q

from bbstats.models import Matches, Boxscores, Teams, PlayerSkills, ScoreTables
from collections import Counter


# TODO get this to process.py
# Fetches the schedule from the DB
def get_schedule(team, season):
    team_id = team.id
    schedule_with_bs = []

    schedule = Matches.objects.filter(season=season)\
        .filter(Q(away_team_id=team_id) | Q(home_team_id=team_id))\
        .order_by('match_date')

    # Append boxscore to each match and tuple them together
    for match in schedule:
        try:
            boxscore = get_boxscore(match.id)
            end_score = match_end_score(match.id)
        except Boxscores.DoesNotExist:
            boxscore = None
            end_score = ''
        finally:
            match_bs = (match, boxscore, end_score)
            schedule_with_bs.append(match_bs)

    return schedule_with_bs


# Sums score by each team from all quarters in a match
def match_end_score(match_id):
    print(match_id)
    match_scores = get_match_scores(match_id)
    end_score = Counter()
    for qtr in match_scores:
        end_score['away_score'] += qtr.away_team_score
        end_score['home_score'] += qtr.home_team_score

    return '{} - {}'.format(
        end_score['away_score'],
        end_score['home_score']
    )


def get_all_teams():
    return Teams.objects.order_by('name')


# Get all the fields associated with a particular match_id
def get_match(id):
    return Matches.objects.get(id=id)


def get_boxscore(match_id):
    return Boxscores.objects.get(match_id=match_id)


def get_match_scores(match_id):
    return ScoreTables.objects.filter(match_id=match_id)


def get_player_skills(player_id):
    return PlayerSkills.objects.filter(
        pk=player_id
    )


def get_latest_player_skills(player_id):
    return PlayerSkills.objects.latest_skills(
        pk=player_id
    )

