import unittest
from scrapy.selector import Selector, SelectorList
from tests.mock_boxscore_data import MOCK_BOXSCORE_DIV, BOXSCORE_MOCK_DICT
from buzzerbeater_scraper.boxscore_parser import BoxscoreParser


class TestBoxscoreParser(unittest.TestCase):

    boxscore_div_sel = Selector(text=MOCK_BOXSCORE_DIV)

    # Test invalid type for scores_by_quarter
    def test_invalid_types(self):
        self.assertIsNone(
            BoxscoreParser.get_scores_by_quarter(self=BoxscoreParser, box_score_div=12321, match_id=1)
        )
        self.assertIsNone(
            BoxscoreParser.get_tactics(self=BoxscoreParser, box_score_div=12321)
        )

    # Test if scores are correct
    def test_scores_per_quarter(self):
        self.assertDictEqual(
            BoxscoreParser.get_scores_by_quarter(
                self=BoxscoreParser,
                box_score_div=self.boxscore_div_sel,
                match_id=1234,
            ),
            BOXSCORE_MOCK_DICT
        )

    # Test if tactics are correct
    def test_tactics(self):
        self.assertEqual(
            BoxscoreParser.get_tactics(
                self=BoxscoreParser,
                box_score_div=self.boxscore_div_sel
            )['away_off_tactic'],
            'push_the_ball'
        )
