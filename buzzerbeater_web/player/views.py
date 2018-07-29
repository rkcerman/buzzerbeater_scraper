import logging
import re

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

from .models import Players, PlayerSkills, BoxscoreStats, Boxscores, Shots

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


def index(request):
    latest_players_list = Players.objects.order_by('-last_update_at')[:10]
    context = {
        'latest_players_list': latest_players_list,
    }
    return render(request, 'player/index.html', context)


# Returns player overview with the default season
def default_overview(request, player_id):
    return overview(
        request=request,
        player_id=player_id,
        season=default_season
    )


# Returns player overview
def overview(request, player_id, season):
    try:
        print('season: ', season)
        player = Players.objects.get(id=player_id)
        team = player.team
        skills = PlayerSkills.objects.filter(player=player_id)
        boxscore_stats = BoxscoreStats.objects.filter(player_id=player_id).order_by('-match_id')
        shots = Shots.objects.filter(shooter=player_id)

        # Creating a map of skills nomenclature with their respective values
        player_skills = {}
        for skill in skills:
            skill_name = skill.skill.replace(' ', '_').replace('.', '').lower()
            player_skills[skill_name] = [skill.value, skills_mapping[skill.value]]

        # Creating a list of all matches with their types, stats and minutes
        stats = []
        for match in boxscore_stats:
            max_minutes = {
                'PG': match.pg_min,
                'SG': match.sg_min,
                'SF': match.sf_min,
                'PF': match.pf_min,
                'C': match.c_min
            }

            max_minute_key = max(max_minutes, key=max_minutes.get)
            max_minute_value = max(max_minutes.values())

            boxscore = Boxscores.objects.get(match_id=match.match_id)
            match_type = boxscore.match_type

            stats.append({
                'match': match,
                'max_minute_key': max_minute_key,
                'max_minute_value': max_minute_value,
                'match_type': match_type,
                'strategies_preps': get_strategies_preps(match, boxscore),
                'shots': shots
            }
            )

        # Setting up the final context
        context = {
            'player': player,
            'team': team,
            'skills': player_skills,
            'stats': stats,
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

        return render(request, 'player/player_overview.html', context)
    except ObjectDoesNotExist as e:
        return HttpResponse('Player ID ', player_id, ' does not exist.')

# Get initials of each strategy name for display a shorter version in the table
def get_initials(string):
    initials = ''.join(re.findall('(\d?\d?\d?[A-Z])', string))

    if len(initials) == 1:
        return string
    else:
        return initials

# Gets strategies and preps matches used by the player's team in that particular match
def get_strategies_preps(player_stats, boxscore):
    if isinstance(player_stats, BoxscoreStats) and isinstance(boxscore, Boxscores):
        player_team = player_stats.team

        if player_stats.match.home_team_id == player_team.id:
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