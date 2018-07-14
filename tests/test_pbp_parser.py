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

    # Checks if item with 'info' returns none in parse_shots
    def test_info_in_parse_shots_is_none(self):
        self.assertIsNone(PlayByPlayParser.parse_shots(self=PlayByPlayParser, shot_play=mock_info_item))

    # Checks that get_defender returns None if not string passed
    def test_only_string_allowed(self):
        self.assertIsNone(PlayByPlayParser.get_defender(shot_event=mock_dlayup_missed_item))

    # Checks that there is no defender
    def test_no_defender(self):
        self.assertEqual(PlayByPlayParser.get_defender(shot_event=mock_dlayup_missed_item['event']), [])

    # Checks that there is no defender with 'info' event
    def test_no_defender_info(self):
        self.assertEqual(PlayByPlayParser.get_defender(shot_event=mock_info_item['event']), [])

    # Checks that there is no passer
    def test_no_passer(self):
        self.assertEqual(PlayByPlayParser.get_passer(shot_event=mock_dlayup_missed_item['event']), '')

    # Checks that there is no passer with 'info' event
    def test_no_passer_info(self):
        self.assertEqual(PlayByPlayParser.get_passer(shot_event=mock_info_item['event']), '')


if __name__ == '__main__':
    unittest.main()


