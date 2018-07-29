# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BoxscoreStats(models.Model):
    match = models.ForeignKey('Matches', models.DO_NOTHING, primary_key=True)
    player_id = models.IntegerField()
    pg_min = models.SmallIntegerField()
    sg_min = models.SmallIntegerField()
    sf_min = models.SmallIntegerField()
    pf_min = models.SmallIntegerField()
    c_min = models.SmallIntegerField()
    fgm = models.SmallIntegerField()
    fga = models.SmallIntegerField()
    tpm = models.SmallIntegerField()
    tpa = models.SmallIntegerField()
    ftm = models.SmallIntegerField()
    fta = models.SmallIntegerField()
    oreb = models.SmallIntegerField()
    reb = models.SmallIntegerField()
    ast = models.SmallIntegerField()
    t_o = models.SmallIntegerField()
    stl = models.SmallIntegerField()
    blk = models.SmallIntegerField()
    pf = models.SmallIntegerField()
    pts = models.SmallIntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    team = models.ForeignKey('Teams', models.DO_NOTHING)


    class Meta:
        managed = False
        db_table = 'boxscore_stats'
        unique_together = (('match', 'player_id'),)


class Boxscores(models.Model):
    match = models.OneToOneField('Matches', models.DO_NOTHING, primary_key=True)
    away_prep_focus = models.TextField(blank=True, null=True)  # This field type is a guess.
    away_prep_pace = models.TextField(blank=True, null=True)  # This field type is a guess.
    home_prep_focus = models.TextField(blank=True, null=True)  # This field type is a guess.
    home_prep_pace = models.TextField(blank=True, null=True)  # This field type is a guess.
    away_outside_off = models.DecimalField(max_digits=3, decimal_places=1)
    away_inside_off = models.DecimalField(max_digits=3, decimal_places=1)
    away_outside_def = models.DecimalField(max_digits=3, decimal_places=1)
    away_inside_def = models.DecimalField(max_digits=3, decimal_places=1)
    away_reb = models.DecimalField(max_digits=3, decimal_places=1)
    away_off_flow = models.DecimalField(max_digits=3, decimal_places=1)
    home_outside_off = models.DecimalField(max_digits=3, decimal_places=1)
    home_inside_off = models.DecimalField(max_digits=3, decimal_places=1)
    home_outside_def = models.DecimalField(max_digits=3, decimal_places=1)
    home_inside_def = models.DecimalField(max_digits=3, decimal_places=1)
    home_reb = models.DecimalField(max_digits=3, decimal_places=1)
    home_off_flow = models.DecimalField(max_digits=3, decimal_places=1)
    home_prep_focus_matched = models.CharField(max_length=4, blank=True, null=True)
    home_prep_pace_matched = models.CharField(max_length=4, blank=True, null=True)
    away_prep_focus_matched = models.CharField(max_length=4, blank=True, null=True)
    away_prep_pace_matched = models.CharField(max_length=4, blank=True, null=True)
    match_type = models.CharField(max_length=30)
    away_off_strategy = models.TextField()  # This field type is a guess.
    away_def_strategy = models.TextField()  # This field type is a guess.
    home_off_strategy = models.TextField()  # This field type is a guess.
    home_def_strategy = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'boxscores'


class Matches(models.Model):
    id = models.IntegerField(primary_key=True)
    match_date = models.DateField()
    home_team = models.ForeignKey('Teams', models.DO_NOTHING, related_name='%(class)s_home_team_id')
    away_team = models.ForeignKey('Teams', models.DO_NOTHING, related_name='%(class)s_away_team_id')
    season = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'matches'


class OnlinePeople(models.Model):
    scrape_date = models.DateTimeField()
    value = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'online_people'


class PlayByPlays(models.Model):
    id = models.BigIntegerField(primary_key=True)
    event_type = models.CharField(max_length=30)
    quarter = models.SmallIntegerField()
    clock = models.CharField(max_length=6)
    score = models.CharField(max_length=10)
    event = models.TextField()
    match = models.ForeignKey(Boxscores, models.DO_NOTHING)
    play_tags = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'play_by_plays'

    def __str__(self):
        return self.event_type + ': ' + self.event


class PlayerHistory(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING, primary_key=True)
    event = models.CharField(max_length=25)
    date = models.DateField()
    season = models.SmallIntegerField()
    details = models.TextField()

    class Meta:
        managed = False
        db_table = 'player_history'
        unique_together = (('player', 'date', 'event'),)

    def __str__(self):
        return self.player.name


class PlayerSkills(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING, primary_key=True)
    date = models.DateTimeField(primary_key=True)
    skill = models.TextField(primary_key=True)  # This field type is a guess.
    value = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'player_skills'
        unique_together = (('player', 'skill', 'value'), ('player', 'skill', 'value'),)

    def __str__(self):
        return self.player.name


class Players(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField()
    last_update_at = models.DateTimeField(blank=True, null=True)
    weekly_salary = models.IntegerField()
    dmi = models.IntegerField()
    age = models.SmallIntegerField()
    height = models.SmallIntegerField()
    position = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=80, blank=True, null=True)
    team = models.ForeignKey('Teams', models.DO_NOTHING)
    transfer_estimate = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'players'

    def __str__(self):
        return self.name


class ScoreTables(models.Model):
    match = models.ForeignKey(Matches, models.DO_NOTHING, primary_key=True)
    qtr = models.SmallIntegerField()
    away_team_score = models.SmallIntegerField()
    home_team_score = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'score_tables'
        unique_together = (('match', 'qtr'),)


class Shots(models.Model):
    pbp = models.ForeignKey(PlayByPlays, models.DO_NOTHING, primary_key=True)
    outcome = models.TextField()  # This field type is a guess.
    defender = models.IntegerField(blank=True, null=True)
    defense_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    passer = models.IntegerField(blank=True, null=True)
    shooter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shots'

    def __str__(self):
        return self.outcome + ' by ' + self.shooter

class Teams(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'
