from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

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


@register.inclusion_tag('bbstats/player_info.html', takes_context=True)
def player_info(context):
    return_context = {
            'player': context['player'],
            'potential': context['potential'],
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
