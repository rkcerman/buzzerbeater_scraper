import datetime

import scrapy
import urllib.parse
from buzzerbeater_scraper.formdata import BB_API_LOGIN
from buzzerbeater_scraper.items import SeasonItem


class SeasonsSpider(scrapy.Spider):
    name = "seasons_spider"
    allowed_domains = ["buzzerbeater.com"]
    base_url = 'http://bbapi.buzzerbeater.com'
    base_login_url = base_url + '/login.aspx'
    base_seasons_url = base_url + '/seasons.aspx'
    start_urls = (
        base_login_url,
    )

    def parse(self, response):
        api_url = self.base_login_url + '?{}'.format(
            urllib.parse.urlencode(BB_API_LOGIN)
        )
        # Opening a login request
        return scrapy.Request(
            url=api_url,
            callback=self.after_login
        )

    def after_login(self, response):
        self.logger.debug('Logged in.')
        yield scrapy.Request(
            url=self.base_seasons_url,
            callback=self.parse_seasons,
        )

    def parse_seasons(self, response):
        seasons_xml = response.xpath('//bbapi/seasons')

        for season in seasons_xml.xpath('season'):
            season_id = int(season.xpath('@id').extract_first())
            start_date = season.xpath('start/text()').extract_first()
            start_date = datetime.datetime.strptime(
                start_date,
                '%Y-%m-%dT%H:%M:%SZ'
            )

            end_date = season.xpath('finish/text()').extract_first()

            try:
                end_date = datetime.datetime.strptime(
                    end_date,
                    '%Y-%m-%dT%H:%M:%SZ'
                )
            except TypeError:
                end_date = None

            season_item = SeasonItem(
                season_id=season_id,
                start_date=start_date,
                end_date=end_date
            )

            yield season_item
