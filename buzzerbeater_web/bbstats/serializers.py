from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Teams, Players


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ('id', 'name')


class PlayersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = (
            'id',
            'created_at',
            'last_update_at',
            'weekly_salary',
            'dmi',
            'age',
            'height',
            'position',
            'name',
            'team_id',
            'transfer_estimate',
            'potential',
        )


class TeamDetailsSerializer(serializers.ModelSerializer):
    players_set = PlayersSerializer(many=True, read_only=True)

    class Meta:
        model = Teams
        fields = ('id', 'name', 'players_set')

class PlayerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = (
            'id',
            'created_at',
            'last_update_at',
            'weekly_salary',
            'dmi',
            'age',
            'height',
            'position',
            'name',
            'team_id',
            'transfer_estimate',
            'potential',
        )
