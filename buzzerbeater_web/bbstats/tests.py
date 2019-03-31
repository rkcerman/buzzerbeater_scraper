from datetime import datetime

from django.test import TestCase

from . import views

from .models import *
from .processors.process import *
from .processors.query import get_player_36m_stats


class TestViews(TestCase):
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
        Teams.objects.create(
            id=58377,
            name='BK Sever 5'
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
        Matches.objects.create(
            id=321,
            match_date=datetime.now(),
            home_team_id=58420,
            away_team_id=58377,
            season=43,
        )
        Boxscores.objects.create(
            match_id=321,
            away_outside_off=5.1,
            away_inside_off=6.2,
            away_outside_def=7.3,
            away_inside_def=8.4,
            away_reb=9.5,
            away_off_flow=10.6,
            home_outside_off=1.6,
            home_inside_off=2.5,
            home_outside_def=3.4,
            home_inside_def=4.3,
            home_reb=5.2,
            home_off_flow=6.1,
            match_type='league.rs',
            away_off_strategy='Push',
            away_def_strategy='ManToMan',
            home_off_strategy='LowPost',
            home_def_strategy='23Zone',
        )
        BoxscoreStats.objects.create(
            boxscore_id=321,
            player_id=123,
            pg_min=30,
            sg_min=6,
            sf_min=0,
            pf_min=0,
            c_min=0,
            fgm=4,
            fga=9,
            tpm=1,
            tpa=2,
            ftm=2,
            fta=4,
            oreb=1,
            reb=4,
            ast=6,
            t_o=2,
            stl=2,
            blk=0,
            pf=2,
            pts=8,
            rating=11.0,
            team_id=58420,
        )

    def test_calc_player_defense_per(self):
        print('Player defense fg% calculation - ')
        self.assertEqual(
            calc_player_defense_per(self.mock_def_stats),
            0.5
        )


class TestApi(TestCase):

    def setUp(self):
        Teams.objects.create(
            id=58420,
            name='Ethereum Traders'
        )
        Teams.objects.create(
            id=58377,
            name='BK Sever 5'
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
        Matches.objects.create(
            id=321,
            match_date=datetime.now(),
            home_team_id=58420,
            away_team_id=58377,
            season=43,
        )
        Matches.objects.create(
            id=432,
            match_date=datetime.now(),
            home_team_id=58377,
            away_team_id=58420,
            season=44,
        )
        Boxscores.objects.create(
            match_id=321,
            away_outside_off=5.1,
            away_inside_off=6.2,
            away_outside_def=7.3,
            away_inside_def=8.4,
            away_reb=9.5,
            away_off_flow=10.6,
            home_outside_off=1.6,
            home_inside_off=2.5,
            home_outside_def=3.4,
            home_inside_def=4.3,
            home_reb=5.2,
            home_off_flow=6.1,
            match_type='league.rs',
            away_off_strategy='Push',
            away_def_strategy='ManToMan',
            home_off_strategy='LowPost',
            home_def_strategy='23Zone',
        )
        Boxscores.objects.create(
            match_id=432,
            away_outside_off=5.1,
            away_inside_off=6.2,
            away_outside_def=7.3,
            away_inside_def=8.4,
            away_reb=9.5,
            away_off_flow=10.6,
            home_outside_off=1.6,
            home_inside_off=2.5,
            home_outside_def=3.4,
            home_inside_def=4.3,
            home_reb=5.2,
            home_off_flow=6.1,
            match_type='league.rs',
            away_off_strategy='Push',
            away_def_strategy='ManToMan',
            home_off_strategy='LowPost',
            home_def_strategy='23Zone',
        )
        BoxscoreStats.objects.create(
            boxscore_id=321,
            player_id=123,
            pg_min=30,
            sg_min=6,
            sf_min=0,
            pf_min=0,
            c_min=0,
            fgm=4,
            fga=9,
            tpm=1,
            tpa=2,
            ftm=2,
            fta=4,
            oreb=1,
            reb=4,
            ast=6,
            t_o=2,
            stl=2,
            blk=0,
            pf=2,
            pts=8,
            rating=11.0,
            team_id=58420,
        )
        BoxscoreStats.objects.create(
            boxscore_id=432,
            player_id=123,
            pg_min=0,
            sg_min=0,
            sf_min=34,
            pf_min=1,
            c_min=0,
            fgm=5,
            fga=6,
            tpm=2,
            tpa=3,
            ftm=6,
            fta=6,
            oreb=0,
            reb=5,
            ast=8,
            t_o=4,
            stl=3,
            blk=1,
            pf=1,
            pts=18,
            rating=13.0,
            team_id=58420,
        )

    def test_player_36m_stats(self):
        stats = get_player_36m_stats(123)
        season_44 = stats[0]
        self.assertEqual(
            44,
            season_44['boxscore__match__season']
        )
        self.assertEqual(
            18.51,
            round(season_44['pts'], 2)
        )
        self.assertEqual(
            8.23,
            round(season_44['ast'], 2)
        )
        self.assertEqual(
            5.14,
            round(season_44['reb'], 2)
        )
        self.assertEqual(
            3.09,
            round(season_44['stl'], 2)
        )
        self.assertEqual(
            1.03,
            round(season_44['blk'], 2)
        )
        self.assertEqual(
            4.11,
            round(season_44['t_o'], 2)
        )
