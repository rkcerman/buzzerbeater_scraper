from bbstats.models import Countries

import scrapy
import urllib.parse
from buzzerbeater_scraper.formdata import BB_API_LOGIN
from buzzerbeater_scraper.items import LeagueItem


class LeaguesSpider(scrapy.Spider):
    name = "leagues_spider"
    allowed_domains = ["buzzerbeater.com"]
    base_url = 'http://bbapi.buzzerbeater.com'
    base_login_url = base_url + '/login.aspx'
    base_leagues_url = base_url + '/leagues.aspx'
    start_urls = (
        base_login_url,
    )
    league_urls = []

    # Queries the DB for available countries, and generates list of
    # league URLs to scrape using country_id and no. of divisions
    # in the particular country.
    def __init__(self, **kwargs):
        # Makes sure we only query the active ones
        countries = Countries.objects.exclude(divisions=None)
        for country in countries:
            for division in range(1, country.divisions + 1):
                args = {
                    'countryId': country.id,
                    'level': division
                }
                self.league_urls.append(
                    self.base_leagues_url + '?{}'.format(
                        urllib.parse.urlencode(args)
                    )
                )
        super().__init__(**kwargs)

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
        self.logger.debug(str(self.league_urls))

        for url in self.league_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse_leagues,
            )

    def parse_leagues(self, response):
        division_xml = response.xpath('//bbapi/division')
        country_id = division_xml.xpath('@countryid').extract_first()
        level = division_xml.xpath('@level').extract_first()

        for division in division_xml.xpath('league'):
            league_id = int(division.xpath('@id').extract_first())
            name = division.xpath('text()').extract_first()

            league_item = LeagueItem(
                id=league_id,
                name=name,
                country_id=country_id,
                level=level
            )

            yield league_item

