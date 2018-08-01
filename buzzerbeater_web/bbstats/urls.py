from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('player/<int:player_id>/', views.player_default_overview, name='player_default_overview'),
    path('player/<int:player_id>/<int:season>', views.player_season_overview, name='player_season_overview'),
    path('player/<int:player_id>/<int:season>/<str:match_type>', views.player_overview, name='player_overview'),
    path('team/<int:team_id>', views.team_overview, name='team_overview'),
]
