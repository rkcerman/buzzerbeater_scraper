from datetime import datetime

from django.test import TestCase

from . import views

from .models import Teams, Players
from .processors.process import *


class ViewTester(TestCase):
    mock_def_stats = [
        {
            'shot_type': 'DRIVING_LAYUP',
            'made_fg': 45,
            'attempted_fg': 90,
            'fg_per': 0.5,
        },
        {
            'shot_type': 'BASELINE_J',
            'made_fg': 12,
            'attempted_fg': 25,
            'fg_per': 0.48,
        }
    ]

    def setUp(self):
        Teams.objects.create(
            id=58420,
            name='Ethereum Traders'
        )
        Players.objects.create(
            id=123,
            created_at=datetime.now(),
            weekly_salary=10000,
            dmi=99876,
            age=24,
            height=204,
            position='Power Forward',
            team_id=58420,
            potential=5,
            name='Kok',

        )

    def test_calc_player_defense_per(self):
        self.assertEqual(
            calc_player_defense_per(self.mock_def_stats),
            0.5
        )
