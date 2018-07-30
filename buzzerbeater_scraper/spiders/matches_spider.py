# -*- coding: utf-8 -*-
import scrapy
import re

from twisted.internet import reactor
from datetime import datetime
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

from buzzerbeater_scraper import pbp_parser
from buzzerbeater_scraper import boxscore_parser

from buzzerbeater_scraper.pbp_tags import PLAY_TYPE_CATEGORIES
from buzzerbeater_scraper.items import PlayByPlayItem, TeamItem, MatchItem
from buzzerbeater_scraper.pbp_parser import PlayByPlayParser
from buzzerbeater_scraper.formdata import BB_LOGIN
from buzzerbeater_scraper.boxscore_parser import BoxscoreParser
from buzzerbeater_scraper.spiders import player_spider


class BuzzerbeaterMatchesSpider(scrapy.Spider):

    name = "matches_spider"
    allowed_domains = ["buzzerbeater.com"]
    start_urls = (
        'http://www.buzzerbeater.com/default.aspx',
    )
    urls = [
        'http://www.buzzerbeater.com/team/58420/schedule.aspx?season=42'
    ]
    parse_players = False
    parse_pbps = True

    def __init__(self, team_id, season='', parse_players=False, parse_pbps=True, **kwargs):
        if season != '':
            season = season.split(',')
        if team_id is not None:
            team_id = team_id.split(',')
            print(team_id)
            self.urls = []

            for team in team_id:
                url = 'http://www.buzzerbeater.com/team/' + team + '/schedule.aspx'
                print(url)
                if season:
                    for s in season:
                        self.urls.append(url + '?season=' + s)
                else:
                    self.urls.append(url)
        self.parse_players = parse_players
        self.parse_pbps = parse_pbps
        print(self.urls)
        print(self.parse_players)
        print(self.parse_pbps)
        self.logger.info(self.urls)
        super().__init__(**kwargs)  # python3

    def parse(self, response):
        # Opening a login request
        return scrapy.FormRequest.from_response(
            response,
            formdata=BB_LOGIN,
            callback=self.after_login
        )

    def after_login(self, response):
        # Check login succeed before going on
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.h1.get_text()
        print(title)
        if title != "Welcome to BuzzerBeater!":
            self.logger.error("Login failed")
        else:
            self.logger.info("Login successful")
            yield scrapy.Request(
                url='http://bbapi.buzzerbeater.com/login.aspx?login=rkcerman&code=konzola2',
                callback=self.after_api_login
            )

    # After API login method that calls the boxscore API link before parsing it
    def after_api_login(self, response):
        for url in self.urls:
            self.logger.info(["URL", url])
            yield scrapy.Request(url, callback=self.parse_schedule)

    # TODO better to move this into boxscore_parser
    # Parses the Schedule page
    def parse_schedule(self, response):
        season = response.xpath('//option[@selected="selected"]/@value').extract_first()

        # Iterating through each row
        for row in response.xpath('//table[@class="schedule"]/tr'):
            boxscore_link = row.xpath('td[4]/a[@id="matchBoxscoreLink"]/@href').extract_first()
            away_team_name = row.xpath('td[3]//a/text()').extract_first()
            home_team_name = row.xpath('td[6]//a/text()').extract_first()

            # To prevent table headers and all star games from getting scraped
            if boxscore_link and away_team_name and home_team_name is not None:
                match_date = row.xpath('td[1]//text()').extract_first().split()[0]
                match_date = datetime.strptime(match_date, '%m/%d/%Y')

                # Creating the Away Team item
                away_team_id = row.xpath('td[3]//a/@href').extract_first().replace("/team/", "")
                away_team_id = away_team_id.replace("/overview.aspx", "")
                away_team_item = TeamItem(
                    id=away_team_id,
                    name=away_team_name
                )

                yield away_team_item

                # Creating the Home Team item
                home_team_id = row.xpath('td[6]//a/@href').extract_first().replace("/team/", "")
                home_team_id = home_team_id.replace("/overview.aspx", "")
                home_team_item = TeamItem(
                    id=home_team_id,
                    name=home_team_name
                )

                yield home_team_item

                # Extracting the Match ID
                match_id = boxscore_link.replace("/match/", "").replace("/boxscore.aspx", "")

                match_item = MatchItem(
                    id=match_id,
                    match_date=match_date,
                    away_team_id=away_team_id,
                    home_team_id=home_team_id,
                    season=season
                )
                yield match_item

                boxscore_api_link = 'http://bbapi.buzzerbeater.com/boxscore.aspx?matchid=' + match_id

                # Login to API before scraping box scores
                meta={'match_id': match_id, 'boxscore_api_link': boxscore_api_link}
                yield response.follow(
                    url=boxscore_api_link,
                    callback=self.parse_boxscore,
                    meta={'match_id': match_id}
                )

    # TODO parse the actual box score
    # Parses the Boxscore page
    def parse_boxscore(self, response):
        boxscore_xml = response.xpath('//bbapi/match')
        match_id = response.meta['match_id']

        bs_all_items = BoxscoreParser.parse(
            self=BoxscoreParser,
            boxscore_xml=boxscore_xml
        )

        score_table_items = bs_all_items[0]
        boxscore_item = bs_all_items[1]
        boxscore_stats_items = bs_all_items[2]
        team_items = bs_all_items[3]

        for team_item in team_items:
            yield team_item

        for score_table_item in score_table_items:
            yield score_table_items[score_table_item]

        yield boxscore_item

        for boxscore_stats_item in boxscore_stats_items:

            if self.parse_players:
                player_id = boxscore_stats_item['player_id']
                url = 'http://www.buzzerbeater.com/player/' + str(player_id) + '/overview.aspx'
                yield response.follow(url, self.parse_player)

            yield boxscore_stats_item

        # Following the link to Play-By-Play page
        pbp_link = 'http://www.buzzerbeater.com/match/' + match_id + '/pbp.aspx'

        if self.parse_pbps is True:
            yield response.follow(pbp_link, self.parse_pbp)

    # TODO Try to find a way to use scrapy's native parsing here
    # Parses the Play-by-Play page
    def parse_pbp(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        # Selecting the Play-by-play table
        play_by_play = soup.find(id='ctl00_cphContent_text').table

        # Extracting the Match ID
        match_id = soup.find(id='aspnetForm')['action']
        match_id = match_id.replace("/match/", "")
        match_id = match_id.replace("/pbp.aspx", "")

        # Iterating through the Play-by-play table
        i = 1
        while i < len(play_by_play.find_all('tr')):
            row = play_by_play.select('tr')[i]
            item_match_id = int(match_id)
            item_event_type = row['class'][0]
            item_quarter = row.select('td')[0].get_text()
            item_clock = row.select('td')[1].get_text()
            item_score = row.select('td')[2].get_text()
            item_event = row.select('td')[3]

            # Replacing Player names for IDs; makes jobs down the line easier
            for idx, href in enumerate(item_event.find_all('a')):
                player_href_id = href.get('href')
                player_href_id = re.search(
                    '/player\/(\d+)\/overview.aspx',
                    player_href_id
                ).group(1)
                item_event.select('a')[idx].string = player_href_id

            # Adding custom play_type_categories to the plays
            play_tags = PLAY_TYPE_CATEGORIES.get(item_event_type)
            print("Play tags", play_tags)

            # Creating an Item to insert into the DB
            pbp_item = PlayByPlayItem(
                id=int(str(match_id) + str(i)),
                match_id=item_match_id,
                event_type=item_event_type,
                quarter=int(item_quarter),
                clock=item_clock,
                score=item_score,
                event=item_event.get_text(),
                play_tags=play_tags
            )

            yield pbp_item

            # Check if the item can be processed further, e.g. in case of shot items
            parsed_pbp_item = pbp_parser.PlayByPlayParser.parse(
                self=PlayByPlayParser,
                pbp_item=pbp_item
            )
            if parsed_pbp_item is not None:
                yield parsed_pbp_item

            i += 1

    # Parses individual player overviews
    def parse_player(self, response):
        player = player_spider.PlayerSpider.parse_player_html(response=response)

        if player is not None:
            player_item = player['player_item']
            team_item = player['team_item']

            yield team_item
            yield player_item

            # TODO ugly AF
            try:
                for skill in player['player_skills_items']:
                    yield skill
            except KeyError:
                print('No player skills available for ', player_item.id)

            player_history_link = player['player_history_link']
            yield response.follow(player_history_link, self.parse_player_history)

    # Parses the player history page
    def parse_player_history(self, response):
        player_history_items = player_spider.PlayerSpider.parse_player_history_html(response=response)

        for item in player_history_items:
            yield item
