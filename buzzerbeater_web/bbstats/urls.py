from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('players/<int:player_id>/', views.player_overview, name='player_default_overview'),
    path('players/<int:player_id>/season/<int:season>/', views.player_overview, name='player_season_overview'),
    path('teams/<int:team_id>/', views.team_overview, name='team_overview'),
    path('teams/<int:team_id>/season/<int:season>/', views.team_overview, name='team_season_overview'),
    path('matches/<int:match_id>/', views.match_overview, name='match_overview'),
    url(r'^api/teams/$', views.TeamList.as_view()),
    url(r'^api/teams/(?P<pk>[0-9]+)/$', views.TeamDetail.as_view(), name='team_detail'),
    url(r'^api/teams/(?P<pk>[0-9]+)/stats/(?P<season>[0-9]+)/$', views.team_stats, name='team_stats'),
    url(r'^api/players/$', views.PlayerList.as_view()),
    url(r'^api/players/(?P<pk>[0-9]+)/$', views.PlayerDetail.as_view()),
    url(r'^api/players/(?P<pk>[0-9]+)/stats/(?P<season>[0-9]+)/$', views.player_stats, name='player_stats'),
]
