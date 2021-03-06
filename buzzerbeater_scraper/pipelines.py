# -*- coding: utf-8 -*-

import buzzerbeater_scraper.config
import psycopg2
from psycopg2 import IntegrityError

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from buzzerbeater_scraper.items import *


class BuzzerbeaterScraperPipeline(object):
    def open_spider(self, spider):
        hostname = buzzerbeater_scraper.config.DATABASE_CONFIG['hostname']
        username = buzzerbeater_scraper.config.DATABASE_CONFIG['username']
        password = buzzerbeater_scraper.config.DATABASE_CONFIG['password']
        database = buzzerbeater_scraper.config.DATABASE_CONFIG['database']
        self.conn = psycopg2.connect(host=hostname, user=username,
                                     password=password, dbname=database)
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    # TODO order alphabetically
    # TODO remove duplicate method calls
    def process_item(self, item, spider):
        if isinstance(item, PlayByPlayItem):
            try:
                self.cur.execute(
                    "INSERT INTO play_by_plays VALUES(%s, %s, %s, %s, %s, %s, %s, %s::play_tags[]) "
                    "ON CONFLICT DO NOTHING",
                    (item['id'],
                     item['event_type'],
                     item['quarter'],
                     item['clock'],
                     item['score'],
                     item['event'],
                     item['match_id'],
                     item['play_tags']))
                self.conn.commit()
            except IntegrityError as e:
                print("Duplicate primary key entry, skipping")
            return item
        if isinstance(item, CountryItem):
            self.cur.execute("INSERT INTO countries (id,"
                             "name,"
                             "divisions,"
                             "first_season) "
                             "VALUES(%s, %s, %s, %s) "
                             "ON CONFLICT DO NOTHING",
                             (item['id'],
                              item['name'],
                              item['divisions'],
                              item['first_season']))
            self.conn.commit()
            return item
        if isinstance(item, LeagueItem):
            self.cur.execute("INSERT INTO leagues (id,"
                             "name,"
                             "country_id,"
                             "level) "
                             "VALUES(%s, %s, %s, %s) "
                             "ON CONFLICT DO NOTHING",
                             (item['id'],
                              item['name'],
                              item['country_id'],
                              item['level']))
            self.conn.commit()
            return item
        if isinstance(item, ShotsItem):
            self.cur.execute(
                "INSERT INTO shots VALUES(%s, %s, %s, %s, %s, %s) "
                "ON CONFLICT DO NOTHING",
                (item['pbp_id'],
                 item['outcome'],
                 item['defender'],
                 item['defense_type'],
                 item['passer'],
                 item['shooter']))
            self.conn.commit()
            return item
        if isinstance(item, MatchItem):
            try:
                self.cur.execute(
                    "INSERT INTO matches VALUES(%s, %s, %s, %s, %s) "
                    "ON CONFLICT DO NOTHING",
                    (item['id'],
                     item['match_date'],
                     item['home_team_id'],
                     item['away_team_id'],
                     item['season']))
                self.conn.commit()
            except IntegrityError as e:
                print("Duplicate primary key entry, skipping")
            return item
        if isinstance(item, ScoreTableItem):
            try:
                self.cur.execute(
                    "INSERT INTO score_tables VALUES(%s, %s, %s, %s) "
                    "ON CONFLICT DO NOTHING",
                    (item['match_id'],
                     item['qtr'],
                     item['away_team_score'],
                     item['home_team_score']))
                self.conn.commit()
            except IntegrityError as e:
                print("Duplicate primary key entry, skipping")
            return item
        if isinstance(item, BoxscoreItem):
            try:
                self.cur.execute("INSERT INTO boxscores VALUES("
                                 "%s, %s, %s, %s, %s, "
                                 "%s, %s, %s, %s, %s, "
                                 "%s, %s, %s, %s, %s, "
                                 "%s, %s, %s, %s, %s, "
                                 "%s, %s, %s, %s, %s, %s"
                                 ") "
                                 "ON CONFLICT DO NOTHING",
                                 (item['match_id'],
                                  item['away_prep_focus'],
                                  item['away_prep_pace'],
                                  item['home_prep_focus'],
                                  item['home_prep_pace'],
                                  item['away_outside_off'],
                                  item['away_inside_off'],
                                  item['away_outside_def'],
                                  item['away_inside_def'],
                                  item['away_reb'],
                                  item['away_off_flow'],
                                  item['home_outside_off'],
                                  item['home_inside_off'],
                                  item['home_outside_def'],
                                  item['home_inside_def'],
                                  item['home_reb'],
                                  item['home_off_flow'],
                                  item['home_prep_focus_matched'],
                                  item['home_prep_pace_matched'],
                                  item['away_prep_focus_matched'],
                                  item['away_prep_pace_matched'],
                                  item['match_type'],
                                  item['away_off_strategy'],
                                  item['away_def_strategy'],
                                  item['home_off_strategy'],
                                  item['home_def_strategy'],
                                  )
                                 )
                self.conn.commit()
            except IntegrityError as e:
                print("Duplicate primary key entry, skipping")
            return item
        if isinstance(item, BoxscoreStatsItem):
            try:
                self.cur.execute("INSERT INTO boxscore_stats VALUES("
                                 "%s, %s, %s, %s, %s, "
                                 "%s, %s, %s, %s, %s, "
                                 "%s, %s, %s, %s, %s, "
                                 "%s, %s, %s, %s, %s, "
                                 "%s, %s, %s) "
                                 "ON CONFLICT DO NOTHING",
                                 (item['match_id'],
                                  item['player_id'],
                                  item['pg_min'],
                                  item['sg_min'],
                                  item['sf_min'],
                                  item['pf_min'],
                                  item['c_min'],
                                  item['fgm'],
                                  item['fga'],
                                  item['tpm'],
                                  item['tpa'],
                                  item['ftm'],
                                  item['fta'],
                                  item['oreb'],
                                  item['reb'],
                                  item['ast'],
                                  item['t_o'],
                                  item['stl'],
                                  item['blk'],
                                  item['pf'],
                                  item['pts'],
                                  item['rating'],
                                  item['team_id']
                                  )
                                 )
                self.conn.commit()
            except IntegrityError as e:
                print("Duplicate primary key entry in teams, skipping")
                print(e)
            return item
        if isinstance(item, TeamItem):
            try:
                self.cur.execute("INSERT INTO teams VALUES(%s, %s) "
                                 "ON CONFLICT DO NOTHING",
                                 (item['id'],
                                  item['name']))
                self.conn.commit()
            except IntegrityError as e:
                print("Duplicate primary key entry in teams, skipping")
                print(e)
            return item
        if isinstance(item, OnlinePeopleItem):
            self.cur.execute("INSERT INTO online_people ("
                             "scrape_date,"
                             "value) "
                             "VALUES(current_timestamp, %s)",
                             [item['value']])
            self.conn.commit()
            return item
        if isinstance(item, PlayerItem):
            try:
                self.cur.execute("INSERT INTO players ("
                                 "id,"
                                 "created_at,"
                                 "last_update_at,"
                                 "team_id,"
                                 "weekly_salary,"
                                 "dmi,"
                                 "age,"
                                 "height,"
                                 "position,"
                                 "name,"
                                 "transfer_estimate,"
                                 "potential) "
                                 "VALUES(%s, current_timestamp, current_timestamp, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
                                 "ON CONFLICT (id) DO UPDATE SET "
                                 "last_update_at=current_timestamp,"
                                 "team_id=EXCLUDED.team_id,"
                                 "weekly_salary=EXCLUDED.weekly_salary,"
                                 "dmi=EXCLUDED.dmi,"
                                 "age=EXCLUDED.age,"
                                 "height=EXCLUDED.height,"
                                 "position=EXCLUDED.position,"
                                 "transfer_estimate=EXCLUDED.transfer_estimate,"
                                 "potential=EXCLUDED.potential",
                                 (item['id'],
                                  item['team_id'],
                                  item['weekly_salary'],
                                  item['dmi'],
                                  item['age'],
                                  item['height'],
                                  item['position'],
                                  item['name'],
                                  item['transfer_estimate'],
                                  item['potential']))
                self.conn.commit()
            except IntegrityError as e:
                print("Duplicate primary key entry in players, skipping")
                print(e)
            return item
        if isinstance(item, PlayerSkillsItem):
            try:
                self.cur.execute("INSERT INTO player_skills (player_id,"
                                 "date,"
                                 "game_shape,"
                                 "experience,"
                                 "jump_shot,"
                                 "jump_range, "
                                 "outside_def, "
                                 "handling, "
                                 "driving, "
                                 "passing, "
                                 "inside_shot, "
                                 "inside_def, "
                                 "rebounding, "
                                 "shot_blocking, "
                                 "stamina, "
                                 "free_throw"
                                 ") "
                                 "VALUES("
                                 "%s, current_timestamp, %s, %s,"
                                 "%s, %s, %s, %s,"
                                 "%s, %s, %s, %s,"
                                 "%s, %s, %s, %s"
                                 ") "
                                 "ON CONFLICT DO NOTHING "
                                 ,
                                 (
                                     item.get('player_id', None),
                                     item.get('game_shape', None),
                                     item.get('experience', None),
                                     item.get('jump_shot', None),
                                     item.get('jump_range', None),
                                     item.get('outside_def', None),
                                     item.get('handling', None),
                                     item.get('driving', None),
                                     item.get('passing', None),
                                     item.get('inside_shot', None),
                                     item.get('inside_def', None),
                                     item.get('rebounding', None),
                                     item.get('shot_blocking', None),
                                     item.get('stamina', None),
                                     item.get('free_throw', None),
                                 ))
                self.conn.commit()
            except IntegrityError as e:
                print(
                    "Duplicate primary key entry in player_skills, skipping")
                print(e)
            return item
        if isinstance(item, PlayerHistoryItem):
            self.cur.execute("INSERT INTO player_history (player_id,"
                             "event,"
                             "date,"
                             "season,"
                             "details) "
                             "VALUES(%s, %s, %s, %s, %s) "
                             "ON CONFLICT DO NOTHING",
                             (item['player_id'],
                              item['event'],
                              item['date'],
                              item['season'],
                              item['details']))
            self.conn.commit()
            return item
        if isinstance(item, SeasonItem):
            self.cur.execute("INSERT INTO seasons (id,"
                             "start_date,"
                             "end_date) "
                             "VALUES(%s, %s, %s) "
                             "ON CONFLICT (id) DO UPDATE SET "
                             "start_date=EXCLUDED.start_date, "
                             "end_date=EXCLUDED.end_date",
                             (item['season_id'],
                              item['start_date'],
                              item['end_date']))
            self.conn.commit()
            return item
        if isinstance(item, SeasonLeagueTeamItem):
            self.cur.execute("INSERT INTO seasons_leagues_teams ("
                             "season_id,"
                             "league_id,"
                             "team_id) "
                             "VALUES(%s, %s, %s) "
                             "ON CONFLICT DO NOTHING",
                             (item['season_id'],
                              item['league_id'],
                              item['team_id']))
            self.conn.commit()
            return item
