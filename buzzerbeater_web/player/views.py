from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Players, PlayerSkills


def index(request):
    latest_players_list = Players.objects.order_by('-last_update_at')[:10]
    context = {
        'latest_players_list': latest_players_list,
    }
    return render(request, 'player/index.html', context)

# Returns player overview
def overview(request, player_id):
    player = Players.objects.get(id=player_id)
    team = player.team
    skills = PlayerSkills.objects.filter(player=player_id)

    player_skills = {}
    for skill in skills:
        player_skills[skill.skill.replace(' ', '_').replace('.', '').lower()] = skill.value

    guard_skill_points = player_skills['jump_shot'] + player_skills['jump_range'] + player_skills['outside_def'] \
                        + player_skills['handling'] + player_skills['driving'] + player_skills['passing']
    forward_skill_points = player_skills['inside_shot'] + player_skills['inside_def'] \
                           + player_skills['rebounding'] + player_skills['shot_blocking']
    tsp = guard_skill_points + forward_skill_points

    context = {
        'player': player,
        'team': team,
        'skills': player_skills,
        'gsp': guard_skill_points,
        'fsp': forward_skill_points,
        'tsp': tsp,
    }
    return render(request, 'player/player_overview.html', context)
