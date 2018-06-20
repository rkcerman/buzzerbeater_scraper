# -*- coding: utf-8 -*-
import scrapy
import psycopg2
from bs4 import BeautifulSoup

from buzzerbeater_scraper.items import PlayByPlayItem


class BuzzerbeaterSpider(scrapy.Spider):

    name = "buzzerbeater"
    allowed_domains = ["buzzerbeater.com"]
    start_urls = (
        'http://www.buzzerbeater.com/default.aspx',
    )
    urls = [
        'http://www.buzzerbeater.com/match/101245701/pbp.aspx',
        'http://www.buzzerbeater.com/match/101245693/pbp.aspx'
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
                print("URL", url)
                yield scrapy.Request(url, callback=self.parse_pbp)

    # Parses the Play-by-Play page
    def parse_pbp(self, response):
        print("URL", response.url)
        soup = BeautifulSoup(response.text, 'lxml')

        # Selecting the Play-by-play table
        play_by_play = soup.find(id='ctl00_cphContent_text').table

        # Selecting the match ID
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

