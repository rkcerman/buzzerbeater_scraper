from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

skills_mapping = {
    1: 'atrocious',
    2: 'pitiful',
    3: 'awful',
    4: 'inept',
    5: 'mediocre',
    6: 'average',
    7: 'respectable',
    8: 'strong',
    9: 'proficient',
    10: 'prominent',
    11: 'prolific',
    12: 'sensational',
    13: 'tremendous',
    14: 'wondrous',
    15: 'marvelous',
    16: 'prodigious',
    17: 'stupendous',
    18: 'phenomenal',
    19: 'colossal',
    20: 'legendary',
}

potentials_mapping = {
    0: ('announcer', 'lev5'),
    1: ('bench warmer', 'lev6'),
    2: ('role player', 'lev7'),
    3: ('6th man', 'lev8'),
    4: ('starter', 'lev9'),
    5: ('star', 'lev10'),
    6: ('allstar', 'lev11'),
    7: ('perennial allstar', 'lev12'),
    8: ('superstar', 'lev13'),
    9: ('MVP', 'lev15'),
    10: ('hall of famer', 'lev16'),
    11: ('all-time great', 'lev17'),
}

strategies_initials_mapping = {
    'Patient': 'Pa',
    'Base': 'BO',
    'Push': 'PB',
    'Princeton': 'Pr',
    'Motion': 'Mo',
    'RunAndGun': 'RG',
    'LowPost': 'LP',
    'LookInside': 'LI',
    'OutsideIsolation': 'OI',
    'InsideIsolation': 'II',
    'ManToMan': 'MM',
    '23Zone': '23',
    '131Zone': '13',
    '32Zone': '32',
    'Press': 'FP',
    'InsideBoxAndOne': 'IB',
    'OutsideBoxAndOne': 'OB',
}

hit_miss_mapping = {
    'hit': '✓',
    'miss': 'x',
    None: '--'
}


# Turns a strategy name into simple initials
@register.filter(is_safe=True)
@stringfilter
def to_initials(value):
    try:
        initials = strategies_initials_mapping[value]
    except KeyError:
        return '-'
    else:
        return initials


# Turns 'None' to empty string
@register.filter(is_safe=True)
@stringfilter
def none_to_empty(value):
    return '' if value == 'None' else value


# Turns a strategy name into simple initials
@register.filter(is_safe=True)
def to_hit_miss(value):
    try:
        hit_miss_symbol = hit_miss_mapping[value]
    except KeyError:
        return '-'
    else:
        return hit_miss_symbol


# Returns the 'lev' number for player's potential
# The 'lev' is used for styling
@register.filter(is_safe=True)
def potential_lev(potential):
    try:
        return potentials_mapping[potential][1]
    except KeyError:
        return ''


# Returns the verbal name for player's potential
@register.filter(is_safe=True)
def potential_name(potential):
    try:
        return potentials_mapping[potential][0]
    except KeyError:
        return ''


# Skill values above 20 used the same styling and nomenc.
# as the skill value 20/'legendary'
@register.filter(is_safe=True)
def skill_name(skill):
    if skill == '':
        return skill
    else:
        if skill < 21:
            return skills_mapping[skill]
        else:
            return skills_mapping[20]


# Includes the player info table with skills
@register.inclusion_tag('bbstats/player_info.html', takes_context=True)
def player_info(context):
    return_context = {
            'player': context['player'],
            'skills': context['skills'],
    }
    try:
        tsp = context['tsp']
        gsp = context['gsp']
        fsp = context['fsp']
    except KeyError:
        return return_context
    else:
        return_context['tsp'] = tsp
        return_context['gsp'] = gsp
        return_context['fsp'] = fsp
        return return_context
