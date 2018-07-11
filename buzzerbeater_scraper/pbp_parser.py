import re

from buzzerbeater_scraper.items import PlayByPlayItem


# Class for parsing each play-by-play by
# assigning a play categories to each play type. Each category gets parsed differently.
class PlayByPlayParser:
    # TODO turnover should be -> X loses the ball
    # TODO steal should be -> Y steals the ball
    event_type_categories = {
        'ASSIST': 'passing',
        'BAD_PASS': ['turnover', 'passing'],
        'BASELINE_J': ['mid', 'shot'],
        'BLOWOUT': 'info',
        'BUZZERBEATER': 'info',
        'CORNER_THREE': ['three', 'shot'],
        'DOUBLE_DOUBLE': 'info',
        'DRIVING_LAYUP': ['inside', 'shot'],
        'DUNK': ['dunk', 'shot', 'inside'],
        'DUNK_MISSED': ['dunk', 'shot', 'inside'],
        'ELBOW': ['mid', 'shot'],
        'FALL_AWAY': ['mid', 'shot'],
        'FREE_THROW_MADE': 'ft',
        'FREE_THROW_MISSED': 'ft',
        'HALF_COURT_SHOT': ['three', 'shot'],
        'HALF_OVER': 'info',
        'HOOK': ['inside', 'shot'],
        'INJURY': 'info',
        'JUMP_BALL': 'info',
        'LAYUP': ['inside', 'shot'],
        'NOSHOOT_FOUL': 'foul',
        'OFF_FOUL': 'foul',
        'PERIOD_OVER': 'info',
        'PUTBACK': ['inside', 'shot'],
        'REBOUND': 'rebound',
        'REBOUND_OOB': 'info',
        'SHOOTING_FOUL': 'foul',
        'SHOT_CLOCK_ZERO': 'info',
        'SHOTSTREAKMAKE': 'info',
        'SHOTSTREAKMISS': 'info',
        'SPINNY': ['mid', 'shot'],
        'STEAL': ['turnover', 'steal'],
        'STEAL_ON_PASS': ['turnover', 'steal'],
        'STRAIGHT_ON_THREE': ['three', 'shot'],
        'STRONG': ['inside', 'shot'],
        'SUBSTITUTION': 'info',
        'SUBSTITUTION_SWAP': 'info',
        'TECHNICAL': 'foul',
        'THREE_SECOND': 'turnover',
        'TIME_OUT': 'info',
        'TIPBACK': ['inside', 'shot'],
        'TIPBACKDUNK': ['dunk', 'shot', 'inside'],
        'TOPKEY': ['mid', 'shot'],
        'TRAVEL': 'turnover',
        'VERY_LONG': ['three', 'shot'],
        'WING': ['mid', 'shot'],
        'WING_THREE': ['three', 'shot']
    }

    def parse(self, pbp_item):
        # Looks up the event type as a key value in the event_type_groups dictionary
        event_group = self.event_type_categories.get(pbp_item['event_type'])
        if 'shot' in event_group:
            self.parse_shots(self, shot_play=pbp_item)

    def parse_shots(self, shot_play):
        # Let's list all the players in this particular play

        # Turn all the Goaltends into Scoreds because noone cares
        shot_play['event'] = shot_play['event'].replace('Goaltending called', 'Scored')
        print(shot_play['event'])

        outcome = self.get_shot_outcome(shot_event=shot_play['event'])


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
        print(outcome)
        return outcome
