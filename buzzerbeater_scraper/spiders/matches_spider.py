# -*- coding: utf-8 -*-
import logging
import datetime
import logging
import urllib.parse
from collections import Counter

import scrapy
import re

from bs4 import BeautifulSoup
from django.db.models import Q

from buzzerbeater_scraper import pbp_parser

from buzzerbeater_scraper.pbp_tags import PLAY_TYPE_CATEGORIES
from buzzerbeater_scraper.items import PlayByPlayItem, TeamItem, MatchItem
from buzzerbeater_scraper.pbp_parser import PlayByPlayParser
from buzzerbeater_scraper.formdata import BB_LOGIN, BB_API_LOGIN
from buzzerbeater_scraper.boxscore_parser import BoxscoreParser
from buzzerbeater_scraper.spiders.player_spider import PlayerSpider

from bbstats.models import Boxscores, SeasonsLeaguesTeams


# Generates a list of dictionaries containing
# all combinations of team IDs and seasons to scrape
def get_teams_seasons(team_ids, seasons):
    teams_seasons = []
    for team_id in team_ids:
        for season in seasons:
            args = {
                'teamid': team_id,
                'season': season,
            }
            teams_seasons.append(args)
    return teams_seasons


# Pulls out list of teams for a league/season combination
def get_standings(league_ids, seasons):
    standings = SeasonsLeaguesTeams.objects.filter(
        season__in=seasons,
        league__in=league_ids,
    )
    team_ids = [team['team_id'] for team in
                standings.values('team_id')]
    return team_ids


# Pulls out already scraped matches from the DB into a list
def get_scraped_matches(team_ids, seasons):
    schedule = Boxscores.objects.filter(match__season__in=seasons) \
        .filter(Q(match__away_team_id__in=team_ids)
                | Q(match__home_team_id__in=team_ids))
    matches_ids = [match['match_id'] for match in
                   schedule.values('match_id')]
    return matches_ids


class BuzzerbeaterMatchesSpider(scrapy.Spider):
    logger = logging.getLogger(__name__)

    name = "matches_spider"
    allowed_domains = ["buzzerbeater.com"]
    start_urls = (
        'http://www.buzzerbeater.com/default.aspx',
    )
    base_url = 'http://bbapi.buzzerbeater.com'
    base_login_url = base_url + '/login.aspx'
    base_schedule_url = base_url + '/schedule.aspx'
    base_boxscore_url = base_url + '/boxscore.aspx'
    API_URL = base_login_url + '?{}'.format(
        urllib.parse.urlencode(BB_API_LOGIN)
    )

    matches_pbp_counter = {}

    # __init__ function to handle custom args
    # team_ids - IDs of teams to scrape their schedule
    # seasons - for which seasons the schedule should be scraped
    # parse_players - if true, scrapes each player's overview page
    # parse_pbps - if true, scrapes every match's play by play
    # force_rescrape - if true, rescrapes already scraped matches
    def __init__(self,
                 team_ids='58420',
                 league_ids='2274',
                 seasons='44',
                 parse_players=True,
                 parse_pbps=True,
                 force_rescrape=False,
                 **kwargs):

        team_ids = team_ids.split(',')
        league_ids = league_ids.split(',')
        seasons = seasons.split(',')

        # Adds team_ids from leagues if supplied
        team_ids += get_standings(league_ids, seasons)

        if not force_rescrape:
            self.scraped_boxscores = get_scraped_matches(team_ids, seasons)
        else:
            self.scraped_boxscores = []
        self.teams_seasons = get_teams_seasons(
            team_ids=team_ids,
            seasons=seasons
        )
        self.parse_players = parse_players
        self.parse_pbps = parse_pbps
        super().__init__(**kwargs)

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
        if title != 'Welcome to BuzzerBeater!':
            self.logger.error('Login failed')
        else:
            self.logger.info('Login successful')
            self.logger.info('Parse Players: '
                             + str(self.parse_players)
                             )
            self.logger.info('Parse Play-by-plays: '
                             + str(self.parse_pbps)
                             )
            self.logger.info('Already scraped boxscores: '
                             + str(self.scraped_boxscores)
                             )
            yield scrapy.Request(
                url=self.API_URL,
                callback=self.after_api_login
            )

    # After API login method that calls the boxscore API link before
    # parsing it
    def after_api_login(self, response):
        for team_season in self.teams_seasons:
            args = {
                'teamid': team_season['teamid'],
                'season': team_season['season'],
            }
            url = self.base_schedule_url + '?{}'.format(
                urllib.parse.urlencode(args)
            )

            self.logger.info("Current URL: {}".format(url))
            yield scrapy.Request(
                url=url,
                callback=self.parse_schedule,
                meta=args,
            )

    # Parses the schedule from the API response
    def parse_schedule(self, response):
        schedule_xml = response.xpath('//bbapi/schedule')
        season = response.meta['season']

        for match in schedule_xml.xpath('match'):
            match_id = int(match.xpath('@id').extract_first())
            match_type = match.xpath('@type').extract_first()

            # Further scrape matches only if they haven't been scraped yet
            # Also excludes matches of type 'unknown' which are all-star
            if match_id not in self.scraped_boxscores and match_type != 'unknown':
                match_date = match.xpath('@start').extract_first()
                match_date = datetime.datetime.strptime(
                    match_date,
                    '%Y-%m-%dT%H:%M:%SZ'
                )

                # Gathering data for away and home teams and yielding it
                away_team_id = match.xpath('awayTeam/@id').extract_first()
                away_team_name = match.xpath(
                    'awayTeam/teamName/text()').extract_first()
                away_team_item = TeamItem(
                    id=away_team_id,
                    name=away_team_name
                )
                home_team_id = match.xpath('homeTeam/@id').extract_first()
                home_team_name = match.xpath(
                    'homeTeam/teamName/text()').extract_first()
                home_team_item = TeamItem(
                    id=home_team_id,
                    name=home_team_name
                )
                match_item = MatchItem(
                    id=match_id,
                    match_date=match_date,
                    away_team_id=away_team_id,
                    home_team_id=home_team_id,
                    season=season
                )

                yield away_team_item
                yield home_team_item
                yield match_item

                # Prevent requesting not-yet-existing boxscore pages
                if datetime.datetime.now() > match_date:
                    boxscore_api_link = self.base_boxscore_url \
                                        + '?matchid=' \
                                        + str(match_id)

                    yield response.follow(
                        url=boxscore_api_link,
                        callback=self.parse_boxscore,
                        meta={'match_id': match_id}
                    )
            else:
                self.logger.info('Match id already in the DB: '
                                 + str(match_id))

    # Parses the Boxscore page
    def parse_boxscore(self, response):
        boxscore_xml = response.xpath('//bbapi/match')
        match_id = response.meta['match_id']

        try:
            bs_all_items = BoxscoreParser.parse(
                self=BoxscoreParser,
                boxscore_xml=boxscore_xml
            )
        except TypeError:
            self.logger.error('Re-login for match ' + str(match_id))
            scrapy.Request(
                url=self.API_URL
            )
            yield response.follow(
                url=response.url,
                callback=self.parse_boxscore,
                meta={'match_id': match_id}
            )
        else:
            score_table_items = bs_all_items[0]
            boxscore_item = bs_all_items[1]
            boxscore_stats_items = bs_all_items[2]
            team_items = bs_all_items[3]

            for team_item in team_items:
                yield team_item

            for score_table_item in score_table_items:
                yield score_table_items[score_table_item]

            yield boxscore_item

            for boxscore_stats_item in boxscore_stats_items:

                if self.parse_players:
                    player_id = boxscore_stats_item['player_id']
                    url = 'http://www.buzzerbeater.com/player/' \
                          + str(player_id) \
                          + '/overview.aspx'
                    yield response.follow(
                        url=url,
                        callback=self.parse_player
                    )

                yield boxscore_stats_item

            # Following the link to Play-By-Play page
            if self.parse_pbps:
                pbp_link = 'http://www.buzzerbeater.com/match/' \
                           + str(match_id) \
                           + '/pbp.aspx'

                yield response.follow(
                    url=pbp_link,
                    callback=self.parse_pbp
                )

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

        self.logger.info('Parsing match id: ' + str(match_id))

        # Iterating through the Play-by-play table
        i = 1
        len_play_by_plays = len(play_by_play.find_all('tr'))
        self.logger.info(str(match_id)
                         + ' -- Total number of plays: '
                         + str(len_play_by_plays))
        self.matches_pbp_counter[match_id] = Counter(
            total_pbps=len_play_by_plays,
            scraped_pbps=1,
            scraped_shots=1,
        )
        while i < len_play_by_plays:
            self.logger.debug(str(match_id)
                              + ' --- play no. '
                              + str(i))
            row = play_by_play.select('tr')[i]
            self.logger.debug(row)
            item_match_id = int(match_id)
            item_event_type = row['class'][0]
            item_quarter = row.select('td')[0].get_text()
            item_clock = row.select('td')[1].get_text()
            item_score = row.select('td')[2].get_text()
            item_event = row.select('td')[3]

            # Replacing Player names for IDs
            # Makes jobs down the line easier
            for idx, href in enumerate(item_event.find_all('a')):
                player_href_id = href.get('href')
                player_href_id = re.search(
                    '/player\/(\d+)\/overview.aspx',
                    player_href_id
                ).group(1)
                item_event.select('a')[idx].string = player_href_id

            # Adding custom play_type_categories to the plays
            # If doesn't exist, use default 'info'
            play_tags = ['info']
            try:
                play_tags = PLAY_TYPE_CATEGORIES[item_event_type]
            except KeyError:
                self.logger.error('Unknown play tag ' + item_event_type)

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

            # Check if the item can be processed further
            # E.g. in case of shot items
            parsed_pbp_item = pbp_parser.PlayByPlayParser.parse(
                self=PlayByPlayParser,
                pbp_item=pbp_item
            )
            if parsed_pbp_item is not None:
                yield parsed_pbp_item
                self.matches_pbp_counter[match_id]['scraped_shots'] += 1

            self.matches_pbp_counter[match_id]['scraped_pbps'] += 1
            i += 1

    # Parses individual player overviews
    def parse_player(self, response):
        player = PlayerSpider.parse_player_html(
            response=response
        )

        if player is not None:
            player_item = player['player_item']
            team_item = player['team_item']
            skill_item = player['player_skills_item']

            self.logger.info('Team: '
                             + team_item['id']
                             + ' Player: '
                             + player_item['id'])

            yield team_item
            yield player_item
            yield skill_item

            player_history_link = player['player_history_link']
            yield response.follow(
                url=player_history_link,
                callback=self.parse_player_history
            )

    # Parses the player history page
    def parse_player_history(self, response):
        player_history_items = PlayerSpider.parse_player_history_html(
            response=response
        )

        for item in player_history_items:
            yield item

    def closed(self, reason):
        self.logger.info(reason)
        for k, v in self.matches_pbp_counter.items():
            self.logger.info(('%s %s', str(k), str(v)))
            if v['total_pbps'] != v['scraped_pbps']:
                self.logger.error('Scraped PBPs lower than total.')
