import logging

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render

from .models import Players, PlayerSkills, BoxscoreStats

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


# Returns player overview
def overview(request, player_id):
    try:
        player = Players.objects.get(id=player_id)
        team = player.team
        skills = PlayerSkills.objects.filter(player=player_id)
        matches = BoxscoreStats.objects.filter(player_id=player_id).order_by('-match_id')

        player_skills = {}
        for skill in skills:
            skill_name = skill.skill.replace(' ', '_').replace('.', '').lower()
            player_skills[skill_name] = [skill.value, skills_mapping[skill.value]]

        for match in matches:
            max_minutes = [match.pg_min, match.sg_min, match.sf_min, match.pf_min, match.c_min]

        context = {
            'player': player,
            'team': team,
            'skills': player_skills,
            'matches': matches,
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
