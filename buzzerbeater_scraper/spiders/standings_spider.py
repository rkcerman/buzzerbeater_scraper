import scrapy
import time
import urllib.parse
from buzzerbeater_scraper.formdata import BB_API_LOGIN
from buzzerbeater_scraper.items import SeasonLeagueTeamItem, TeamItem
from bbstats.models import Leagues, Seasons


# Generates a list of dictionaries containing
# all combinations of league IDs and seasons to scrape
# TODO move to helpers
def get_leagues_seasons(league_ids, seasons):
    leagues_seasons = []
    for league_id in league_ids:
        for season in seasons:
            args = {
                'leagueid': league_id,
                'season': season,
            }
            leagues_seasons.append(args)
    return leagues_seasons


class SeasonsSpider(scrapy.Spider):
    name = "standings_spider"
    allowed_domains = ["buzzerbeater.com"]
    base_url = 'http://bbapi.buzzerbeater.com'
    base_login_url = base_url + '/login.aspx'
    base_standings_url = base_url + '/standings.aspx'
    start_urls = (
        base_login_url,
    )
    leagues_seasons = []

    # __init__ function to handle custom args
    # league_ids - IDs of leagues to scrape their standings
    # seasons - for which seasons the standings should be scraped
    # all_leagues - disregards the league_ids param and scrapes every league
    # all_seasons - disregards the seasons param and scrapes every season
    def __init__(self,
                 league_ids='2274',
                 seasons='44',
                 all_leagues=False,
                 all_seasons=False,
                 **kwargs):
        if not all_leagues:
            league_ids = league_ids.split(',')
        else:
            league_ids = Leagues.objects.all().values_list('id', flat=True)
        if not all_seasons:
            seasons = seasons.split(',')
        else:
            seasons = Seasons.objects.all().values_list('id', flat=True)
        self.leagues_seasons = get_leagues_seasons(league_ids, seasons)

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
        print('There are ',
              len(self.leagues_seasons),
              ' unique combinations.')
        # Sleep function gives time to terminate script
        # in case there are too many URLs
        time.sleep(6)
        # Generate a URL for every league_id and season combination
        # And then scrape it
        for league_season in self.leagues_seasons:
            args = {
                'leagueid': league_season['leagueid'],
                'season': league_season['season'],
            }
            url = self.base_standings_url + '?{}'.format(
                urllib.parse.urlencode(args)
            )

            self.logger.debug("Current URL: {}".format(url))

            yield scrapy.Request(
                url=url,
                callback=self.parse_standings,
                meta=args,
            )

    def parse_standings(self, response):
        standings_xml = response.xpath('//bbapi/standings/regularSeason')
        league_id = response.meta['leagueid']
        season = response.meta['season']

        for team in standings_xml.xpath('conference/team'):
            team_id = team.xpath('@id').extract_first()
            team_name = team.xpath('teamName/text()').extract_first()

            team_item = TeamItem(
                id=team_id,
                name=team_name
            )
            season_league_team_item = SeasonLeagueTeamItem(
                season_id=season,
                league_id=league_id,
                team_id=team_id
            )

            # Yield team item FIRST
            yield team_item
            yield season_league_team_item
