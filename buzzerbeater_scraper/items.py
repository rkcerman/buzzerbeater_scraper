# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayByPlayItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    match_id = scrapy.Field()
    event_type = scrapy.Field()
    quarter = scrapy.Field()
    clock = scrapy.Field()
    score = scrapy.Field()
    event = scrapy.Field()
    pass

class MatchItem(scrapy.Item):
    id = scrapy.Field()
    match_date = scrapy.Field()
    home_team_id = scrapy.Field()
    away_team_id = scrapy.Field()

class TeamItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()

class OnlinePeopleItem(scrapy.Item):
    value = scrapy.Field()
