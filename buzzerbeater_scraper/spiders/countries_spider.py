import scrapy
import urllib.parse
from buzzerbeater_scraper.formdata import BB_API_LOGIN
from buzzerbeater_scraper.items import CountryItem


class CountriesSpider(scrapy.Spider):
    name = "countries_spider"
    allowed_domains = ["buzzerbeater.com"]
    base_url = 'http://bbapi.buzzerbeater.com'
    base_login_url = base_url + '/login.aspx'
    base_countries_url = base_url + '/countries.aspx'
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
            url=self.base_countries_url,
            callback=self.parse_countries,
        )

    def parse_countries(self, response):
        countries_xml = response.xpath('//bbapi/countries')

        for country in countries_xml.xpath('country'):
            country_id = int(country.xpath('@id').extract_first())
            try:
                divisions = int(country.xpath('@divisions').extract_first())
            except ValueError:
                divisions = None
            first_season = int(country.xpath('@firstSeason').extract_first())
            name = country.xpath('text()').extract_first()

            country_item = CountryItem(
                id=country_id,
                divisions=divisions,
                first_season=first_season,
                name=name
            )

            yield country_item
