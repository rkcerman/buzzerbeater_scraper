import logging
import re

from bbstats.models import BoxscoreStats, Boxscores, PlayerSkills, \
    PlayByPlays
from django.db.models import Sum
from collections import Counter

from .query import get_player_skills

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


# Calculates GSP, FSP and TSP from the skills model
def calculate_skill_points(skills):
    try:
        gsp = skills['jump_shot'][0] + skills['jump_range'][0] + skills['outside_def'][0] \
              + skills['handling'][0] + skills['driving'][0] + skills['passing'][0]
        fsp = skills['inside_shot'][0] + skills['inside_def'][0] \
              + skills['rebounding'][0] + skills['shot_blocking'][0]
    except KeyError as e:
        raise ValueError('Not enough skills') from e
    else:
        tsp = gsp + fsp
        skill_points = {
            'gsp': gsp,
            'fsp': fsp,
            'tsp': tsp,
        }
        return skill_points


# Creating a map of skills nomenclature with their respective values
def get_skills_nomenclature(skills):
    player_skills = {}
    for skill in skills:
        skill_name = skill.skill.replace(' ', '_').replace('.', '').lower()
        player_skills[skill_name] = [skill.value, skills_mapping[skill.value]]
    return player_skills


# Gets strategies and preps matches used by the player's team in that particular match
def get_strategies_context(player_stats, boxscore):
    if isinstance(player_stats, BoxscoreStats) and isinstance(boxscore, Boxscores):
        player_team = player_stats.team

        if player_stats.boxscore.match.home_team_id == player_team.id:
            away_or_home_str = 'home'
            player_team_off = boxscore.home_off_strategy
            player_team_def = boxscore.home_def_strategy
            player_team_prep_f = boxscore.home_prep_focus_matched
            player_team_prep_p = boxscore.home_prep_pace_matched
            opp_team_off = boxscore.away_off_strategy
            opp_team_def = boxscore.away_def_strategy
            opp_team_prep_f = boxscore.away_prep_focus_matched
            opp_team_prep_p = boxscore.away_prep_pace_matched
        else:
            away_or_home_str = 'away'
            player_team_off = boxscore.away_off_strategy
            player_team_def = boxscore.away_def_strategy
            player_team_prep_f = boxscore.away_prep_focus_matched
            player_team_prep_p = boxscore.away_prep_pace_matched
            opp_team_off = boxscore.home_off_strategy
            opp_team_def = boxscore.home_def_strategy
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


# Creates a list of dicts per player ID, containing the player object and skills
def get_players_skills_info(players):
    team_players_skills = []
    for player in players:
        try:
            player_skills = get_player_skills(player_id=player.id)
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


# Gets performances for each shot type for a player
def get_player_shot_types(shots, agg_type):
    if agg_type in ['pass', 'shoot', 'guard']:
        distinct_shot_types = shots \
            .values_list('pbp__event_type') \
            .distinct() \
            .order_by('pbp__event_type')
        shot_performances = []

        # Performing the actual aggregates
        for shot_type in distinct_shot_types:
            shot_type = shot_type[0]
            shot_type_query = shots.filter(pbp__event_type=shot_type)

            shot_performances.append(
                aggregate_shot_type(shot_type, shot_type_query, agg_type)
            )

        return shot_performances
    else:
        raise ValueError('type needs to be one of pass, shoot or guard.')


# Performs aggregates for each shot type for a player
def aggregate_shot_type(shot_type, shot_type_query, agg_type):
    made_fg = shot_type_query.filter(
        outcome__in=['scored', 'fouled']
    ).count()
    attempted_fg = shot_type_query.count()
    fg_per = round(safe_div(made_fg, attempted_fg), 2)

    agg_shot_type = {
        # TODO remove after creating a mapping table
        'play_tags': PlayByPlays.objects.filter(
            event_type=shot_type
        )[0].play_tags,
        'shot_type': shot_type,
        'made_fg': made_fg,
        'attempted_fg': attempted_fg,
        'fg_per': fg_per,
    }

    if agg_type == 'shoot':
        # Guarded
        made_guarded = shot_type_query.filter(defender__isnull=False, outcome='scored').count()
        attempted_guarded = shot_type_query.filter(defender__isnull=False).count()
        guarded_per = round(safe_div(made_guarded, attempted_guarded), 2)

        # Passed
        made_passed = shot_type_query.filter(passer__isnull=False, outcome='scored').count()
        attempted_passed = shot_type_query.filter(passer__isnull=False).count()
        passed_per = round(safe_div(made_passed, attempted_passed), 2)

        agg_shot_type['made_guarded'] = made_guarded
        agg_shot_type['attempted_guarded'] = attempted_guarded
        agg_shot_type['guarded_per'] = guarded_per
        agg_shot_type['made_passed'] = made_passed
        agg_shot_type['attempted_passed'] = attempted_passed
        agg_shot_type['passed_per'] = passed_per

    return agg_shot_type


# Creates dict with quick overview stats for a player
def get_player_quick_stats_context(boxscore_stats, sdp_stats):
    fg_per = calc_player_fg_per(boxscore_stats)

    return {
        'fg_per': fg_per,
    }


# Calculates player's FG% out of supplied boxscore stats
def calc_player_fg_per(player_boxscore_stats):
    try:
        fgm_sum = player_boxscore_stats.aggregate(Sum('fgm'))
        fga_sum = player_boxscore_stats.aggregate(Sum('fga'))
    except AttributeError:
        raise TypeError('Expecting type BoxscoreStats.')
    else:
        return safe_div(fgm_sum['fgm_sum'], fga_sum['fga_sum'])


# Calculates player's defensive FG% out of supplied def. performances
def calc_player_defense_per(def_stats):
    result = Counter()
    try:
        for shot_type in def_stats:
            result['made_fg'] += shot_type['made_fg']
            result['attempted_fg'] += shot_type['attempted_fg']
    except TypeError:
        raise TypeError('Expecting a shot_types dict')
    else:
        return round(safe_div(
            result['made_fg'],
            result['attempted_fg']
        ), 2)


def safe_div(x, y):
    if y == 0:
        return 0
    return x / y
