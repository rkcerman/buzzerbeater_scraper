# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

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

    def parse_pbp(self, response):
        print("URL", response.url)
        soup = BeautifulSoup(response.text, 'lxml')

        # Selecting the Play-by-play table
        play_by_play = soup.find(id='ctl00_cphContent_text').table

        # Selecting the match ID
        match_id = soup.find(id='aspnetForm')['action']
        match_id = match_id.replace("/match/", "")
        match_id = match_id.replace("/pbp.aspx", "")

        # Preparing a CSV file
        f = open('-'.join([match_id, "match.csv"]), 'w')
        f.write("match_id,qtr,clock,score,event_type,event")

        # Iterating through the Play-by-play table
        i = 1
        while i < len(play_by_play.find_all('tr')):
            row = play_by_play.select('tr')[i]
            event_type = row['class']
            qtr = row.select('td')[0]
            clock = row.select('td')[1]
            score = row.select('td')[2]
            event = row.select('td')[3]
            string = ','.join([match_id, qtr.get_text(), clock.get_text(), score.get_text(), event_type[0], event.get_text()])
            print(string.replace(" , ", ","), file=f)
            i += 1
        f.close()

