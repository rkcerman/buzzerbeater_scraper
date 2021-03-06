from django.db import models


class PlayerSkillsManager(models.Manager):

    # Returns latest skills formatted as a dict
    def latest_skills(self, pk):
        _skills = (
            'game_shape',
            'experience',
            'jump_shot',
            'jump_range',
            'outside_def',
            'handling',
            'driving',
            'passing',
            'inside_shot',
            'inside_def',
            'rebounding',
            'shot_blocking',
            'stamina',
            'free_throw',
        )
        data = {}

        ps = self.filter(pk=pk).order_by('-date')

        for skill in _skills:
            try:
                skill_set = ps.filter(**{skill + '__isnull': False})[0]
            except IndexError:
                skill_set = None
            else:
                data[skill] = getattr(skill_set, skill)

        return data


class BoxscoreStats(models.Model):
    boxscore = models.ForeignKey('Boxscores', models.DO_NOTHING,
                                 primary_key=True)
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
    rating = models.DecimalField(max_digits=3, decimal_places=1, blank=True,
                                 null=True)
    team = models.ForeignKey('Teams', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'boxscore_stats'
        unique_together = (('boxscore', 'player_id'),)


class Boxscores(models.Model):
    match = models.OneToOneField('Matches', models.DO_NOTHING,
                                 primary_key=True)
    away_prep_focus = models.TextField(blank=True,
                                       null=True)
    away_prep_pace = models.TextField(blank=True,
                                      null=True)
    home_prep_focus = models.TextField(blank=True,
                                       null=True)
    home_prep_pace = models.TextField(blank=True,
                                      null=True)
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
    home_prep_focus_matched = models.CharField(max_length=4, blank=True,
                                               null=True)
    home_prep_pace_matched = models.CharField(max_length=4, blank=True,
                                              null=True)
    away_prep_focus_matched = models.CharField(max_length=4, blank=True,
                                               null=True)
    away_prep_pace_matched = models.CharField(max_length=4, blank=True,
                                              null=True)
    match_type = models.CharField(max_length=30)
    away_off_strategy = models.TextField()
    away_def_strategy = models.TextField()
    home_off_strategy = models.TextField()
    home_def_strategy = models.TextField()

    class Meta:
        managed = False
        db_table = 'boxscores'

    def __str__(self):
        return 'Boxscore ' + self.match.__str__()


class Countries(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    divisions = models.SmallIntegerField(null=True)
    first_season = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'countries'

    def __str__(self):
        return self.name


class Leagues(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    country = models.ForeignKey('Countries', models.DO_NOTHING)
    level = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'leagues'

    def __str__(self):
        return self.name


class Matches(models.Model):
    id = models.IntegerField(primary_key=True)
    match_date = models.DateField()
    home_team = models.ForeignKey('Teams', models.DO_NOTHING,
                                  related_name='%(class)s_home_team_id')
    away_team = models.ForeignKey('Teams', models.DO_NOTHING,
                                  related_name='%(class)s_away_team_id')
    season = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'matches'

    def __str__(self):
        return '{} - {} vs. {}'.format(
            self.match_date,
            self.away_team,
            self.home_team
        )


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
    boxscore = models.ForeignKey(Boxscores, models.DO_NOTHING)
    play_tags = models.TextField(blank=True,
                                 null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'play_by_plays'

    def __str__(self):
        return self.event_type + ': ' + self.event


class PlayerHistory(models.Model):
    player = models.ForeignKey('Players', models.DO_NOTHING,
                               primary_key=True)
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
    player = models.ForeignKey('Players', models.DO_NOTHING,
                               primary_key=True)
    date = models.DateTimeField()
    game_shape = models.SmallIntegerField()
    experience = models.SmallIntegerField()
    jump_shot = models.SmallIntegerField()
    jump_range = models.SmallIntegerField()
    outside_def = models.SmallIntegerField()
    handling = models.SmallIntegerField()
    driving = models.SmallIntegerField()
    passing = models.SmallIntegerField()
    inside_shot = models.SmallIntegerField()
    inside_def = models.SmallIntegerField()
    rebounding = models.SmallIntegerField()
    shot_blocking = models.SmallIntegerField()
    stamina = models.SmallIntegerField()
    free_throw = models.SmallIntegerField()

    objects = PlayerSkillsManager()
    class Meta:
        managed = False
        db_table = 'player_skills'
        unique_together = (('player', 'date'),)

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
    potential = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'players'

    def __str__(self):
        return self.name


class Seasons(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True) # In case season in progress

    class Meta:
        managed = False
        db_table = 'seasons'

    def __str__(self):
        return str(self.id)


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
    pbp = models.ForeignKey(PlayByPlays, models.DO_NOTHING,
                            primary_key=True)
    outcome = models.TextField()  # This field type is a guess.
    defender = models.IntegerField(blank=True, null=True)
    defense_type = models.TextField(blank=True,
                                    null=True)  # This field type is a guess.
    passer = models.IntegerField(blank=True, null=True)
    shooter = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shots'

    def __str__(self):
        return self.outcome + ' by ' + str(self.shooter)


class Teams(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    owner = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'

    def __str__(self):
        return str(self.id) + ' - ' + str(self.name)


class SeasonsLeaguesTeams(models.Model):
    season = models.ForeignKey(Seasons, models.DO_NOTHING, primary_key=True)
    league = models.ForeignKey(Leagues, models.DO_NOTHING)
    team = models.ForeignKey(Teams, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'seasons_leagues_teams'
        unique_together = (('season', 'league', 'team'),)

    def __str__(self):
        return '%s %s %s' % (self.season, self.league, self.team)
