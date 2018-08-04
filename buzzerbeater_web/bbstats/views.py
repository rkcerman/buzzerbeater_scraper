import logging
import re

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from .models import Players, PlayerSkills, BoxscoreStats, Boxscores, Shots, Teams, GameShapes

default_season = 43

skills_mapping = {
    1: 'atrocious',
    2: 'pitiful',
    3: 'awful',
    4: 'inept',
    5: 'mediocre',
    6: 'average',
    7: 'respectable',
    8: 'strong',
    9: 'proficient',
    10: 'prominent',
    11: 'prolific',
    12: 'sensational',
    13: 'tremendous',
    14: 'wondrous',
    15: 'marvelous',
    16: 'prodigious',
    17: 'stupendous',
    18: 'phenomenal',
    19: 'colossal',
    20: 'legendary',
}

potentials_mapping = {
    0: {'announcer': 'lev5'},
    1: {'bench warmer': 'lev6'},
    2: {'role player': 'lev7'},
    3: {'6th man': 'lev8'},
    4: {'starter': 'lev9'},
    5: {'star': 'lev10'},
    6: {'allstar': 'lev11'},
    7: {'perennial allstar': 'lev12'},
    8: {'superstar': 'lev13'},
    9: {'MVP': 'lev15'},
    10: {'hall of famer': 'lev16'},
    11: {'all-time great': 'lev17'},
}


def index(request):
    all_teams = Teams.objects.order_by('name')
    context = {
        'all_teams': all_teams,
    }
    return render(request, 'bbstats/index.html', context)


# Returns team overview with the list of players and their skills
def team_overview(request, team_id):
    team = Teams.objects.get(id=team_id)
    team_players = Players.objects.filter(team_id=team_id)
    team_players_skills = get_team_players_skills(team_players)

    context = {
        'team': team,
        'players_skills': team_players_skills,
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
    try:
        # Defining and looking up key objects from the DB
        player = Players.objects.get(
            id=player_id
        )
        skills = PlayerSkills.objects.filter(
            player=player_id
        ).distinct('skill').order_by('-skill')
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

        player_skills = get_skills_nomenclature(skills)

        # Returns styling class and nomeclature for potential
        try:
            potential_nomenc = potentials_mapping[player.potential]
            potenial_name = list(potential_nomenc)[0]
            potential = {
                'value': player.potential,
                'name': potenial_name,
                'lev': potential_nomenc[potenial_name],
            }
        except KeyError:
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
        }

        # Calculating value of TSP
        try:
            gsp = player_skills['jump_shot'][0] + player_skills['jump_range'][0] + player_skills['outside_def'][0] \
                  + player_skills['handling'][0] + player_skills['driving'][0] + player_skills['passing'][0]
            fsp = player_skills['inside_shot'][0] + player_skills['inside_def'][0] \
                  + player_skills['rebounding'][0] + player_skills['shot_blocking'][0]
            tsp = gsp + fsp

            context['gsp'] = gsp
            context['fsp'] = fsp
            context['tsp'] = tsp
        except KeyError as e:
            logging.info('Not enough skills available')
            print(e)

        return render(request, 'bbstats/player_overview.html', context)
    except ObjectDoesNotExist as e:
        return HttpResponse('Player ID ', player_id, ' does not exist.')


# Get aggregates for each unique shot type
def get_shot_performances(shots):
    distinct_shot_types = shots\
        .values_list('pbp__event_type')\
        .distinct()\
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


# Creating a map of skills nomenclature with their respective values
def get_skills_nomenclature(skills):
    player_skills = {}
    for skill in skills:
        skill_name = skill.skill.replace(' ', '_').replace('.', '').lower()
        player_skills[skill_name] = [skill.value, skills_mapping[skill.value]]
    return player_skills


def safe_div(x,y):
    if y == 0:
        return 0
    return x / y


# Get initials of each strategy name for display a shorter version in the table
def get_initials(string):
    initials = ''.join(re.findall('(\d?\d?\d?[A-Z])', string))

    if len(initials) == 1:
        return string
    else:
        return initials


# Creates a list of dicts per player ID, containing the player object and skills
def get_team_players_skills(players):
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
            player_dict = {
                    'info': player,
                    'skills': player_skills,
            }
            team_players_skills.append(player_dict)
    return team_players_skills


# Gets strategies and preps matches used by the player's team in that particular match
def get_strategies_preps(player_stats, boxscore):
    if isinstance(player_stats, BoxscoreStats) and isinstance(boxscore, Boxscores):
        player_team = player_stats.team

        if player_stats.boxscore.match.home_team_id == player_team.id:
            away_or_home_str = 'home'
            player_team_off = get_initials(boxscore.home_off_strategy)
            player_team_def = get_initials(boxscore.home_def_strategy)
            player_team_prep_f = boxscore.home_prep_focus_matched
            player_team_prep_p = boxscore.home_prep_pace_matched
            opp_team_off = get_initials(boxscore.away_off_strategy)
            opp_team_def = get_initials(boxscore.away_def_strategy)
            opp_team_prep_f = boxscore.away_prep_focus_matched
            opp_team_prep_p = boxscore.away_prep_pace_matched
        else:
            away_or_home_str = 'away'
            player_team_off = get_initials(boxscore.away_off_strategy)
            player_team_def = get_initials(boxscore.away_def_strategy)
            player_team_prep_f = boxscore.away_prep_focus_matched
            player_team_prep_p = boxscore.away_prep_pace_matched
            opp_team_off = get_initials(boxscore.home_off_strategy)
            opp_team_def = get_initials(boxscore.home_def_strategy)
            opp_team_prep_f = boxscore.home_prep_focus_matched
            opp_team_prep_p = boxscore.home_prep_pace_matched

        strategies_preps = {
            'away_or_home': away_or_home_str,
            'player_team_off': player_team_off,
            'player_team_def': player_team_def,
            'player_team_prep_f': player_team_prep_f,
            'player_team_prep_p': player_team_prep_p,
            'opp_team_off': opp_team_off,
            'opp_team_def': opp_team_def,
            'opp_team_prep_f': opp_team_prep_f,
            'opp_team_prep_p': opp_team_prep_p
        }
        return strategies_preps