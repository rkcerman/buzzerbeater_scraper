from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Players, PlayerSkills

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
    player = Players.objects.get(id=player_id)
    team = player.team
    skills = PlayerSkills.objects.filter(player=player_id)

    player_skills = {}
    nomenclature = []
    for skill in skills:
        skill_name = skill.skill.replace(' ', '_').replace('.', '').lower()
        player_skills[skill_name] = [skill.value, skills_mapping[skill.value]]

    guard_skill_points = player_skills['jump_shot'][0] + player_skills['jump_range'][0] + player_skills['outside_def'][0] \
                        + player_skills['handling'][0] + player_skills['driving'][0] + player_skills['passing'][0]
    forward_skill_points = player_skills['inside_shot'][0] + player_skills['inside_def'][0] \
                           + player_skills['rebounding'][0] + player_skills['shot_blocking'][0]
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
