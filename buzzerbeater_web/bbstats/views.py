import logging

from django.shortcuts import render
from django.db.models import Q
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page

from .processors.process import calculate_skill_points, get_skills_nomenclature, \
    get_potential_nomenclature, get_strategies_preps

from .processors.query import get_schedule, get_all_teams
from .models import Players, PlayerSkills, BoxscoreStats, Shots, Teams

default_season = 43
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def index(request):
    context = {
        'all_teams': get_all_teams(),
    }
    return render(request, 'bbstats/index.html', context)


# Returns team overview with the list of players and their skills
def team_overview(request, team_id):
    team = Teams.objects.get(id=team_id)
    team_players = Players.objects.filter(team_id=team_id)
    team_players_skills = get_players_skills_potential(team_players)

    # TODO change season
    schedule = get_schedule(team, 43)

    context = {
        'team': team,
        'players_skills': team_players_skills,
        'schedule': schedule,
    }
    return render(request, 'bbstats/team_overview.html', context)


# Returns player overview with the default season and all league and cup matches
def player_default_overview(request, player_id):
    return player_overview(
        request=request,
        player_id=player_id,
        season=default_season,
        match_type='standard',
    )


# Returns player overview with the specified season and all league and cup matches
def player_season_overview(request, player_id, season):
    return player_overview(
        request=request,
        player_id=player_id,
        season=season,
        match_type='standard',
    )


# Returns player overview
def player_overview(request, player_id, season, match_type):
    # Defining and looking up key objects from the DB
    player = Players.objects.get(
        id=player_id
    )
    skills = PlayerSkills.objects.filter(
        player=player_id
    ).distinct('skill').order_by('-skill', '-date')
    boxscore_stats = BoxscoreStats.objects.filter(
        player_id=player_id,
        boxscore__match__season=season
    ).order_by('-boxscore_id')
    player_shots = Shots.objects.filter(
        shooter=player_id,
        pbp__boxscore__match__season=season
    )
    player_defended_shots = Shots.objects.filter(
        defender=player_id,
        pbp__boxscore__match__season=season
    )
    player_passed_shots = Shots.objects.filter(
        passer=player_id,
        pbp__boxscore__match__season=season
    )

    # Further filtering based on match_types if they are defined
    if match_type == 'standard':
        boxscore_stats = boxscore_stats.filter(
            Q(boxscore__match_type__contains='league') | Q(boxscore__match_type__contains='cup')
        )
        player_shots = player_shots.filter(
            Q(pbp__boxscore__match_type__contains='league') | Q(pbp__boxscore__match_type__contains='cup')
        )

    # Returns styling class and nomenclature for skills
    player_skills = get_skills_nomenclature(skills)

    try:
        skill_points = calculate_skill_points(player_skills)
    except ValueError:
        skill_points = {}

    # Returns styling class and nomenclature for potential
    try:
        potential = get_potential_nomenclature(player)
    except ValueError:
        potential = {}

    # Creating a list of all matches with their types, stats and minutes
    stats = []
    for stat in boxscore_stats:
        max_minutes = {
            'PG': stat.pg_min,
            'SG': stat.sg_min,
            'SF': stat.sf_min,
            'PF': stat.pf_min,
            'C': stat.c_min
        }

        max_minute_key = max(max_minutes, key=max_minutes.get)
        max_minute_value = max(max_minutes.values())

        boxscore = stat.boxscore
        match_type = boxscore.match_type

        stats.append({
            'match': stat,
            'max_minute_key': max_minute_key,
            'max_minute_value': max_minute_value,
            'match_type': match_type,
            'strategies_preps': get_strategies_preps(stat, stat.boxscore),
            'shots': player_shots
        }
        )

    shot_performances = get_shot_performances(player_shots)
    defense_performances = get_defense_performances(player_defended_shots)
    passing_performances = get_passing_performances(player_passed_shots)

    # Setting up the final context
    context = {
        'player': player,
        'potential': potential,
        'skills': player_skills,
        'stats': stats,
        'shot_performances': shot_performances,
        'defense_performances': defense_performances,
        'passing_performances': passing_performances,
        **skill_points
    }

    return render(request, 'bbstats/player_overview.html', context)


# Get aggregates for each unique shot type
def get_shot_performances(shots):
    distinct_shot_types = shots \
        .values_list('pbp__event_type') \
        .distinct() \
        .order_by('pbp__event_type')
    shot_performances = []

    # Performing the actual aggregates, with the exclusion of fouled shots
    for shot_type in distinct_shot_types:
        shot_type = shot_type[0]
        shot_type_query = shots.filter(pbp__event_type=shot_type).exclude(outcome='fouled')

        attempted_fg = shot_type_query.count()
        made_fg = shot_type_query.filter(outcome='scored').count()
        fg_per = round(safe_div(made_fg, attempted_fg), 2)

        # Guarded
        attempted_guarded = shot_type_query.filter(defender__isnull=False).count()
        made_guarded = shot_type_query.filter(defender__isnull=False, outcome='scored').count()
        guarded_per = round(safe_div(made_guarded, attempted_guarded), 2)

        # Passed
        attempted_passed = shot_type_query.filter(passer__isnull=False).count()
        made_passed = shot_type_query.filter(passer__isnull=False, outcome='scored').count()
        passed_per = round(safe_div(made_passed, attempted_passed), 2)

        shot_performances.append(
            {
                'shot_type': shot_type,
                'attempted_fg': attempted_fg,
                'made_fg': made_fg,
                'fg_per': fg_per,
                'attempted_guarded': attempted_guarded,
                'made_guarded': made_guarded,
                'guarded_per': guarded_per,
                'attempted_passed': attempted_passed,
                'made_passed': made_passed,
                'passed_per': passed_per,
            }
        )

    return shot_performances


# TODO look into combining these aggregate functions into one
# Get aggregates for each shot types and player's ability to defend them
def get_defense_performances(defended_shots):
    distinct_shot_types = defended_shots \
        .values_list('pbp__event_type') \
        .distinct() \
        .order_by('pbp__event_type')
    defense_performances = []

    # Performing the actual aggregates, with the exclusion of fouled shots
    for shot_type in distinct_shot_types:
        shot_type = shot_type[0]
        shot_type_query = defended_shots.filter(pbp__event_type=shot_type).exclude(outcome='fouled')

        opp_attempted_fg = shot_type_query.count()
        opp_made_fg = shot_type_query.filter(outcome='scored').count()
        opp_fg_per = round(safe_div(opp_made_fg, opp_attempted_fg), 2)

        # Passed
        opp_attempted_passed = shot_type_query.filter(passer__isnull=False).count()
        opp_made_passed = shot_type_query.filter(passer__isnull=False, outcome='scored').count()
        opp_passed_per = round(safe_div(opp_made_passed, opp_attempted_passed), 2)

        defense_performances.append(
            {
                'shot_type': shot_type,
                'opp_attempted_fg': opp_attempted_fg,
                'opp_made_fg': opp_made_fg,
                'opp_fg_per': opp_fg_per,
                'opp_attempted_passed': opp_attempted_passed,
                'opp_made_passed': opp_made_passed,
                'opp_passed_per': opp_passed_per,
            }
        )

    return defense_performances


# TODO look into combining these aggregate functions into one
# Get aggregates for each shot types the player passed to
def get_passing_performances(passed_shots):
    distinct_shot_types = passed_shots \
        .values_list('pbp__event_type') \
        .distinct() \
        .order_by('pbp__event_type')
    passing_performances = []

    # Performing the actual aggregates, with the exclusion of fouled shots
    for shot_type in distinct_shot_types:
        shot_type = shot_type[0]
        shot_type_query = passed_shots.filter(pbp__event_type=shot_type).exclude(outcome='fouled')

        # All
        mate_attempted_fg = shot_type_query.count()
        mate_made_fg = shot_type_query.filter(outcome='scored').count()
        mate_fg_per = round(safe_div(mate_made_fg, mate_attempted_fg), 2)

        # Guarded
        mate_attempted_guarded = shot_type_query.filter(defender__isnull=False).count()
        mate_made_guarded = shot_type_query.filter(defender__isnull=False, outcome='scored').count()
        mate_guarded_per = round(safe_div(mate_made_guarded, mate_attempted_guarded), 2)

        passing_performances.append(
            {
                'shot_type': shot_type,
                'mate_attempted_fg': mate_attempted_fg,
                'mate_made_fg': mate_made_fg,
                'mate_fg_per': mate_fg_per,
                'mate_attempted_guarded': mate_attempted_guarded,
                'mate_made_guarded': mate_made_guarded,
                'mate_guarded_per': mate_guarded_per,
            }
        )

    return passing_performances


# Creates a list of dicts per player ID, containing the player object and skills
def get_players_skills_potential(players):
    team_players_skills = []
    for player in players:
        try:
            player_skills = PlayerSkills.objects.filter(player_id=player.id)
        except AttributeError as e:
            logging.error(e)
            logging.error('Only accepting Players as a model')
        else:
            player_skills = player_skills.distinct('skill').order_by('-skill')
            player_skills = get_skills_nomenclature(player_skills)
            try:
                player_potential = get_potential_nomenclature(player)
            except ValueError:
                player_potential = {}
            player_dict = {
                'info': player,
                'skills': player_skills,
                'potential': player_potential,
            }
            team_players_skills.append(player_dict)
    return team_players_skills


def safe_div(x, y):
    if y == 0:
        return 0
    return x / y
