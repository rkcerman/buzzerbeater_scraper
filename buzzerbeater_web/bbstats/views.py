from django.shortcuts import render
from django.db.models import Q
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from .processors.process import calculate_skill_points, get_skills_dict, \
    get_strategies_context, get_players_skills_info, get_player_shot_types

from .processors.query import get_schedule, get_all_teams
from .models import Matches, Players, PlayerSkills, BoxscoreStats, Shots, \
    Teams, Seasons
from .serializers import *

default_season = Seasons.objects.filter(
    end_date=None
).order_by(
    '-end_date'
)[0].id
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


@cache_page(CACHE_TTL)
def index(request):
    context = {
        'all_teams': get_all_teams(),
    }
    return render(request, 'bbstats/index.html', context)


# Returns team overview with the list of players and their skills
def team_overview(request,
                  team_id,
                  season=default_season):
    # GET params
    match_type = request.GET.get('match_type', 'standard')

    team = Teams.objects.get(id=team_id)
    team_players = Players.objects.filter(team_id=team_id)
    team_players_skills = get_players_skills_info(team_players)

    schedule = get_schedule(team, season)

    context = {
        'team': team,
        'players_skills': team_players_skills,
        'schedule': schedule,
        'season': season,
        'match_type': match_type,
    }
    return render(request, 'bbstats/team_overview.html', context)


# Returns player overview
def player_overview(request,
                    player_id,
                    season=default_season):
    # GET params
    match_type = request.GET.get('match_type', 'standard')

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

    # Further filtering based on match_types if they are defined
    if match_type == 'standard':
        boxscore_stats = boxscore_stats.filter(
            Q(boxscore__match_type__contains='league')
            | Q(boxscore__match_type__contains='cup')
        )
    else:
        boxscore_stats = boxscore_stats.filter(
            boxscore__match_type__contains=match_type
        )

    # Returns styling class and nomenclature for skills
    player_skills = get_skills_dict(skills)

    try:
        skill_points = calculate_skill_points(player_skills)
    except ValueError:
        skill_points = {}

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
        stat_match_type = boxscore.match_type

        stats.append({
            'match': stat,
            'max_minute_key': max_minute_key,
            'max_minute_value': max_minute_value,
            'match_type': stat_match_type,
            'strategies_preps': get_strategies_context(stat, stat.boxscore),
        }
        )

    # Setting up the final context
    context = {
        'player': player,
        'skills': player_skills,
        'stats': stats,
        'season': season,
        'match_type': match_type,
        **skill_points
    }

    return render(request, 'bbstats/player_overview.html', context)


# Returns match overview
def match_overview(request, match_id):
    match = Matches.objects.get(id=match_id)

    context = {
        'match': match
    }

    return render(request, 'bbstats/match_overview.html', context)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def player_stats(request, pk, season):
    """
    Returns single player's statistics for a season/list of seasons

    :param request:
    :param pk: - player ID
    :param season: - season to aggregate stats for

    GET params:
    with_fouled - boolean: aggregate shots with 'fouled' outcome
    match_type - if 'standard', agg.s only league and cup games
    filter - allows to aggregate only specific types of stats
            options: pass, shoot, guard
    """
    players = [pk]

    return get_stats(request, season, players)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def team_stats(request, pk, season):
    players = [
        BoxscoreStats.objects.filter(
            team_id=pk,
            boxscore__match__season=season
        ).values(
            'player_id'
        )
    ]

    return get_stats(request, season, players)


def get_stats(request, season, players):
    data = {}
    default_filter = ('shoot', 'guard', 'pass')

    # GET params
    with_fouled = request.GET.get('with_fouled', False)
    match_type = request.GET.get('match_type', 'standard')

    season_shots = Shots.objects.filter(
        pbp__boxscore__match__season=season
    )

    # Able to add shots with 'fouled' outcome into calculations
    if not with_fouled:
        season_shots = season_shots.exclude(outcome='fouled')
    # Only aggregate from league and cup matches if no match_type
    # Else, filter
    if match_type == 'standard':
        season_shots = season_shots.filter(
            Q(pbp__boxscore__match_type__contains='league')
            | Q(pbp__boxscore__match_type__contains='cup')
        )
    else:
        season_shots = season_shots.filter(
            pbp__boxscore__match_type__contains=match_type
        )

    # Only aggregate specific types of stats
    # To aggregate multiple types, separate by comma
    data_filter = request.GET.get('filter', default_filter)
    if 'shoot' in data_filter:
        player_shots = season_shots.filter(
            shooter__in=players,
        )
        shot_performances = get_player_shot_types(player_shots, 'shoot')
        data['shoot'] = shot_performances
    if 'guard' in data_filter:
        player_defended_shots = season_shots.filter(
            defender__in=players,
        )
        defense_performances = get_player_shot_types(player_defended_shots,
                                                     'pass')
        data['guard'] = defense_performances
    if 'pass' in data_filter:
        player_passed_shots = season_shots.filter(
            passer__in=players,
        )
        passing_performances = get_player_shot_types(player_passed_shots,
                                                     'guard')
        data['pass'] = passing_performances

    return Response(data)


class UserViewSet(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamList(generics.ListAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamsSerializer


class TeamDetail(generics.RetrieveAPIView):
    queryset = Teams.objects.all()
    serializer_class = TeamDetailSerializer


class PlayerList(generics.ListAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer


class PlayerDetail(generics.RetrieveAPIView):
    queryset = Players.objects.all()
    serializer_class = PlayersSerializer
