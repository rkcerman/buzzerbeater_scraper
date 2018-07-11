import re
from buzzerbeater_scraper.pbp_tags import PLAY_TYPE_CATEGORIES

from buzzerbeater_scraper.items import ShotsItem

# TODO badly needs unit testing
# Class for parsing each play-by-play by
# assigning a play categories to each play type. Each category gets parsed differently.
class PlayByPlayParser:

    # Reads play type and decides what to do with the play
    def parse(self, pbp_item):
        # Looks up the play type as a key value in the event_type_groups dictionary
        event_group = PLAY_TYPE_CATEGORIES.get(pbp_item['event_type'])

        if 'shot' in event_group:
            return self.parse_shots(self, shot_play=pbp_item)

    def parse_shots(self, shot_play):
        print("Parsing shot -----")
        # Turn all the Goaltends into Scoreds because noone cares
        shot_play['event'] = shot_play['event'].replace('Goaltending called', 'Scored')

        outcome = self.get_shot_outcome(shot_event=shot_play['event'])
        defensive_play = self.get_defender(shot_event=shot_play['event'])

        passer = self.get_passer(shot_event=shot_play['event'])

        for player_id in re.findall(pattern='(\d+)', string=shot_play['event']):
            if player_id not in (defensive_play, passer):
                shooter = player_id
                break

        shots_item = ShotsItem(
            pbp_id=shot_play['id'],
            shooter=shooter,
            outcome=outcome,
        )

        try:
            shots_item['defender'] = defensive_play[1]
            shots_item['defense_type'] = defensive_play[0]
        except IndexError as e:
            shots_item['defender'] = None
            shots_item['defense_type'] = None
            print("No defender.")

        print("Passer: " + passer)
        if passer != '':
            shots_item['passer'] = passer
        else:
            shots_item['passer'] = None

        return shots_item

    # TODO research if all the methods below should actually be static or not
    # Gets the outcome of the shot (scored? missed? blocked?)
    @staticmethod
    def get_shot_outcome(shot_event):
        # Get the outcome
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
        patterns = [
            ', guarded closely by (\d+)',
            'as (\d+) rotates over and alters his shot',
            ' under pressure from (\d+)',
            ' with (\d+) right in his face',
            ' over (\d+).',
            ' after (\d+) backed off slightly'
        ]

        defender_list = []
        for pattern in patterns:
            search = re.search(pattern, shot_event)
            if search is not None:
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
        print(defender_list)
        return defender_list

    # Finds the shot passer based on the regex patterns
    @staticmethod
    def get_passer(shot_event):
        patterns = [
            'off of a nice pass from (\d+)',
            '(\d+) gets off a great pass to',
            '(\d+) opens up the play with a pass to',
            '(\d+) threads a pass through the defense and finds',
            'finds (\d+) in space'
        ]

        passer = ''
        for pattern in patterns:
            search = re.search(pattern, shot_event)
            if search is not None:
                passer = search.group(1)
        return passer
