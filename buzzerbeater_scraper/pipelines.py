# -*- coding: utf-8 -*-

import psycopg2
from psycopg2 import IntegrityError


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from buzzerbeater_scraper.items import PlayByPlayItem, MatchItem, TeamItem, OnlinePeopleItem


class BuzzerbeaterScraperPipeline(object):
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'rkcerman'  # the username when you create the database
        password = 'konzolka.23'  # change to your password
        database = 'testpython'
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
                self.cur.execute("INSERT INTO matches VALUES(%s, %s, %s, %s) ON CONFLICT DO NOTHING",
                                 (item['id'], item['match_date'], item['home_team_id'], item['away_team_id']))
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
                print("Duplicate primary key entry, skipping")
            return item
        if isinstance(item, OnlinePeopleItem):
            self.cur.execute("INSERT INTO online_people (scrape_date, value) VALUES(current_timestamp, %s)",
                             [item['value']])
            self.conn.commit()
            return item
