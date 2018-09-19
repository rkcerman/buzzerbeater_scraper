from django.shortcuts import render
from django.db.models import Q
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404

from .processors.process import calculate_skill_points, get_skills_nomenclature, \
    get_potential_context, get_strategies_context, get_players_skills_potential, get_player_shot_types

from .processors.query import get_schedule, get_all_teams
from .models import Players, PlayerSkills, BoxscoreStats, Shots, Teams
from .serializers import *

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
        potential = get_potential_context(player)
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
            'strategies_preps': get_strategies_context(stat, stat.boxscore),
            'shots': player_shots
        }
        )

    shot_performances = get_player_shot_types(player_shots, 'shoot')
    defense_performances = get_player_shot_types(player_defended_shots, 'pass')
    passing_performances = get_player_shot_types(player_passed_shots, 'guard')

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


class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamList(generics.ListAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer


class TeamDetail(generics.RetrieveAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamDetailsSerializer


class PlayerList(generics.ListAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer


class PlayerDetail(generics.RetrieveAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
