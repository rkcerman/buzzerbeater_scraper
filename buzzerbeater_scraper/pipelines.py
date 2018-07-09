# -*- coding: utf-8 -*-

import buzzerbeater_scraper.config
import psycopg2
from psycopg2 import IntegrityError


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from buzzerbeater_scraper.items import PlayByPlayItem, MatchItem, TeamItem, OnlinePeopleItem, PlayerItem, \
    PlayerSkillsItem, PlayerHistoryItem


# TODO implement UPSERT
class BuzzerbeaterScraperPipeline(object):
    def open_spider(self, spider):
        hostname = buzzerbeater_scraper.config.DATABASE_CONFIG['hostname']
        username = buzzerbeater_scraper.config.DATABASE_CONFIG['username']
        password = buzzerbeater_scraper.config.DATABASE_CONFIG['password']
        database = buzzerbeater_scraper.config.DATABASE_CONFIG['database']
        self.conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.conn.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()

    def process_item(self, item, spider):
        if isinstance(item, PlayByPlayItem):
            try:
                self.cur.execute("INSERT INTO play_by_plays VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING",
                                 (item['id'], item['event_type'], item['quarter'],
                                  item['clock'], item['score'], item['event'], item['match_id']))
                self.conn.commit()
            except IntegrityError as e:
                print("Duplicate primary key entry, skipping")
            return item
        if isinstance(item, MatchItem):
            try:
                self.cur.execute("INSERT INTO matches VALUES(%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING"
                                 " SET season=EXCLUDED.season",
                                 (item['id'], item['match_date'], item['home_team_id'], item['away_team_id'],
                                  item['season']))
                self.conn.commit()
            except IntegrityError as e:
                print("Duplicate primary key entry, skipping")
            return item
        if isinstance(item, TeamItem):
            try:
                self.cur.execute("INSERT INTO teams VALUES(%s, %s) ON CONFLICT DO NOTHING",
                                 (item['id'], item['name']))
                self.conn.commit()
            except IntegrityError as e:
                print("Duplicate primary key entry in teams, skipping")
                print(e)
            return item
        if isinstance(item, OnlinePeopleItem):
            self.cur.execute("INSERT INTO online_people (scrape_date, value) VALUES(current_timestamp, %s)",
                             [item['value']])
            self.conn.commit()
            return item
        if isinstance(item, PlayerItem):
            try:
                self.cur.execute("INSERT INTO players (id, created_at, last_update_at, team_id, weekly_salary, dmi,"
                                 "age, height, position, name, transfer_estimate)"
                                 " VALUES(%s, current_timestamp, current_timestamp, %s, %s, %s, %s, %s, %s, %s, %s) "
                                 "ON CONFLICT (id) DO UPDATE "
                                 "SET last_update_at=current_timestamp, team_id=EXCLUDED.team_id, "
                                 "weekly_salary=EXCLUDED.weekly_salary, dmi=EXCLUDED.dmi, "
                                 "age=EXCLUDED.age, height=EXCLUDED.height, position=EXCLUDED.position, "
                                 "transfer_estimate=EXCLUDED.transfer_estimate",
                                 (item['id'], item['team_id'], item['weekly_salary'], item['dmi'],
                                  item['age'], item['height'], item['position'], item['name'], item['transfer_estimate']))
                self.conn.commit()
            except IntegrityError as e:
                print("Duplicate primary key entry in players, skipping")
                print(e)
            return item
        if isinstance(item, PlayerSkillsItem):
            try:
                self.cur.execute("INSERT INTO player_skills (date, player_id, skill, value)"
                                 " VALUES(current_timestamp, %s, %s, %s) "
                                 "ON CONFLICT DO NOTHING",
                                 (item['player_id'], item['skill'], item['value']))
                self.conn.commit()
            except IntegrityError as e:
                print("Duplicate primary key entry in player_skills, skipping")
                print(e)
            return item
        if isinstance(item, PlayerHistoryItem):
            self.cur.execute("INSERT INTO player_history (player_id, event, date, season, details)"
                             " VALUES(%s, %s, %s, %s, %s) "
                             "ON CONFLICT DO NOTHING",
                             (item['player_id'], item['event'], item['date'], item['season'], item['details']))
            self.conn.commit()
            return item

