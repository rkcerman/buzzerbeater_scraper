import unittest

from tests.mock_pbp_data import mock_info_item, mock_dlayup_missed_item
from buzzerbeater_scraper.pbp_parser import PlayByPlayParser
from buzzerbeater_scraper.items import PlayByPlayItem, ShotsItem


class TestPlayByPlayParser(unittest.TestCase):

    # Checks if SUBSTITUTION gets correctly assigned 'info' tag
    def test_info_is_none(self):
        self.assertIsNone(PlayByPlayParser.parse(self=PlayByPlayParser, pbp_item=mock_info_item))

    # Checks if item with 'shot' tag returns ShotItem
    def test_is_shot(self):
        self.assertIsInstance(PlayByPlayParser.parse(self=PlayByPlayParser, pbp_item=mock_dlayup_missed_item),
                              ShotsItem
                              )

if __name__ == '__main__':
    unittest.main()


