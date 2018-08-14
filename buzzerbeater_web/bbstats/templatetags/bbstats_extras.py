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


@register.filter(is_safe=True)
@stringfilter
def to_initials(value):
    try:
        initials = strategies_initials_mapping[value]
    except KeyError:
        return '-'
    else:
        return initials

