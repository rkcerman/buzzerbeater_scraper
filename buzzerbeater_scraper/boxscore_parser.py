import re

from scrapy.selector import Selector, SelectorList
from buzzerbeater_scraper.items import ScoreTableItem, BoxscoreItem

class BoxscoreParser:

    def parse(self, boxscore_xml):
        match_id = int(boxscore_xml.xpath('//match/@id').extract_first())
        score_table_items = self.get_scores_by_qtr(
            self=self,
            boxscore_xml=boxscore_xml,
            match_id=match_id)
        away_team_xml = boxscore_xml.xpath('//match/awayteam')
        home_team_xml = boxscore_xml.xpath('//match/hometeam')
        boxscore_item = BoxscoreItem(match_id=match_id)

        for i, team_xml in enumerate([away_team_xml, home_team_xml]):
            if i == 0:
                team = 'away'
            else:
                team = 'home'

            print()

    # Parses the final score table
    # Returns the list of ScoreTableItem
    def get_scores_by_qtr(self, boxscore_xml, match_id):
        try:
            away_team_scores = boxscore_xml.xpath('//match/awayteam/score/@partials').extract_first().split(',')
            home_team_scores = boxscore_xml.xpath('//match/hometeam/score/@partials').extract_first().split(',')
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
            print('ERROR: Only accepting scrapy.selector.Selector type')
            print(e)

    def get_strategies(self, team_xml, team, boxscore_item):
        if team in ('away', 'home'):
            try:
                team_off_strategy = team_xml.xpath('offstrategy/text()').extract_first()
                team_def_strategy = team_xml.xpath('defstrategy/text()').extract_first()

                print('off_strategy: ', team_off_strategy)

                boxscore_item[team + '_off_strategy'] = team_off_strategy
                boxscore_item[team + '_def_strategy'] = team_def_strategy
                return boxscore_item
            except AttributeError as e:
                print('ERROR: Only accepting scrapy.selector.Selector type')
                print(e)
        else:
            print('Invalid team')
