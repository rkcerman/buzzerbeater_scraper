from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Players


def index(request):
    latest_players_list = Players.objects.order_by('-last_update_at')[:10]
    context = {
        'latest_players_list': latest_players_list,
    }
    return render(request, 'player/index.html', context)

def overview(request, player_id):
    player = Players.objects.get(id=player_id)
    context = {
        'player': player,
    }
    return render(request, player)
