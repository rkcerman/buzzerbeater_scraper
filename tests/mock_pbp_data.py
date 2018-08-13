from buzzerbeater_scraper.items import PlayByPlayItem

MOCK_INFO_ITEM = PlayByPlayItem(
    id=1,
    match_id=11,
    event_type='SUBSTITUTION',
    quarter=1,
    clock='11:23',
    score='86 - 80',
    event='4534342 substituted for 12345678 (H) at SG.',
    play_tags='info',
)

MOCK_DLAYUP_MISSED_ITEM = PlayByPlayItem(
    id=2,
    match_id=11,
    event_type='JUMP_SHOT',
    quarter=1,
    clock='11:23',
    score='86 - 80',
    event='987654321 attempts a jump-shot from the wing.  Shot missed.',
    play_tags=['shot', 'mid']
)

MOCK_NO_EVENT_ITEM = PlayByPlayItem(
    id=2,
    match_id=11,
    event_type='JUMP_SHOT',
    quarter=1,
    clock='11:23',
    score='86 - 80',
    play_tags=['shot', 'mid']
)

MOCK_PASSER_PATTERNS = [
    '32957585 tries a driving layup off of a nice pass from 1234567.  Shot missed.',
    '1234567 gets off a great pass to 28668697. 28668697 attempts a baseline jumper.  Scored.',
    '1234567 opens up the play with a pass to 42240378. 42240378 shoots while falling away.  Shot missed.',
    '1234567 threads a pass through the defense and finds 31837161.  31837161 attempts a jumper from the elbow.  Shot missed.',
    '1234567  finds 43109016 in space. 43109016 tries a driving layup.  Shot missed.'
]
