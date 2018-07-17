import unittest
from scrapy.selector import Selector, SelectorList

from buzzerbeater_scraper.items import BoxscoreItem
from tests.mock_boxscore_data import MOCK_BOXSCORE_DICT, MOCK_BOXSCORE_XML
from buzzerbeater_scraper.boxscore_parser import BoxscoreParser


class TestBoxscoreParser(unittest.TestCase):

    boxscore_xml_sel = Selector(text=MOCK_BOXSCORE_XML)
    away_boxscore_xml = boxscore_xml_sel.xpath('//match/awayteam')
    home_boxscore_xml = boxscore_xml_sel.xpath('//match/hometeam')
    boxscore_item = BoxscoreItem(match_id=101245565)

    # Test invalid type for scores_by_quarter
    def test_invalid_types(self):
        self.assertIsNone(
            BoxscoreParser.get_scores_by_qtr(self=BoxscoreParser, boxscore_xml=1232, match_id=1)
        )
        self.assertIsNone(
            BoxscoreParser.get_strategies(self=BoxscoreParser, team_xml=12321, team='away', boxscore_item=self.boxscore_item)
        )
        self.assertIsNone(
            BoxscoreParser.get_strategies(self=BoxscoreParser, team_xml=12321, team='bla', boxscore_item=self.boxscore_item)
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

    # Test if tactics are correct
    def test_tactics(self):
        self.assertEqual(
            BoxscoreParser.get_strategies(
                self=BoxscoreParser,
                team_xml=self.away_boxscore_xml,
                team='away',
                boxscore_item=self.boxscore_item
            )['away_off_strategy'],
            'RunAndGun'
        )
        self.assertEqual(
            BoxscoreParser.get_strategies(
                self=BoxscoreParser,
                team_xml=self.home_boxscore_xml,
                team='home',
                boxscore_item=self.boxscore_item
            )['home_off_strategy'],
            'Patient'
        )
        self.assertEqual(
            BoxscoreParser.get_strategies(
                self=BoxscoreParser,
                team_xml=self.away_boxscore_xml,
                team='away',
                boxscore_item=self.boxscore_item
            )['away_def_strategy'],
            'ManToMan'
        )
        self.assertEqual(
            BoxscoreParser.get_strategies(
                self=BoxscoreParser,
                team_xml=self.home_boxscore_xml,
                team='home',
                boxscore_item=self.boxscore_item
            )['home_def_strategy'],
            '23Zone'
        )
