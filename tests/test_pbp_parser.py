import unittest

from tests.mock_pbp_data import mock_info_item
from buzzerbeater_scraper.pbp_parser import PlayByPlayParser
from buzzerbeater_scraper.items import PlayByPlayItem, ShotsItem


class TestPlayByPlayParser(unittest.TestCase):

    def test_info_is_none(self):
        self.assertIsNone(PlayByPlayParser.parse(self=PlayByPlayParser, pbp_item=mock_info_item))

if __name__ == '__main__':
    unittest.main()


