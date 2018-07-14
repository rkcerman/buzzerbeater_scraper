from buzzerbeater_scraper.items import PlayByPlayItem, ShotsItem

mock_info_item = PlayByPlayItem(
    id=1,
    match_id=11,
    event_type='SUBSTITUTION',
    quarter=1,
    clock='11:23',
    score='86 - 80',
    event='4534342 substituted for 12345678 (H) at SG.',
    play_tags='info',
)

mock_dlayup_missed_item = PlayByPlayItem(
    id=2,
    match_id=11,
    event_type='DRIVING_LAYUP',
    quarter=1,
    clock='11:23',
    score='86 - 80',
    event='987654321 attempts a jump-shot from the wing.  Shot missed.',
    play_tags=['shot', 'mid']
)
