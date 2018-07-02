# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from buzzerbeater_scraper.items import OnlinePeopleItem

class BuzzerbeaterMatchesSpider(scrapy.Spider):

    name = "online_people_logger"
    allowed_domains = ["buzzerbeater.com"]
    start_urls = [
    'http://www.buzzerbeater.com/default.aspx',
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

            # Retrieve the value
            value = re.search("(\d+) online at", soup.findAll(language="JavaScript")[10].get_text()).group(1)
            print("Value", value)
            online_people_item = OnlinePeopleItem(value=value)

            yield online_people_item
