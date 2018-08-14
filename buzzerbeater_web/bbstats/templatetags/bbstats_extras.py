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


@register.inclusion_tag('bbstats/player_info.html', takes_context=True)
def player_info(context):
    return {
        'player': context['player'],
        'potential': context['potential'],
        'skills': context['skills'],
        'tsp': context['tsp'],
        'fsp': context['fsp'],
        'gsp': context['gsp'],
    }
