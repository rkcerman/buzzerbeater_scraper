import unittest

from tests.mock_pbp_data import mock_info_item, mock_dlayup_missed_item, mock_no_event_item
from buzzerbeater_scraper.pbp_parser import PlayByPlayParser
from buzzerbeater_scraper.items import PlayByPlayItem, ShotsItem
from buzzerbeater_scraper.regex_patterns import PASSER_PATTERNS, DEFENDER_PATTERNS


class TestPlayByPlayParser(unittest.TestCase):

    test_defended_list = []
    test_passer_list = []

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

    # Checking if it parses the defenders correctly with the list of regex patterns
    def test_defenders(self):
        print('------ Testing defender regex patterns')

        # Creating a test list of mock shot items for each defense type
        for d_pattern in DEFENDER_PATTERNS:
            event = '987654321 attempts a jump-shot from the wing.  Shot missed.'.replace('. ', d_pattern)
            mock_no_event_item['event'] = event.replace('(\d+)', '1234567')
            print("Mock defended item: " + mock_no_event_item['event'])
            self.test_defended_list.append(
                mock_no_event_item
            )

        # Testing for each defense type
        for defended_item in self.test_defended_list:
            print('Defended item: ' + defended_item['event'])
            defense_list = PlayByPlayParser.get_defender(shot_event=defended_item['event'])
            self.assertEqual(defense_list[1], '1234567')

    # Checking if it parses the passers correctly with the list of regex patterns
    def test_passers(self):
        print('------ Testing passer regex patterns')

        # Creating a test list of mock shot items for each pass  type
        for p_pattern in PASSER_PATTERNS:
            event = '987654321 attempts a jump-shot from the wing.  Shot missed.'.replace('. ', p_pattern)
            mock_no_event_item['event'] = event.replace('(\d+)', '1234567')
            print("Mock passed item: " + mock_no_event_item['event'])
            self.test_passer_list.append(
                mock_no_event_item
            )

        # Testing for each pass type
        for passed_item in self.test_passer_list:
            print('Passed item: ' + passed_item['event'])
            passer = PlayByPlayParser.get_passer(shot_event=passed_item['event'])
            self.assertEqual(passer, '1234567')

if __name__ == '__main__':
    unittest.main()
