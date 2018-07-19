from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("BB Players app")

def overview(request, player_id):
    response = 'Player id: %s.'
    return HttpResponse(response % player_id)
