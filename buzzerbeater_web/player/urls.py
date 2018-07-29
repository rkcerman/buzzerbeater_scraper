from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:player_id>/', views.default_overview, name='default_overview'),
    path('<int:player_id>/<int:season>', views.overview, name='overview'),
]
