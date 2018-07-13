# -*- coding: utf-8 -*-
import scrapy
import re
from datetime import datetime
from bs4 import BeautifulSoup

from buzzerbeater_scraper import pbp_parser
from buzzerbeater_scraper.pbp_tags import PLAY_TYPE_CATEGORIES
from buzzerbeater_scraper.items import PlayByPlayItem, TeamItem, MatchItem
from buzzerbeater_scraper.pbp_parser import PlayByPlayParser
from buzzerbeater_scraper.formdata import BB_LOGIN


class BuzzerbeaterMatchesSpider(scrapy.Spider):

    name = "matches_spider"
    allowed_domains = ["buzzerbeater.com"]
    start_urls = (
        'http://www.buzzerbeater.com/default.aspx',
    )
    urls = [
        'http://www.buzzerbeater.com/team/58420/schedule.aspx'
    ]

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
            for url in self.urls:
                self.logger.info(["URL", url])
                yield scrapy.Request(url, callback=self.parse_schedule)

    # Parses the Schedule page
    def parse_schedule(self, response):
        season = response.xpath('//option[@selected="selected"]/@value').extract_first()

        # Iterating through each row
        for row in response.xpath('//table[@class="schedule"]/tr'):
            box_score_link = row.xpath('td[4]/a[@id="matchBoxscoreLink"]').css('::attr(href)').extract_first()

            if box_score_link is not None:
                match_date = row.xpath('td[1]//text()').extract_first().split()[0]
                match_date = datetime.strptime(match_date, '%m/%d/%Y')
                print("date : ", match_date)

                # TODO Fails at Great/Big 8, also likely a shitty approach (avoid try/except)
                # TODO do it with descendant-or-self
                # Creating the Away Team item
                try:
                    away_team_name = row.xpath('td[3]/a/text()').extract_first()
                    away_team_id = row.xpath('td[3]/a').css('::attr(href)').extract_first().replace("/team/", "")
                except AttributeError:
                    print("Buy ETH <3")
                    away_team_name = row.xpath('td[3]/strong/a/text()').extract_first()
                    away_team_id = row.xpath('td[3]/strong/a').css('::attr(href)').extract_first().replace("/team/", "")
                print("Away team: ", away_team_name)
                away_team_id = away_team_id.replace("/overview.aspx", "")
                away_team_item = TeamItem(
                    id=away_team_id,
                    name=away_team_name
                )

                yield away_team_item
                print(away_team_item)

                # Creating the Home Team item
                try:
                    home_team_name = row.xpath('td[6]/a/text()').extract_first()
                    home_team_id = row.xpath('td[6]/a').css('::attr(href)').extract_first().replace("/team/", "")
                except AttributeError:
                    print("Buy ETH <3")
                    home_team_name = row.xpath('td[6]/strong/a/text()').extract_first()
                    home_team_id = row.xpath('td[6]/strong/a').css('::attr(href)').extract_first().replace("/team/", "")
                home_team_id = home_team_id.replace("/overview.aspx", "")
                home_team_item = TeamItem(
                    id=home_team_id,
                    name=home_team_name
                )

                yield home_team_item

                # Extracting the Match ID
                match_id = box_score_link.replace("/match/", "").replace("/boxscore.aspx", "")

                match_item = MatchItem(
                    id=match_id,
                    match_date=match_date,
                    away_team_id=away_team_id,
                    home_team_id=home_team_id,
                    season=season
                )
                yield match_item

                yield response.follow(box_score_link, self.parse_boxscore)

    # TODO parse the actual box score
    # Parses the Boxscore page
    def parse_boxscore(self, response):
        for href in response.xpath('//a[@title="Play-By-Play"]').css('::attr(href)'):
            yield response.follow(href, self.parse_pbp)

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
                player_href_id = re.search('/player\/(\d+)\/overview.aspx', player_href_id).group(1)
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

            if 'shot' in play_tags:
                shots_item = pbp_parser.PlayByPlayParser.parse(self=PlayByPlayParser, pbp_item=pbp_item)
                yield shots_item

            i += 1

