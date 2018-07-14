from buzzerbeater_scraper.items import PlayByPlayItem, ShotsItem

mock_info_item = PlayByPlayItem(
    id=1,
    match_id=11,
    event_type='SUBSTITUTION',
    quarter=1,
    clock='11:23',
    score='86 - 80',
    event='P. Vaculčiak (H) substituted for M. Ilić (H) at SG.',
    play_tags='info',
)

mock_unguarded_item = PlayByPlayItem(
    id=2,
    match_id=11,
    event_type='SUBSTITUTION',
    quarter=1,
    clock='11:23',
    score='86 - 80',
    event='P. Vaculčiak (H) substituted for M. Ilić (H) at SG.',
    play_tags='info',
)
