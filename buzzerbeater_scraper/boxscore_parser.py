import logging
import traceback

from scrapy.selector import Selector, SelectorList
from buzzerbeater_scraper.items import ScoreTableItem, BoxscoreItem


class BoxscoreParser:

    # A function that parses through the boxscore page (with the help of other functions)
    # Returns boxscore_item together with score_table
    def parse(self, boxscore_xml):
        match_id = int(boxscore_xml.xpath('//match/@id').extract_first())
        score_table_items = self.get_scores_by_qtr(
            self=self,
            boxscore_xml=boxscore_xml,
            match_id=match_id)
        away_team_xml = boxscore_xml.xpath('//match/awayTeam')
        home_team_xml = boxscore_xml.xpath('//match/homeTeam')
        boxscore_item = BoxscoreItem(match_id=match_id)

        for i, team_xml in enumerate([away_team_xml, home_team_xml]):
            if i == 0:
                team = 'away'
            else:
                team = 'home'
            boxscore_item = self.get_strategies(
                self=self,
                team_xml=team_xml,
                team=team,
                boxscore_item=boxscore_item
            )
            

        items = [score_table_items, boxscore_item]
        return items

    # Parses the final score table
    # Returns the list of ScoreTableItem
    def get_scores_by_qtr(self, boxscore_xml, match_id):
        try:
            away_team_scores = boxscore_xml.xpath('//match/awayTeam/score/@partials').extract_first().split(',')
            home_team_scores = boxscore_xml.xpath('//match/homeTeam/score/@partials').extract_first().split(',')
            score_table_item = ScoreTableItem(match_id=match_id)

            score_table_items = {}
            scores_zip = list(zip(away_team_scores, home_team_scores))

            # Iterates through list of scores to create a list with score table items
            for i, qtr in enumerate(scores_zip):
                item = score_table_item.copy()
                item['qtr'] = i+1
                item['away_team_score'] = int(qtr[0])
                item['home_team_score'] = int(qtr[1])
                score_table_items[i+1] = item

            print(score_table_items)

            return score_table_items
        except AttributeError as e:
            logging.error('Only accepting scrapy.selector.Selector type')
            print(traceback.print_tb(e.__traceback__))

    # Gets offensive and defensive strategies used by the (away or home) team
    def get_strategies(self, team_xml, team, boxscore_item):
        if team in ('away', 'home'):
            try:
                team_off_strategy = team_xml.xpath('offStrategy/text()').extract_first()
                team_def_strategy = team_xml.xpath('defStrategy/text()').extract_first()

                boxscore_item[team + '_off_strategy'] = team_off_strategy
                boxscore_item[team + '_def_strategy'] = team_def_strategy
                return boxscore_item
            except AttributeError as e:
                logging.error('Only accepting scrapy.selector.Selector type')
                print(traceback.print_tb(e.__traceback__))
        else:
            print('Invalid team')

    # Gets focus and pace preps set by the (away or home) team
    def get_preps(self, team_xml, team, boxscore_item):
        if team in ('away', 'home'):
            try:
                team_prep_focus = team_xml.xpath('gdp/focus/text()').extract_first()
                team_prep_focus = team_prep_focus.split('.')
                team_prep_pace = team_xml.xpath('gdp/pace/text()').extract_first()
                team_prep_pace = team_prep_pace.split('.')

                if team_prep_focus[0] != 'N/A':
                    boxscore_item[team + '_prep_focus'] = team_prep_focus[0]
                    boxscore_item[team + '_prep_focus_matched'] = team_prep_focus[1]
                else:
                    boxscore_item[team + '_prep_focus'] = None
                    boxscore_item[team + '_prep_focus_matched'] = None

                if team_prep_pace[0] != 'N/A':
                    boxscore_item[team + '_prep_pace'] = team_prep_pace[0]
                    boxscore_item[team + '_prep_pace_matched'] = team_prep_pace[1]
                else:
                    boxscore_item[team + '_prep_pace'] = None
                    boxscore_item[team + '_prep_pace_matched'] = None
                return boxscore_item
            except AttributeError as e:
                logging.error('Only accepting scrapy.selector.Selector type')
                print(traceback.print_tb(e.__traceback__))
        else:
            print('Invalid team')
