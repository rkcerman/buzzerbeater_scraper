from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Teams, Players, PlayerSkills


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = ('id', 'name')


class PlayerSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerSkills
        fields = (
            'player',
            'date',
            'skill',
            'value',
        )


class PlayersSerializer(serializers.ModelSerializer):
    playerskills_set = PlayerSkillsSerializer(many=True, read_only=True)

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
            'playerskills_set',
        )


class TeamDetailSerializer(serializers.ModelSerializer):
    players_set = PlayersSerializer(many=True, read_only=True)

    class Meta:
        model = Teams
        fields = ('id', 'name', 'players_set')


# TODO might be useless
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
