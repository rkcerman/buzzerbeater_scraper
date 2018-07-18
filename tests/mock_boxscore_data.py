from buzzerbeater_scraper.items import BoxscoreStatsItem

MOCK_SCORE_TABLE_DICT = {
    1: {
        'match_id': 101245565,
        'qtr' : 1,
        'away_team_score': 23,
        'home_team_score': 29
    },
    2: {
        'match_id': 101245565,
        'qtr' : 2,
        'away_team_score': 14,
        'home_team_score': 19
    },
    3: {
        'match_id': 101245565,
        'qtr' : 3,
        'away_team_score': 19,
        'home_team_score': 20
    },
    4: {
        'match_id': 101245565,
        'qtr' : 4,
        'away_team_score': 29,
        'home_team_score': 29
    }
}

MOCK_BOXSCORE_STATS_DICT = {
    'match_id':101245565,
    'player_id':28668697,
    'pg_min':0,
    'sg_min':0,
    'sf_min':0,
    'pf_min':34,
    'c_min':0,
    'fgm':6,
    'fga':11,
    'tpm':1,
    'tpa':1,
    'ftm':0,
    'fta':0,
    'oreb':4,
    'reb':13,
    'ast':6,
    't_o':2,
    'stl':0,
    'blk':0,
    'pf':3,
    'pts':13,
    'rating':12
}

MOCK_BOXSCORE_XML ='<bbapi version="1">' \
'<match id="101245565" retrieved="2018-07-16T15:37:19Z" type="league.rs">' \
'<neutral>0</neutral>' \
'<startTime>2018-04-14T16:00:00Z</startTime>' \
'<endTime>2018-04-14T17:41:53Z</endTime>' \
'<effortDelta>1</effortDelta>' \
'<attendance>' \
'<bleachers>7708</bleachers>' \
'<lowerTier>1351</lowerTier>' \
'<courtside>284</courtside>' \
'<luxury>12</luxury>' \
'</attendance>' \
'<awayTeam id="58377">' \
'<teamname>BK sever 5</teamname>' \
'<shortname>BK </shortname>' \
'<score partials="23,14,19,29">85</score>' \
'<offStrategy>RunAndGun</offStrategy>' \
'<defStrategy>ManToMan</defStrategy>' \
'<boxscore>' \
'<player id="28668697">' \
'<firstname>Fernand</firstname>' \
'<lastname>Le Goff</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>34</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>6</fgm>' \
'<fga>11</fga>' \
'<tpm>1</tpm>' \
'<tpa>1</tpa>' \
'<ftm>0</ftm>' \
'<fta>0</fta>' \
'<oreb>4</oreb>' \
'<reb>13</reb>' \
'<ast>6</ast>' \
'<to>2</to>' \
'<stl>0</stl>' \
'<blk>0</blk>' \
'<pf>3</pf>' \
'<pts>13</pts>' \
'<rating>12</rating>' \
'</performance>' \
'</player>' \
'<player id="35115556">' \
'<firstname>Curtis</firstname>' \
'<lastname>Harris</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>41</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>6</fgm>' \
'<fga>21</fga>' \
'<tpm>2</tpm>' \
'<tpa>5</tpa>' \
'<ftm>2</ftm>' \
'<fta>3</fta>' \
'<oreb>2</oreb>' \
'<reb>4</reb>' \
'<ast>2</ast>' \
'<to>2</to>' \
'<stl>1</stl>' \
'<blk>0</blk>' \
'<pf>2</pf>' \
'<pts>16</pts>' \
'<rating>9</rating>' \
'</performance>' \
'</player>' \
'<player id="36218011">' \
'<firstname>Guillaume</firstname>' \
'<lastname>Geay</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>29</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>3</fgm>' \
'<fga>14</fga>' \
'<tpm>0</tpm>' \
'<tpa>8</tpa>' \
'<ftm>1</ftm>' \
'<fta>3</fta>' \
'<oreb>0</oreb>' \
'<reb>1</reb>' \
'<ast>0</ast>' \
'<to>2</to>' \
'<stl>0</stl>' \
'<blk>1</blk>' \
'<pf>2</pf>' \
'<pts>7</pts>' \
'<rating>8.5</rating>' \
'</performance>' \
'</player>' \
'<player id="36732163">' \
'<firstname>Sandis</firstname>' \
'<lastname>Klavinš</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>7</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>1</fgm>' \
'<fga>4</fga>' \
'<tpm>0</tpm>' \
'<tpa>0</tpa>' \
'<ftm>0</ftm>' \
'<fta>0</fta>' \
'<oreb>0</oreb>' \
'<reb>0</reb>' \
'<ast>1</ast>' \
'<to>0</to>' \
'<stl>0</stl>' \
'<blk>0</blk>' \
'<pf>3</pf>' \
'<pts>2</pts>' \
'<rating>7.5</rating>' \
'</performance>' \
'</player>' \
'<player id="36877385">' \
'<firstname>Hüseyin</firstname>' \
'<lastname>Nazgul</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>35</C>' \
'</minutes>' \
'<performance>' \
'<fgm>3</fgm>' \
'<fga>8</fga>' \
'<tpm>0</tpm>' \
'<tpa>2</tpa>' \
'<ftm>2</ftm>' \
'<fta>2</fta>' \
'<oreb>1</oreb>' \
'<reb>11</reb>' \
'<ast>0</ast>' \
'<to>3</to>' \
'<stl>0</stl>' \
'<blk>1</blk>' \
'<pf>4</pf>' \
'<pts>8</pts>' \
'<rating>11</rating>' \
'</performance>' \
'</player>' \
'<player id="36894298">' \
'<firstname>Miquel</firstname>' \
'<lastname>Miró</lastname>' \
'<minutes>' \
'<PG>27</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>3</fgm>' \
'<fga>12</fga>' \
'<tpm>2</tpm>' \
'<tpa>6</tpa>' \
'<ftm>5</ftm>' \
'<fta>6</fta>' \
'<oreb>1</oreb>' \
'<reb>3</reb>' \
'<ast>2</ast>' \
'<to>2</to>' \
'<stl>1</stl>' \
'<blk>0</blk>' \
'<pf>6</pf>' \
'<pts>13</pts>' \
'<rating>9.5</rating>' \
'</performance>' \
'</player>' \
'<player id="39156549">' \
'<firstname>Alberto</firstname>' \
'<lastname>Acosta</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>19</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>4</fgm>' \
'<fga>5</fga>' \
'<tpm>2</tpm>' \
'<tpa>3</tpa>' \
'<ftm>0</ftm>' \
'<fta>0</fta>' \
'<oreb>0</oreb>' \
'<reb>6</reb>' \
'<ast>3</ast>' \
'<to>0</to>' \
'<stl>1</stl>' \
'<blk>0</blk>' \
'<pf>2</pf>' \
'<pts>10</pts>' \
'<rating>12.5</rating>' \
'</performance>' \
'</player>' \
'<player id="39786791">' \
'<firstname>Elroy</firstname>' \
'<lastname>Steward</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>14</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>3</fgm>' \
'<fga>3</fga>' \
'<tpm>0</tpm>' \
'<tpa>0</tpa>' \
'<ftm>0</ftm>' \
'<fta>2</fta>' \
'<oreb>1</oreb>' \
'<reb>8</reb>' \
'<ast>0</ast>' \
'<to>1</to>' \
'<stl>0</stl>' \
'<blk>2</blk>' \
'<pf>2</pf>' \
'<pts>6</pts>' \
'<rating>13</rating>' \
'</performance>' \
'</player>' \
'<player id="40921645">' \
'<firstname>Pere</firstname>' \
'<lastname>Belengué</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>13</C>' \
'</minutes>' \
'<performance>' \
'<fgm>1</fgm>' \
'<fga>2</fga>' \
'<tpm>0</tpm>' \
'<tpa>0</tpa>' \
'<ftm>2</ftm>' \
'<fta>2</fta>' \
'<oreb>1</oreb>' \
'<reb>3</reb>' \
'<ast>0</ast>' \
'<to>0</to>' \
'<stl>0</stl>' \
'<blk>2</blk>' \
'<pf>0</pf>' \
'<pts>4</pts>' \
'<rating>11.5</rating>' \
'</performance>' \
'</player>' \
'<player id="41525134">' \
'<firstname>Peregrín</firstname>' \
'<lastname>Hraška</lastname>' \
'<minutes>' \
'<PG>21</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>3</fgm>' \
'<fga>7</fga>' \
'<tpm>0</tpm>' \
'<tpa>3</tpa>' \
'<ftm>0</ftm>' \
'<fta>2</fta>' \
'<oreb>0</oreb>' \
'<reb>3</reb>' \
'<ast>1</ast>' \
'<to>0</to>' \
'<stl>0</stl>' \
'<blk>0</blk>' \
'<pf>0</pf>' \
'<pts>6</pts>' \
'<rating>8</rating>' \
'</performance>' \
'</player>' \
'<player id="42239973">' \
'<firstname>Eugen</firstname>' \
'<lastname>Kašinský</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>0</fgm>' \
'<fga>0</fga>' \
'<tpm>0</tpm>' \
'<tpa>0</tpa>' \
'<ftm>0</ftm>' \
'<fta>0</fta>' \
'<oreb>0</oreb>' \
'<reb>0</reb>' \
'<ast>0</ast>' \
'<to>0</to>' \
'<stl>0</stl>' \
'<blk>0</blk>' \
'<pf>0</pf>' \
'<pts>0</pts>' \
'<rating>N/A</rating>' \
'<dnp/>' \
'</performance>' \
'</player>' \
'<teamTotals>' \
'<fgm>33</fgm>' \
'<fga>87</fga>' \
'<tpm>7</tpm>' \
'<tpa>28</tpa>' \
'<ftm>12</ftm>' \
'<fta>20</fta>' \
'<oreb>10</oreb>' \
'<reb>52</reb>' \
'<ast>15</ast>' \
'<to>12</to>' \
'<stl>3</stl>' \
'<blk>6</blk>' \
'<pf>24</pf>' \
'<pts>85</pts>' \
'</teamTotals>' \
'</boxscore>' \
'<ratings>' \
'<outsideScoring>7.6</outsideScoring>' \
'<insideScoring>6</insideScoring>' \
'<outsideDefense>5.6</outsideDefense>' \
'<insideDefense>7.3</insideDefense>' \
'<rebounding>5.3</rebounding>' \
'<offensiveFlow>5</offensiveFlow>' \
'</ratings>' \
'<efficiency>' \
'<PG>105.3</PG>' \
'<SG>110.8</SG>' \
'<SF>99.2</SF>' \
'<PF>95.7</PF>' \
'<C>86.6</C>' \
'</efficiency>' \
'<gdp>' \
'<focus>Inside.miss</focus>' \
'<pace>N/A</pace>' \
'</gdp>' \
'</awayTeam>' \
'<homeTeam id="58420">' \
'<teamname>Ethereum Traders</teamname>' \
'<shortname>ETH</shortname>' \
'<score partials="29,19,20,29">97</score>' \
'<offStrategy>Patient</offStrategy>' \
'<defStrategy>23Zone</defStrategy>' \
'<effort>normal</effort>' \
'<boxscore>' \
'<player id="27709839">' \
'<firstname>Miloš</firstname>' \
'<lastname>Ilić</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>32</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>5</fgm>' \
'<fga>16</fga>' \
'<tpm>2</tpm>' \
'<tpa>7</tpa>' \
'<ftm>7</ftm>' \
'<fta>10</fta>' \
'<oreb>0</oreb>' \
'<reb>3</reb>' \
'<ast>5</ast>' \
'<to>2</to>' \
'<stl>2</stl>' \
'<blk>0</blk>' \
'<pf>3</pf>' \
'<pts>19</pts>' \
'<rating>11.5</rating>' \
'</performance>' \
'</player>' \
'<player id="30218918">' \
'<firstname>Adolfs</firstname>' \
'<lastname>Biezums</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>31</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>3</fgm>' \
'<fga>5</fga>' \
'<tpm>0</tpm>' \
'<tpa>0</tpa>' \
'<ftm>1</ftm>' \
'<fta>2</fta>' \
'<oreb>1</oreb>' \
'<reb>2</reb>' \
'<ast>5</ast>' \
'<to>2</to>' \
'<stl>0</stl>' \
'<blk>0</blk>' \
'<pf>0</pf>' \
'<pts>7</pts>' \
'<rating>9.5</rating>' \
'</performance>' \
'</player>' \
'<player id="31837161">' \
'<firstname>Carlos</firstname>' \
'<lastname>Rubio La Fuente</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>16</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>3</fgm>' \
'<fga>5</fga>' \
'<tpm>2</tpm>' \
'<tpa>2</tpa>' \
'<ftm>0</ftm>' \
'<fta>0</fta>' \
'<oreb>0</oreb>' \
'<reb>3</reb>' \
'<ast>3</ast>' \
'<to>0</to>' \
'<stl>0</stl>' \
'<blk>0</blk>' \
'<pf>0</pf>' \
'<pts>8</pts>' \
'<rating>11.5</rating>' \
'</performance>' \
'</player>' \
'<player id="32957585">' \
'<firstname>Ângelo</firstname>' \
'<lastname>Frazão</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>34</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>7</fgm>' \
'<fga>15</fga>' \
'<tpm>1</tpm>' \
'<tpa>2</tpa>' \
'<ftm>3</ftm>' \
'<fta>7</fta>' \
'<oreb>2</oreb>' \
'<reb>11</reb>' \
'<ast>1</ast>' \
'<to>0</to>' \
'<stl>1</stl>' \
'<blk>0</blk>' \
'<pf>3</pf>' \
'<pts>18</pts>' \
'<rating>11.5</rating>' \
'</performance>' \
'</player>' \
'<player id="32974535">' \
'<firstname>Valery</firstname>' \
'<lastname>Lisenko</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>15</C>' \
'</minutes>' \
'<performance>' \
'<fgm>0</fgm>' \
'<fga>2</fga>' \
'<tpm>0</tpm>' \
'<tpa>0</tpa>' \
'<ftm>0</ftm>' \
'<fta>0</fta>' \
'<oreb>3</oreb>' \
'<reb>8</reb>' \
'<ast>0</ast>' \
'<to>0</to>' \
'<stl>0</stl>' \
'<blk>2</blk>' \
'<pf>1</pf>' \
'<pts>0</pts>' \
'<rating>11</rating>' \
'</performance>' \
'</player>' \
'<player id="35033483">' \
'<firstname>Camilo</firstname>' \
'<lastname>Angel</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>0</fgm>' \
'<fga>0</fga>' \
'<tpm>0</tpm>' \
'<tpa>0</tpa>' \
'<ftm>0</ftm>' \
'<fta>0</fta>' \
'<oreb>0</oreb>' \
'<reb>0</reb>' \
'<ast>0</ast>' \
'<to>0</to>' \
'<stl>0</stl>' \
'<blk>0</blk>' \
'<pf>0</pf>' \
'<pts>0</pts>' \
'<rating>-100000</rating>' \
'<dnp/>' \
'</performance>' \
'</player>' \
'<player id="35521904">' \
'<firstname>Andrius</firstname>' \
'<lastname>Nerecionis</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>33</C>' \
'</minutes>' \
'<performance>' \
'<fgm>6</fgm>' \
'<fga>13</fga>' \
'<tpm>0</tpm>' \
'<tpa>0</tpa>' \
'<ftm>0</ftm>' \
'<fta>2</fta>' \
'<oreb>3</oreb>' \
'<reb>14</reb>' \
'<ast>0</ast>' \
'<to>0</to>' \
'<stl>1</stl>' \
'<blk>0</blk>' \
'<pf>0</pf>' \
'<pts>12</pts>' \
'<rating>12.5</rating>' \
'</performance>' \
'</player>' \
'<player id="43023368">' \
'<firstname>Fabián</firstname>' \
'<lastname>Adamčík</lastname>' \
'<minutes>' \
'<PG>32</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>7</fgm>' \
'<fga>21</fga>' \
'<tpm>1</tpm>' \
'<tpa>3</tpa>' \
'<ftm>4</ftm>' \
'<fta>6</fta>' \
'<oreb>1</oreb>' \
'<reb>2</reb>' \
'<ast>4</ast>' \
'<to>2</to>' \
'<stl>2</stl>' \
'<blk>0</blk>' \
'<pf>0</pf>' \
'<pts>19</pts>' \
'<rating>12</rating>' \
'</performance>' \
'</player>' \
'<player id="43109016">' \
'<firstname>Miloslav</firstname>' \
'<lastname>Kaprál</lastname>' \
'<minutes>' \
'<PG>16</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>1</fgm>' \
'<fga>3</fga>' \
'<tpm>0</tpm>' \
'<tpa>0</tpa>' \
'<ftm>0</ftm>' \
'<fta>0</fta>' \
'<oreb>0</oreb>' \
'<reb>1</reb>' \
'<ast>0</ast>' \
'<to>0</to>' \
'<stl>1</stl>' \
'<blk>0</blk>' \
'<pf>1</pf>' \
'<pts>2</pts>' \
'<rating>10</rating>' \
'</performance>' \
'</player>' \
'<player id="43916589">' \
'<firstname>Jakub</firstname>' \
'<lastname>Šlapka</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>0</SF>' \
'<PF>14</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>0</fgm>' \
'<fga>1</fga>' \
'<tpm>0</tpm>' \
'<tpa>0</tpa>' \
'<ftm>0</ftm>' \
'<fta>0</fta>' \
'<oreb>0</oreb>' \
'<reb>5</reb>' \
'<ast>1</ast>' \
'<to>0</to>' \
'<stl>1</stl>' \
'<blk>0</blk>' \
'<pf>0</pf>' \
'<pts>0</pts>' \
'<rating>9</rating>' \
'</performance>' \
'</player>' \
'<player id="43919669">' \
'<firstname>Borimír</firstname>' \
'<lastname>Bulejka</lastname>' \
'<minutes>' \
'<PG>0</PG>' \
'<SG>0</SG>' \
'<SF>17</SF>' \
'<PF>0</PF>' \
'<C>0</C>' \
'</minutes>' \
'<performance>' \
'<fgm>4</fgm>' \
'<fga>8</fga>' \
'<tpm>1</tpm>' \
'<tpa>2</tpa>' \
'<ftm>3</ftm>' \
'<fta>4</fta>' \
'<oreb>0</oreb>' \
'<reb>4</reb>' \
'<ast>1</ast>' \
'<to>1</to>' \
'<stl>0</stl>' \
'<blk>0</blk>' \
'<pf>1</pf>' \
'<pts>12</pts>' \
'<rating>10</rating>' \
'</performance>' \
'</player>' \
'<teamTotals>' \
'<fgm>36</fgm>' \
'<fga>89</fga>' \
'<tpm>7</tpm>' \
'<tpa>16</tpa>' \
'<ftm>18</ftm>' \
'<fta>31</fta>' \
'<oreb>10</oreb>' \
'<reb>53</reb>' \
'<ast>20</ast>' \
'<to>7</to>' \
'<stl>8</stl>' \
'<blk>2</blk>' \
'<pf>9</pf>' \
'<pts>97</pts>' \
'</teamTotals>' \
'</boxscore>' \
'<ratings>' \
'<outsideScoring>6.6</outsideScoring>' \
'<insideScoring>7</insideScoring>' \
'<outsideDefense>5.6</outsideDefense>' \
'<insideDefense>9.3</insideDefense>' \
'<rebounding>7.6</rebounding>' \
'<offensiveFlow>5.6</offensiveFlow>' \
'</ratings>' \
'<efficiency>' \
'<PG>107.1</PG>' \
'<SG>115</SG>' \
'<SF>86.1</SF>' \
'<PF>125</PF>' \
'<C>114.4</C>' \
'</efficiency>' \
'<gdp>' \
'<focus>N/A</focus>' \
'<pace>Fast.hit</pace>' \
'</gdp>' \
'</homeTeam>' \
'</match>' \
'</bbapi>'
