import unittest
from scrapy.selector import Selector, SelectorList

from buzzerbeater_scraper.items import BoxscoreItem
from tests.mock_boxscore_data import MOCK_BOXSCORE_DICT, MOCK_BOXSCORE_XML
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
                boxscore_item=self.boxscore_item
            )
        )
        self.assertIsNone(
            BoxscoreParser.get_strategies(
                self=BoxscoreParser,
                team_xml=12321,
                team='bla',
                boxscore_item=self.boxscore_item
            )
        )

    # Test if scores are correct
    def test_scores_per_quarter(self):
        self.assertDictEqual(
            BoxscoreParser.get_scores_by_qtr(
                self=BoxscoreParser,
                boxscore_xml=self.boxscore_xml_sel,
                match_id=101245565
            ),
            MOCK_BOXSCORE_DICT
        )

    # Test if strategies are correct
    def test_strategies(self):
        test_home_item = BoxscoreParser.get_strategies(
            self=BoxscoreParser,
            team_xml=self.away_boxscore_xml,
            team='away',
            boxscore_item=self.boxscore_item
        )
        test_away_item = BoxscoreParser.get_strategies(
            self=BoxscoreParser,
            team_xml=self.home_boxscore_xml,
            team='home',
            boxscore_item=self.boxscore_item
        )
        self.assertEqual(
            test_away_item['away_off_strategy'],
            'RunAndGun'
        )
        self.assertEqual(
            test_home_item['home_off_strategy'],
            'Patient'
        )
        self.assertEqual(
            test_away_item['away_def_strategy'],
            'ManToMan'
        )
        self.assertEqual(
            test_home_item['home_def_strategy'],
            '23Zone'
        )

    def test_preps(self):
        test_home_item = BoxscoreParser.get_preps(
            self=BoxscoreParser,
            team_xml=self.away_boxscore_xml,
            team='away',
            boxscore_item=self.boxscore_item
        )
        test_away_item = BoxscoreParser.get_preps(
            self=BoxscoreParser,
            team_xml=self.home_boxscore_xml,
            team='home',
            boxscore_item=self.boxscore_item
        )
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


    # Test the output of parse()
    def test_parse(self):
        test_parse_item = BoxscoreParser.parse(
            self=BoxscoreParser,
            boxscore_xml=self.boxscore_xml_sel
        )
        test_score_table_item = test_parse_item[0]
        test_boxscore_item = test_parse_item[1]

        # Method testing the score table item
        self.assertEqual(
            test_score_table_item,
            MOCK_BOXSCORE_DICT
        )

        # Methods testing the boxscore_item
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
            test_boxscore_item['home_def_strategy'],
            '23Zone'
        )
