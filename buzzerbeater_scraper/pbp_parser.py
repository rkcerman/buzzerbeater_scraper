import re
import logging

from buzzerbeater_scraper.items import ShotsItem
from buzzerbeater_scraper.regex_patterns import PASSER_PATTERNS, DEFENDER_PATTERNS


# TODO badly needs unit testing
# Class for parsing each play-by-play by
# assigning a play categories to each play type. Each category gets parsed differently.
class PlayByPlayParser:

    # Reads play type and decides what to do with the play
    # If 'shot', returns ShotItem
    def parse(self, pbp_item):
        if 'shot' in pbp_item['play_tags']:
            return self.parse_shots(self, shot_play=pbp_item)

    def parse_shots(self, shot_play):
        if 'shot' in shot_play['play_tags']:
            logging.info('PARSING SHOTS')

            # Turn all the Goaltends into Scores because noone cares
            shot_play['event'] = shot_play['event'].replace('Goaltending called', 'Scored')

            outcome = self.get_shot_outcome(shot_event=shot_play['event'])
            defensive_play = self.get_defender(shot_event=shot_play['event'])

            passer = self.get_passer(shot_event=shot_play['event'])

            for player_id in re.findall(pattern='(\d+)', string=shot_play['event']):
                if player_id not in (defensive_play, passer):
                    shooter = player_id
                    break

            # TODO unit test empty shooter (which should never happen)
            shots_item = ShotsItem(
                pbp_id=shot_play['id'],
                shooter=shooter,
                outcome=outcome,
            )

            try:
                shots_item['defender'] = defensive_play[1]
                shots_item['defense_type'] = defensive_play[0]
            except IndexError:
                shots_item['defender'] = None
                shots_item['defense_type'] = None

            if passer != '':
                shots_item['passer'] = passer
            else:
                shots_item['passer'] = None

            return shots_item
        else:
            print('Not a shot')
            return None

    # TODO research if all the methods below should actually be static or not
    # Gets the outcome of the shot (scored? missed? blocked?)
    @staticmethod
    def get_shot_outcome(shot_event):

        # Get the outcome through regex
        outcome = re.search('(Shot missed|Scored|Shot blocked)', shot_event)

        # Turn all the shot outcomes (Scored | Missed | Shot Blocked) into lowercase with underscores
        if outcome is not None:
            outcome = outcome.group(0)
            outcome = outcome.replace('.', '').replace(' ', '_').lower()
        else:
            outcome = 'fouled'
        return outcome

    # Finds the shot defender based on the regex patterns
    @staticmethod
    def get_defender(shot_event):
        try:
            patterns = DEFENDER_PATTERNS

            # Create a list with the defense type and the defender
            defender_list = []
            for pattern in patterns:
                search = re.search(pattern, shot_event)
                if search is not None:

                    # Turn the pattern into a nice lower case enum with underscores
                    pattern = re.sub(pattern='(, |^ |\.)', repl='', string=pattern)
                    pattern = re.sub(pattern='( \(\\\\d\+\) )', repl='_', string=pattern)
                    pattern = re.sub(pattern='( \(\\\\d\+\))', repl='', string=pattern)
                    pattern = re.sub(pattern=' ', repl='_', string=pattern)
                    pattern = pattern.lower()
                    defender = search.group(1)
                    defender_list = [
                        pattern,
                        defender
                    ]
            return defender_list
        except TypeError as e:
            print(e)
            print("Only string allowed")

    # Finds the shot passer based on the regex patterns
    @staticmethod
    def get_passer(shot_event):
        try:
            patterns = PASSER_PATTERNS

            passer = ''
            for pattern in patterns:
                search = re.search(pattern, shot_event)
                if search is not None:
                    passer = search.group(1)
            return passer
        except TypeError as e:
            print(e)
            print("Only string allowed")
