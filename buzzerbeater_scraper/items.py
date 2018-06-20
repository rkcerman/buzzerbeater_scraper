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
