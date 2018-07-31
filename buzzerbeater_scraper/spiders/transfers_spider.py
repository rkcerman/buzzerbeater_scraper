import scrapy
import re
from datetime import datetime
from bs4 import BeautifulSoup
from scrapy import FormRequest

import buzzerbeater_scraper.spiders.player_spider as player_spider
from buzzerbeater_scraper.items import PlayerItem, PlayerSkillsItem, TeamItem, PlayerHistoryItem
from buzzerbeater_scraper.formdata import BB_LOGIN, BB_TRANSFER_SEARCH_FORMDATA, BB_TRANSFER_NEXT_PAGE_FORMDATA


class BuzzerbeaterTransfersSpider(scrapy.Spider):
    transfer_list_page = 0
    name = "transfers_spider"
    allowed_domains = ["buzzerbeater.com"]
    start_urls = (
        'http://www.buzzerbeater.com/default.aspx',
    )
    urls = [
        'http://www.buzzerbeater.com/manage/transferlist.aspx',
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
        title = response.xpath('//h1/text()').extract_first()
        print(title)
        if title != "Welcome to BuzzerBeater!":
            self.logger.error("Login failed")
        else:
            self.logger.info("Login successful")
            for url in self.urls:
                self.logger.info(["URL", url])
                yield scrapy.Request(url, callback=self.parse_transfer_search)

    # Sends a transfer search request to obtain the players on the market
    def parse_transfer_search(self, response):
        formdata = self.search_page_formdata(response=response)

        yield FormRequest(url=self.urls[0], callback=self.parse_transfers, formdata=formdata)

    # Parses the search results and follows the links to the individual player overviews
    def parse_transfers(self, response):
        self.transfer_list_page += 1
        self.logger.info(msg=("Transfer list page: ", self.transfer_list_page))

        formdata = self.next_page_formdata(response=response)
        for row in response.xpath('//div[@id="playerbox"]'):
            player_link = row.xpath('div[@class="boxheader"]/a/@href').extract_first()

            yield response.follow(player_link, self.parse_player)

        # If the 'next page' button is not present, it's the last page and stop
        if response.xpath('//input[@name="ctl00$cphContent$btnNextPage"]/@value').extract_first() is not None:
            self.logger.info(msg="Next Page button present")
            yield FormRequest(url=self.urls[0], formdata=formdata, callback=self.parse_transfers)

    # Parses individual player overviews
    def parse_player(self, response):
        player = player_spider.PlayerSpider.parse_player_html(response=response)

        if player is not None:
            player_item = player['player_item']
            team_item = player['team_item']
            game_shape_item = player['game_shape_item']

            yield team_item
            yield player_item
            yield game_shape_item

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

    # Creates a form data payload to send, simulating the search button
    def search_page_formdata(self, response):
        viewstate = response.xpath('//input[@name="__VIEWSTATE"]/@value').extract_first()
        eventvalidation = response.xpath('//input[@name="__EVENTVALIDATION"]/@value').extract_first()

        formdata = BB_TRANSFER_SEARCH_FORMDATA
        formdata['__EVENTVALIDATION'] = eventvalidation
        formdata['__VIEWSTATE'] = viewstate

        return formdata

    # Creates a form data payload to send, simulating the next page button
    def next_page_formdata(self, response):
        viewstate = response.xpath('//input[@name="__VIEWSTATE"]/@value').extract_first()
        eventvalidation = response.xpath('//input[@name="__EVENTVALIDATION"]/@value').extract_first()
        previouspage = response.xpath('//input[@name="__PREVIOUSPAGE"]/@value').extract_first()
        page = response.xpath('//input[@name="ctl00$cphContent$hdnPage"]/@value').extract_first()
        search_id = response.xpath('//input[@name="ctl00$cphContent$hdnSearchID"]/@value').extract_first()
        search_date = response.xpath('//input[@name="ctl00$cphContent$hdnSearchDate"]/@value').extract_first()

        formdata = BB_TRANSFER_NEXT_PAGE_FORMDATA
        formdata['__PREVIOUSPAGE'] = previouspage
        formdata['__EVENTVALIDATION'] = eventvalidation
        formdata['__VIEWSTATE'] = viewstate
        formdata['ctl00$cphContent$hdnPage'] = page
        formdata['ctl00$cphContent$hdnSearchID'] = search_id
        formdata['ctl00$cphContent$hdnSearchDate'] = search_date

        return formdata
