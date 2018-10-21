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


class SeasonItem(scrapy.Item):
    season_id = scrapy.Field()
    start_date = scrapy.Field()
    end_date = scrapy.Field()


class ScoreTableItem(scrapy.Item):
    match_id = scrapy.Field()
    qtr = scrapy.Field()
    away_team_score = scrapy.Field()
    home_team_score = scrapy.Field()


class BoxscoreItem(scrapy.Item):
    match_id = scrapy.Field()
    away_off_strategy = scrapy.Field()
    away_def_strategy = scrapy.Field()
    away_prep_focus = scrapy.Field()
    away_prep_pace = scrapy.Field()
    home_off_strategy = scrapy.Field()
    home_def_strategy = scrapy.Field()
    home_prep_focus = scrapy.Field()
    home_prep_pace = scrapy.Field()
    away_outside_off = scrapy.Field()
    away_inside_off = scrapy.Field()
    away_outside_def = scrapy.Field()
    away_inside_def = scrapy.Field()
    away_reb = scrapy.Field()
    away_off_flow = scrapy.Field()
    home_outside_off = scrapy.Field()
    home_inside_off = scrapy.Field()
    home_outside_def = scrapy.Field()
    home_inside_def = scrapy.Field()
    home_reb = scrapy.Field()
    home_off_flow = scrapy.Field()
    home_prep_focus_matched = scrapy.Field()
    home_prep_pace_matched = scrapy.Field()
    away_prep_focus_matched = scrapy.Field()
    away_prep_pace_matched = scrapy.Field()
    match_type = scrapy.Field()


class BoxscoreStatsItem(scrapy.Item):
    match_id = scrapy.Field()
    team_id = scrapy.Field()
    player_id = scrapy.Field()
    pg_min = scrapy.Field()
    sg_min = scrapy.Field()
    sf_min = scrapy.Field()
    pf_min = scrapy.Field()
    c_min = scrapy.Field()
    fgm = scrapy.Field()
    fga = scrapy.Field()
    tpm = scrapy.Field()
    tpa = scrapy.Field()
    ftm = scrapy.Field()
    fta = scrapy.Field()
    oreb = scrapy.Field()
    reb = scrapy.Field()
    ast = scrapy.Field()
    t_o = scrapy.Field()
    stl = scrapy.Field()
    blk = scrapy.Field()
    pf = scrapy.Field()
    pts = scrapy.Field()
    rating = scrapy.Field()


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
    potential = scrapy.Field()


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
