import logging
import unittest
from scrapy.selector import Selector, SelectorList

from buzzerbeater_scraper.items import BoxscoreItem
from tests.mock_boxscore_data import MOCK_SCORE_TABLE_DICT, MOCK_BOXSCORE_XML, MOCK_BOXSCORE_STATS_DICT
from buzzerbeater_scraper.boxscore_parser import BoxscoreParser


class TestBoxscoreParser(unittest.TestCase):

    boxscore_xml_sel = Selector(
        text=MOCK_BOXSCORE_XML,
        type='xml'
    )
    away_boxscore_xml = boxscore_xml_sel.xpath('//match/awayTeam')
    home_boxscore_xml = boxscore_xml_sel.xpath('//match/homeTeam')
    boxscore_item = BoxscoreItem(match_id=101245565)

    # Test invalid type for scores_by_quarter
    def test_invalid_types(self):
        print('test_invalid_types')
        self.assertIsNone(
            BoxscoreParser.get_scores_by_qtr(
                self=BoxscoreParser,
                boxscore_xml=1232,
                match_id=1
            )
        )
        self.assertIsNone(
            BoxscoreParser.get_strategies(
                self=BoxscoreParser,
                team_xml=12321,
                team='away',
                boxscore_item=self.boxscore_item.copy()
            )
        )
        self.assertIsNone(
            BoxscoreParser.get_strategies(
                self=BoxscoreParser,
                team_xml=12321,
                team='bla',
                boxscore_item=self.boxscore_item.copy()
            )
        )

    # Test if scores are correct
    def test_scores_per_quarter(self):
        print('test_scores_per_quarter')
        self.assertDictEqual(
            BoxscoreParser.get_scores_by_qtr(
                self=BoxscoreParser,
                boxscore_xml=self.boxscore_xml_sel,
                match_id=101245565
            ),
            MOCK_SCORE_TABLE_DICT
        )

    # Test if strategies are correct
    def test_strategies(self):
        print('test_strategies')

        test_away_item = BoxscoreParser.get_strategies(
            self=BoxscoreParser,
            team_xml=self.away_boxscore_xml,
            team='away',
            boxscore_item=self.boxscore_item.copy()
        )
        test_home_item = BoxscoreParser.get_strategies(
            self=BoxscoreParser,
            team_xml=self.home_boxscore_xml,
            team='home',
            boxscore_item=self.boxscore_item.copy()
        )
        # Away team tests
        self.assertEqual(
            test_away_item['away_off_strategy'],
            'RunAndGun'
        )
        self.assertEqual(
            test_away_item['away_def_strategy'],
            'ManToMan'
        )
        # Home team tests
        self.assertEqual(
            test_home_item['home_off_strategy'],
            'Patient'
        )
        self.assertEqual(
            test_home_item['home_def_strategy'],
            '23Zone'
        )

    # Testing match preps
    def test_preps(self):
        print('test_preps')
        test_away_item = BoxscoreParser.get_preps(
            self=BoxscoreParser,
            team_xml=self.away_boxscore_xml,
            team='away',
            boxscore_item=self.boxscore_item.copy()
        )
        test_home_item = BoxscoreParser.get_preps(
            self=BoxscoreParser,
            team_xml=self.home_boxscore_xml,
            team='home',
            boxscore_item=self.boxscore_item.copy()
        )
        # Away team tests
        self.assertEqual(
            test_away_item['away_prep_focus'],
            'Inside'
        )
        self.assertEqual(
            test_away_item['away_prep_focus_matched'],
            'miss'
        )
        self.assertEqual(
            test_away_item['away_prep_pace'],
            None
        )
        self.assertEqual(
            test_away_item['away_prep_pace_matched'],
            None
        )
        # Home team tests
        self.assertEqual(
            test_home_item['home_prep_focus'],
            None
        )
        self.assertEqual(
            test_home_item['home_prep_focus_matched'],
            None
        )
        self.assertEqual(
            test_home_item['home_prep_pace'],
            'Fast'
        )
        self.assertEqual(
            test_home_item['home_prep_pace_matched'],
            'hit'
        )

    # Testing team ratings for both away and home teams
    def test_team_ratings(self):
        print('test_team_ratings')
        test_home_item = BoxscoreParser.get_team_ratings(
            self=BoxscoreParser,
            team_xml=self.home_boxscore_xml,
            team='home',
            boxscore_item=self.boxscore_item.copy()
        )
        test_away_item = BoxscoreParser.get_team_ratings(
            self=BoxscoreParser,
            team_xml=self.away_boxscore_xml,
            team='away',
            boxscore_item=self.boxscore_item.copy()
        )
        # Away team tests
        self.assertEqual(
            test_away_item['away_outside_off'],
            7.6
        )
        self.assertEqual(
            test_away_item['away_inside_off'],
            6
        )
        self.assertEqual(
            test_away_item['away_outside_def'],
            5.6
        )
        self.assertEqual(
            test_away_item['away_inside_def'],
            7.3
        )
        self.assertEqual(
            test_away_item['away_reb'],
            5.3
        )
        self.assertEqual(
            test_away_item['away_off_flow'],
            5
        )
        # Home team tests
        self.assertEqual(
            test_home_item['home_outside_off'],
            6.6
        )
        self.assertEqual(
            test_home_item['home_inside_off'],
            7
        )
        self.assertEqual(
            test_home_item['home_outside_def'],
            5.6
        )
        self.assertEqual(
            test_home_item['home_inside_def'],
            9.3
        )
        self.assertEqual(
            test_home_item['home_reb'],
            7.6
        )
        self.assertEqual(
            test_home_item['home_off_flow'],
            5.6
        )

    # Test the get_stats function
    def test_stats(self):
        print('test_stats')
        test_away_item = BoxscoreParser.get_stats(
            self=BoxscoreParser,
            team_xml=self.away_boxscore_xml,
            match_id=101245565,
            team_id=58377
        )
        for field in test_away_item[0]:
            print('field: ', field)
            self.assertEqual(
                test_away_item[0][field],
                MOCK_BOXSCORE_STATS_DICT[field]
            )

    # Test the output of parse()
    def test_parse(self):
        print('test_parse')

        test_parse_item = BoxscoreParser.parse(
            self=BoxscoreParser,
            boxscore_xml=self.boxscore_xml_sel
        )
        test_score_table_item = test_parse_item[0]
        test_boxscore_item = test_parse_item[1]
        test_boxscore_stats_item = test_parse_item[2]

        # Method testing the score table item
        self.assertEqual(
            test_score_table_item,
            MOCK_SCORE_TABLE_DICT
        )

        # Methods testing the boxscore_item
        self.assertEqual(
            test_boxscore_item['match_id'],
            101245565
        )
        self.assertEqual(
            test_boxscore_item['match_type'],
            'league.rs'
        )
        self.assertEqual(
            test_boxscore_item['away_off_strategy'],
            'RunAndGun'
        )
        self.assertEqual(
            test_boxscore_item['home_off_strategy'],
            'Patient'
        )
        self.assertEqual(
            test_boxscore_item['away_def_strategy'],
            'ManToMan'
        )
        self.assertEqual(
            test_boxscore_item['away_prep_focus'],
            'Inside'
        )
        self.assertEqual(
            test_boxscore_item['away_prep_focus_matched'],
            'miss'
        )
        self.assertEqual(
            test_boxscore_item['away_prep_pace'],
            None
        )
        self.assertEqual(
            test_boxscore_item['away_prep_pace_matched'],
            None
        )
        self.assertEqual(
            test_boxscore_item['home_def_strategy'],
            '23Zone'
        )
        self.assertEqual(
            test_boxscore_item['home_prep_pace'],
            'Fast'
        )
        self.assertEqual(
            test_boxscore_item['home_prep_pace_matched'],
            'hit'
        )

        # Methods testing team ratings
        # Away team tests
        self.assertEqual(
            test_boxscore_item['away_outside_off'],
            7.6
        )
        self.assertEqual(
            test_boxscore_item['away_inside_off'],
            6
        )
        self.assertEqual(
            test_boxscore_item['away_outside_def'],
            5.6
        )
        self.assertEqual(
            test_boxscore_item['away_inside_def'],
            7.3
        )
        self.assertEqual(
            test_boxscore_item['away_reb'],
            5.3
        )
        self.assertEqual(
            test_boxscore_item['away_off_flow'],
            5
        )
        # Home team tests
        self.assertEqual(
            test_boxscore_item['home_outside_off'],
            6.6
        )
        self.assertEqual(
            test_boxscore_item['home_inside_off'],
            7
        )
        self.assertEqual(
            test_boxscore_item['home_outside_def'],
            5.6
        )
        self.assertEqual(
            test_boxscore_item['home_inside_def'],
            9.3
        )
        self.assertEqual(
            test_boxscore_item['home_reb'],
            7.6
        )
        self.assertEqual(
            test_boxscore_item['home_off_flow'],
            5.6
        )

        # Methods testing get_stats
        for player in test_boxscore_stats_item:
            if player['player_id'] == 28668697:
                for field in player:
                    print('field: ', field)
                    self.assertEqual(
                        player[field],
                        MOCK_BOXSCORE_STATS_DICT[field]
                    )
