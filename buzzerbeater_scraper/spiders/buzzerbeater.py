# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime
from dateutil.parser import parse
from bs4 import BeautifulSoup

from buzzerbeater_scraper.items import PlayByPlayItem, TeamItem, MatchItem


class BuzzerbeaterSpider(scrapy.Spider):

    name = "buzzerbeater"
    allowed_domains = ["buzzerbeater.com"]
    start_urls = (
        'http://www.buzzerbeater.com/default.aspx',
    )
    urls = [
        'http://www.buzzerbeater.com/team/58420/schedule.aspx'
    #    'http://www.buzzerbeater.com/match/101245701/pbp.aspx',
    #    'http://www.buzzerbeater.com/match/101245693/pbp.aspx'
    ]

    def parse(self, response):
        # Opening a login request
        return scrapy.FormRequest.from_response(
            response,
            formdata={'ctl00$txtLoginName': 'rkcerman', 'ctl00$txtPassword': 'konzola'},
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
        # Iterating through each row
        for idx, row in enumerate(response.xpath('//table[@class="schedule"]/tr')):
            print(idx)
            if idx != 0:
                match_date = row.xpath('td[1]//text()').extract_first().split()[0]
                match_date = datetime.strptime(match_date, '%m/%d/%Y')
                print("date : ", match_date)

                # Creating the Away Team item
                try:
                    away_team_name = row.xpath('td[3]/a/text()').extract_first()
                    away_team_id = row.xpath('td[3]/a').css('::attr(href)').extract_first().replace("/team/", "")
                except AttributeError as e:
                    print("Buy ETH <3")
                    away_team_name = row.xpath('td[3]/strong/a/text()').extract_first()
                    away_team_id = row.xpath('td[3]/strong/a').css('::attr(href)').extract_first().replace("/team/", "")
                print("Away team: ", away_team_name)
                away_team_id = away_team_id.replace("/overview.aspx", "")
                away_team_item = TeamItem(id=away_team_id, name=away_team_name)

                yield away_team_item
                print(away_team_item)

                # Creating the Home Team item
                try:
                    home_team_name = row.xpath('td[6]/a/text()').extract_first()
                    home_team_id = row.xpath('td[6]/a').css('::attr(href)').extract_first().replace("/team/", "")
                except AttributeError as e:
                    print("Buy ETH <3")
                    home_team_name = row.xpath('td[6]/strong/a/text()').extract_first()
                    home_team_id = row.xpath('td[6]/strong/a').css('::attr(href)').extract_first().replace("/team/", "")
                home_team_id = home_team_id.replace("/overview.aspx", "")
                home_team_item = TeamItem(id=home_team_id, name=home_team_name)

                yield home_team_item

                box_score_link = row.xpath('td[4]/a[@id="matchBoxscoreLink"]').css('::attr(href)')

                # Extracting the Match ID
                match_id = box_score_link.extract_first().replace("/match/", "").replace("/boxscore.aspx", "")

                match_item = MatchItem(id=match_id, match_date=match_date,
                                       away_team_id=away_team_id, home_team_id=home_team_id)
                yield match_item

                print("href: ", box_score_link.extract())
                yield response.follow(box_score_link.extract_first(), self.parse_boxscore)

    # TODO parse the actual box score
    # Parses the Boxscore page
    def parse_boxscore(self, response):
        for href in response.xpath('//a[@title="Play-By-Play"]').css('::attr(href)'):
            print(href)
            yield response.follow(href, self.parse_pbp)

    # TODO Try to find a way to use scrapy's native parsing here
    # Parses the Play-by-Play page
    def parse_pbp(self, response):
        print("URL", response.url)
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
            item_event = row.select('td')[3].get_text()

            # Creating an Item to insert into the DB
            playByPlayItem = PlayByPlayItem(id=int(str(match_id) + str(i)), match_id=item_match_id, event_type=item_event_type,
                                            quarter=int(item_quarter), clock=item_clock, score=item_score, event=item_event)
            yield playByPlayItem
            i += 1

