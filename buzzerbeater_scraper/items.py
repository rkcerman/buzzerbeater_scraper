# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayByPlayItem(scrapy.Item):
    id = scrapy.Field()
    match_id = scrapy.Field()
    event_type = scrapy.Field()
    quarter = scrapy.Field()
    clock = scrapy.Field()
    score = scrapy.Field()
    event = scrapy.Field()
    play_tags = scrapy.Field()
    pass


class ShotsItem(scrapy.Item):
    pbp_id = scrapy.Field()
    shooter = scrapy.Field()
    outcome = scrapy.Field()
    defender = scrapy.Field()
    defense_type = scrapy.Field()
    passer = scrapy.Field()


class MatchItem(scrapy.Item):
    id = scrapy.Field()
    match_date = scrapy.Field()
    home_team_id = scrapy.Field()
    away_team_id = scrapy.Field()
    season = scrapy.Field()


class TeamItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()


class OnlinePeopleItem(scrapy.Item):
    value = scrapy.Field()


class PlayerItem(scrapy.Item):
    id = scrapy.Field()
    weekly_salary = scrapy.Field()
    dmi = scrapy.Field()
    age = scrapy.Field()
    height = scrapy.Field()
    position = scrapy.Field()
    name = scrapy.Field()
    team_id = scrapy.Field()
    transfer_estimate = scrapy.Field()


class PlayerHistoryItem(scrapy.Item):
    player_id = scrapy.Field()
    event = scrapy.Field()
    date = scrapy.Field()
    season = scrapy.Field()
    details = scrapy.Field()


class PlayerSkillsItem(scrapy.Item):
    player_id = scrapy.Field()
    skill = scrapy.Field()
    value = scrapy.Field()
