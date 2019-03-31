from abc import ABC
from django.db.models import Q, Avg, Func, Count

from bbstats.models import Matches, Boxscores, Teams, PlayerSkills, \
    ScoreTables, BoxscoreStats, Players
from collections import Counter


# TODO get this to process.py
# Fetches the schedule from the DB
def get_schedule(team, season):
    team_id = team.id
    schedule_with_bs = []

    schedule = Matches.objects.filter(season=season) \
        .filter(Q(away_team_id=team_id) | Q(home_team_id=team_id)) \
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


def adjusted_stat_per_36m(avg_field, total_avg_min):
    return Round((Avg(avg_field) / total_avg_min) * 36)


class Round(Func, ABC):
    function = 'ROUND'
    template = '%(function)s(%(expressions)s, 2)'


class PlayerStats:

    def __init__(self, player_id):
        self.player = Players.objects.get(pk=player_id)
        self.player_stats = BoxscoreStats.objects.filter(
            player_id=player_id)

    def get_player_36m_stats(self, match_type='league'):
        """
        Aggregates player's stats per 36m, grouped by season

        :param player_id:
        :param match_type:
        :return:
        """

        # Let's combine the player's minutes on all positions
        total_avg_min = (
                Avg('pg_min') +
                Avg('sg_min') +
                Avg('sf_min') +
                Avg('pf_min') +
                Avg('c_min')
        )
        player_stats = self.player_stats.filter(
            boxscore__match_type__contains=match_type
        ).order_by('-boxscore__match__season')

        agg_stats = player_stats.values('boxscore__match__season') \
            .annotate(
            games=Count('boxscore'),
            pts=adjusted_stat_per_36m('pts', total_avg_min),
            ast=adjusted_stat_per_36m('ast', total_avg_min),
            oreb=adjusted_stat_per_36m('oreb', total_avg_min),
            reb=adjusted_stat_per_36m('reb', total_avg_min),
            stl=adjusted_stat_per_36m('stl', total_avg_min),
            blk=adjusted_stat_per_36m('blk', total_avg_min),
            t_o=adjusted_stat_per_36m('t_o', total_avg_min),
            pf=adjusted_stat_per_36m('pf', total_avg_min),
            fgm=adjusted_stat_per_36m('fgm', total_avg_min),
            fga=adjusted_stat_per_36m('fga', total_avg_min),
            tpm=adjusted_stat_per_36m('tpm', total_avg_min),
            tpa=adjusted_stat_per_36m('tpa', total_avg_min),
            ftm=adjusted_stat_per_36m('ftm', total_avg_min),
            fta=adjusted_stat_per_36m('fta', total_avg_min),
            # min=Round(total_avg_min)
        )

        return agg_stats
