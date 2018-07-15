import re

from scrapy.selector import Selector, SelectorList
from buzzerbeater_scraper.items import BoxscoreScoreTableItem

class BoxscoreParser:

    def parse(self, box_score_div):
        print()

    # Parses the final score table
    def get_scores_by_quarter(self, box_score_div, match_id):
        try:
            score_table = box_score_div.xpath('//table[1]')
            away_team = score_table.xpath('tr[2]')
            home_team = score_table.xpath('tr[3]')
            score_table_item = BoxscoreScoreTableItem(match_id=match_id)
            score_table_items = {}

            # Iterates through each score table row to create a list with score table items
            t = 0
            for team in away_team, home_team:
                td_list = team.xpath('td')

                for i, td in enumerate(td_list):
                    if 0 < i < (len(td_list) - 1):
                        score = int(re.search('(\d+)', td.xpath('text()').extract_first()).group(1))

                        # For away_team we put the initial items into the score table items dict first
                        if t == 0:
                            item = score_table_item.copy()
                            item['qtr'] = i
                            item['away_team_score'] = score
                            score_table_items[i] = item
                        else:
                            score_table_items[i]['home_team_score'] = score
                t += 1

            print(score_table_items)
            return score_table_items
        except AttributeError as e:
            print('ERROR: Only accepting scrapy.selector.Selector type')
            print(e)
