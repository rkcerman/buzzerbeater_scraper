BOXSCORE_MOCK_DICT = {
    1: {
        'match_id': 1234,
        'qtr' : 1,
        'away_team_score': 21,
        'home_team_score': 17
    },
    2: {
        'match_id': 1234,
        'qtr' : 2,
        'away_team_score': 19,
        'home_team_score': 29
    },
    3: {
        'match_id': 1234,
        'qtr' : 3,
        'away_team_score': 16,
        'home_team_score': 21
    },
    4: {
        'match_id': 1234,
        'qtr' : 4,
        'away_team_score': 27,
        'home_team_score': 31
    }
}

MOCK_BOXSCORE_DIV = '<div id="ctl00_cphContent_pnlBoxScore">' \
                    '<div style="text-align: center;">' \
                    '        <span style="font-weight:bold;">Match Result</span>' \
                    '    </div>' \
                    '    <table style="margin: auto;">' \
                    '        <tr class="tableheader">' \
                    '            <td>' \
                    '                Final' \
                    '            </td>' \
                    '' \
                    '            <td style="width: 30px; text-align: right;">' \
                    '                1' \
                    '            </td>' \
                    '' \
                    '            <td style="width: 30px; text-align: right;">' \
                    '                2' \
                    '            </td>' \
                    '' \
                    '            <td style="width: 30px; text-align: right;">' \
                    '                3' \
                    '            </td>' \
                    '' \
                    '            <td style="width: 30px; text-align: right;">' \
                    '                4' \
                    '            </td>' \
                    '' \
                    '            <td style="width: 30px; text-align: right;">' \
                    '                Total' \
                    '            </td>' \
                    '        </tr>' \
                    '        <tr>' \
                    '            <td>' \
                    '                <a id="ctl00_cphContent_bsResult_hlAwayTeamLink" href="../../team/58420/overview.aspx">Ethereum Traders</a>' \
                    '            </td>' \
                    '' \
                    '            <td style="text-align: right;">' \
                    '                21' \
                    '            </td>' \
                    '' \
                    '            <td style="text-align: right;">' \
                    '                19' \
                    '            </td>' \
                    '' \
                    '            <td style="text-align: right;">' \
                    '                16' \
                    '            </td>' \
                    '' \
                    '            <td style="text-align: right;">' \
                    '                27' \
                    '            </td>' \
                    '' \
                    '            <td style="text-align: right;">' \
                    '                <strong>83</strong>' \
                    '            </td>' \
                    '        </tr>' \
                    '        <tr>' \
                    '            <td>' \
                    '                <a id="ctl00_cphContent_bsResult_hlHomeTeamLink" href="../../team/58377/overview.aspx">BK sever 5</a>' \
                    '            </td>' \
                    '' \
                    '            <td style="text-align: right;">' \
                    '                17' \
                    '            </td>' \
                    '' \
                    '            <td style="text-align: right;">' \
                    '                29' \
                    '            </td>' \
                    '' \
                    '            <td style="text-align: right;">' \
                    '                21' \
                    '            </td>' \
                    '' \
                    '            <td style="text-align: right;">' \
                    '                31' \
                    '            </td>' \
                    '' \
                    '            <td style="text-align: right;">' \
                    '                <strong>98</strong>' \
                    '            </td>' \
                    '        </tr>' \
                    '    </table>' \
                    '    <hr width="99%" align="left" />' \
                    '' \
                    '    <table style="margin: auto;">' \
                    '        <tr>' \
                    '            <td style="text-align: right;">' \
                    '                <img id="ctl00_cphContent_BSMTR_imgAwayJersey" src="../../images/jerseys/3.gif" style="height:48px;width:17px;border-width:0px;float: left; padding-right: 10px" />' \
                    '            </td>' \
                    '            <td style="vertical-align:middle">' \
                    '                <a id="ctl00_cphContent_BSMTR_hlAwayTeamLink" href="../../team/58420/overview.aspx">Ethereum Traders</a>' \
                    '            </td>' \
                    '            <td style="text-align: center; font-weight: bold; padding-left: 20px; padding-right: 20px;">' \
                    '                Team Ratings' \
                    '            </td>' \
                    '            <td style="vertical-align:middle">' \
                    '                <a id="ctl00_cphContent_BSMTR_hlHomeTeamLink" href="../../team/58377/overview.aspx">BK sever 5</a>' \
                    '            </td>' \
                    '            <td>' \
                    '                <img id="ctl00_cphContent_BSMTR_imgHomeJersey" src="../../images/jerseys/1.gif" style="height:48px;width:17px;border-width:0px;padding-right: 10px; padding-left: 6px" />' \
                    '            </td>' \
                    '        </tr>' \
                    '        <tr>' \
                    '            <td colspan="5">' \
                    '                &nbsp;' \
                    '            </td>' \
                    '        </tr>' \
                    '        <tr>' \
                    '            <td colspan="2" style="text-align: right;">' \
                    '                Push the Ball' \
                    '            </td>' \
                    '            <td style="text-align: center; font-weight: bold; padding-left: 20px; padding-right: 20px;">' \
                    '                Offensive Strategy' \
                    '            </td>' \
                    '            <td colspan="2">' \
                    '                Push the Ball' \
                    '            </td>' \
                    '        </tr>' \
                    '        <tr>' \
                    '            <td colspan="2" style="text-align: right;">' \
                    '                Man to Man' \
                    '            </td>' \
                    '            <td style="text-align: center; font-weight: bold; padding-left: 20px; padding-right: 20px;">' \
                    '                Defensive Strategy' \
                    '            </td>' \
                    '            <td colspan="2">' \
                    '                Man to Man' \
                    '            </td>' \
                    '        </tr>' \
                    '        <tr>' \
                    '            <td colspan="5">' \
                    '                &nbsp;' \
                    '            </td>' \
                    '        </tr>' \
                    '        <tr id="ctl00_cphContent_BSMTR_trGDP1">' \
                    '            <td colspan="2">' \
                    '            </td>' \
                    '            <td style="text-align: center; font-weight: bold; padding-left: 20px; padding-right: 20px;">' \
                    '                Game-Day Prep' \
                    '            </td>' \
                    '            <td colspan="2">' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_BSMTR_trGDP2">' \
                    '            <td colspan="2" style="text-align: right;">' \
                    '                --' \
                    '            </td>' \
                    '            <td style="text-align: center; font-weight: bold; padding-left: 20px; padding-right: 20px;">' \
                    '                Focus' \
                    '            </td>' \
                    '            <td colspan="2">' \
                    '                --' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_BSMTR_trGDP3">' \
                    '            <td colspan="2" style="text-align: right;">' \
                    '                Fast<img id="ctl00_cphContent_BSMTR_imgPaceA" src="/images/icons/icon_online.png" style="border-width:0px;padding-left: 3px;" />' \
                    '            </td>' \
                    '            <td style="text-align: center; font-weight: bold; padding-left: 20px; padding-right: 20px;">' \
                    '                Pace' \
                    '            </td>' \
                    '            <td colspan="2">' \
                    '                --' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_BSMTR_trGDPSpacer">' \
                    '            <td colspan="5">' \
                    '                &nbsp;' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr>' \
                    '            <td colspan="2" style="text-align: right;">' \
                    '                <a id="ctl00_cphContent_BSMTR_OutScoreAway_linkDen" class="lev8" title="8" href="../../community/rules.aspx?nav=Nomenclature">strong (low)</a>' \
                    '            </td>' \
                    '            <td style="text-align: center; font-weight: bold; padding-left: 20px; padding-right: 20px;">' \
                    '                Outside Scoring' \
                    '            </td>' \
                    '            <td colspan="2">' \
                    '                <a id="ctl00_cphContent_BSMTR_OutScoreHome_linkDen" class="lev7" title="7" href="../../community/rules.aspx?nav=Nomenclature">respectable (low)</a>' \
                    '            </td>' \
                    '        </tr>' \
                    '        <tr>' \
                    '            <td colspan="2" style="text-align: right;">' \
                    '                <a id="ctl00_cphContent_BSMTR_InScoreAway_linkDen" class="lev7" title="7" href="../../community/rules.aspx?nav=Nomenclature">respectable (low)</a>' \
                    '            </td>' \
                    '            <td style="text-align: center; font-weight: bold; padding-left: 20px; padding-right: 20px;">' \
                    '                Inside Scoring' \
                    '            </td>' \
                    '            <td colspan="2">' \
                    '                <a id="ctl00_cphContent_BSMTR_InScoreHome_linkDen" class="lev8" title="8" href="../../community/rules.aspx?nav=Nomenclature">strong (high)</a>' \
                    '            </td>' \
                    '        </tr>' \
                    '        <tr>' \
                    '            <td colspan="2" style="text-align: right;">' \
                    '                <a id="ctl00_cphContent_BSMTR_OutDefAway_linkDen" class="lev9" title="9" href="../../community/rules.aspx?nav=Nomenclature">proficient (medium)</a>' \
                    '            </td>' \
                    '            <td style="text-align: center; font-weight: bold; padding-left: 20px; padding-right: 20px;">' \
                    '                Perimeter Defense' \
                    '            </td>' \
                    '            <td colspan="2">' \
                    '                <a id="ctl00_cphContent_BSMTR_OutDefHome_linkDen" class="lev8" title="8" href="../../community/rules.aspx?nav=Nomenclature">strong (low)</a>' \
                    '            </td>' \
                    '        </tr>' \
                    '        <tr>' \
                    '            <td colspan="2" style="text-align: right;">' \
                    '                <a id="ctl00_cphContent_BSMTR_InDefAway_linkDen" class="lev9" title="9" href="../../community/rules.aspx?nav=Nomenclature">proficient (low)</a>' \
                    '            </td>' \
                    '            <td style="text-align: center; font-weight: bold; padding-left: 20px; padding-right: 20px;">' \
                    '                Inside Defense' \
                    '            </td>' \
                    '            <td colspan="2">' \
                    '                <a id="ctl00_cphContent_BSMTR_InDefHome_linkDen" class="lev9" title="9" href="../../community/rules.aspx?nav=Nomenclature">proficient (medium)</a>' \
                    '            </td>' \
                    '        </tr>' \
                    '        <tr>' \
                    '            <td colspan="2" style="text-align: right;">' \
                    '                <a id="ctl00_cphContent_BSMTR_ReboundAway_linkDen" class="lev7" title="7" href="../../community/rules.aspx?nav=Nomenclature">respectable (low)</a>' \
                    '            </td>' \
                    '            <td style="text-align: center; font-weight: bold; padding-left: 20px; padding-right: 20px;">' \
                    '                Rebounding' \
                    '            </td>' \
                    '            <td colspan="2">' \
                    '                <a id="ctl00_cphContent_BSMTR_ReboundHome_linkDen" class="lev8" title="8" href="../../community/rules.aspx?nav=Nomenclature">strong (low)</a>' \
                    '            </td>' \
                    '        </tr>' \
                    '        <tr>' \
                    '            <td colspan="2" style="text-align: right;">' \
                    '                <a id="ctl00_cphContent_BSMTR_OffFlowAway_linkDen" class="lev7" title="7" href="../../community/rules.aspx?nav=Nomenclature">respectable (medium)</a>' \
                    '            </td>' \
                    '            <td style="text-align: center; font-weight: bold; padding-left: 20px; padding-right: 20px;">' \
                    '                Offensive Flow' \
                    '            </td>' \
                    '            <td colspan="2">' \
                    '                <a id="ctl00_cphContent_BSMTR_OffFlowHome_linkDen" class="lev6" title="6" href="../../community/rules.aspx?nav=Nomenclature">average (high)</a>' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr>' \
                    '            <td colspan="5">' \
                    '                &nbsp;' \
                    '            </td>' \
                    '        </tr>' \
                    '        <div id="ctl00_cphContent_BSMTR_pnlMatchupRatings">' \
                    '' \
                    '            <tr>' \
                    '                <td colspan="5" style="text-align: center;">' \
                    '                    <span id="ctl00_cphContent_BSMTR_Label1" style="font-weight:bold;">Matchup Ratings</span>' \
                    '                </td>' \
                    '            </tr>' \
                    '            <tr class="tableheader">' \
                    '                <td colspan="2" style="text-align: right; width: 160px;">' \
                    '                    Points per 100 Shots' \
                    '                </td>' \
                    '                <td style="text-align: center;">' \
                    '                    Position' \
                    '                </td>' \
                    '                <td colspan="2" style="width: 160px;">' \
                    '                    Points per 100 Shots' \
                    '                </td>' \
                    '            </tr>' \
                    '            <tr>' \
                    '                <td colspan="2" style="padding: 0px; vertical-align: middle; text-align: right;">' \
                    '                    <div style="float: right;">' \
                    '                        <img alt="82.2" style="padding: 0;" src="/images/rating_left.gif" /><img alt="82.2" style="padding: 0;" width="76px" height="16px" src="/images/rating_bar.gif" /><img alt="82.2" src="/images/rating_right.gif" />' \
                    '                    </div>' \
                    '                    <div style="font-weight: bold;">82.2&nbsp;</div>' \
                    '                </td>' \
                    '                <td style="text-align: center;">' \
                    '                    as PG' \
                    '                </td>' \
                    '                <td colspan="2" style="padding: 0px; vertical-align: middle">' \
                    '                    <div style="float: left;">' \
                    '                        <img alt="103.2" style="padding: 0;" src="/images/rating_left.gif" /><img alt="103.2" style="padding: 0;" width="95px" height="16px" src="/images/rating_bar.gif" /><img alt="103.2" src="/images/rating_right.gif" />' \
                    '                    </div>' \
                    '                    <div style="font-weight: bold;">103.2</div>' \
                    '                </td>' \
                    '            </tr>' \
                    '            <tr>' \
                    '                <td colspan="2" style="padding: 0px; vertical-align: middle; text-align: right;">' \
                    '                    <div style="float: right;">' \
                    '                        <img alt="88.0" style="padding: 0;" src="/images/rating_left.gif" /><img alt="88.0" style="padding: 0;" width="81px" height="16px" src="/images/rating_bar.gif" /><img alt="88.0" src="/images/rating_right.gif" />' \
                    '                    </div>' \
                    '                    <div style="font-weight: bold;">88.0&nbsp;</div>' \
                    '                </td>' \
                    '                <td style="text-align: center;">' \
                    '                    as SG' \
                    '                </td>' \
                    '                <td colspan="2" style="padding: 0px; vertical-align: middle">' \
                    '                    <div style="float: left;">' \
                    '                        <img alt="90.3" style="padding: 0;" src="/images/rating_left.gif" /><img alt="90.3" style="padding: 0;" width="83px" height="16px" src="/images/rating_bar.gif" /><img alt="90.3" src="/images/rating_right.gif" />' \
                    '                    </div>' \
                    '                    <div style="font-weight: bold;">90.3</div>' \
                    '                </td>' \
                    '            </tr>' \
                    '            <tr>' \
                    '                <td colspan="2" style="padding: 0px; vertical-align: middle; text-align: right;">' \
                    '                    <div style="float: right;">' \
                    '                        <img alt="62.4" style="padding: 0;" src="/images/rating_left.gif" /><img alt="62.4" style="padding: 0;" width="58px" height="16px" src="/images/rating_bar.gif" /><img alt="62.4" src="/images/rating_right.gif" />' \
                    '                    </div>' \
                    '                    <div style="font-weight: bold;">62.4&nbsp;</div>' \
                    '                </td>' \
                    '                <td style="text-align: center;">' \
                    '                    as SF' \
                    '                </td>' \
                    '                <td colspan="2" style="padding: 0px; vertical-align: middle">' \
                    '                    <div style="float: left;">' \
                    '                        <img alt="102.6" style="padding: 0;" src="/images/rating_left.gif" /><img alt="102.6" style="padding: 0;" width="95px" height="16px" src="/images/rating_bar.gif" /><img alt="102.6" src="/images/rating_right.gif" />' \
                    '                    </div>' \
                    '                    <div style="font-weight: bold;">102.6</div>' \
                    '                </td>' \
                    '            </tr>' \
                    '            <tr>' \
                    '                <td colspan="2" style="padding: 0px; vertical-align: middle; text-align: right;">' \
                    '                    <div style="float: right;">' \
                    '                        <img alt="98.5" style="padding: 0;" src="/images/rating_left.gif" /><img alt="98.5" style="padding: 0;" width="91px" height="16px" src="/images/rating_bar.gif" /><img alt="98.5" src="/images/rating_right.gif" />' \
                    '                    </div>' \
                    '                    <div style="font-weight: bold;">98.5&nbsp;</div>' \
                    '                </td>' \
                    '                <td style="text-align: center;">' \
                    '                    as PF' \
                    '                </td>' \
                    '                <td colspan="2" style="padding: 0px; vertical-align: middle">' \
                    '                    <div style="float: left;">' \
                    '                        <img alt="77.7" style="padding: 0;" src="/images/rating_left.gif" /><img alt="77.7" style="padding: 0;" width="72px" height="16px" src="/images/rating_bar.gif" /><img alt="77.7" src="/images/rating_right.gif" />' \
                    '                    </div>' \
                    '                    <div style="font-weight: bold;">77.7</div>' \
                    '                </td>' \
                    '            </tr>' \
                    '            <tr>' \
                    '                <td colspan="2" style="padding: 0px; vertical-align: middle; text-align: right;">' \
                    '                    <div style="float: right;">' \
                    '                        <img alt="108.5" style="padding: 0;" src="/images/rating_left.gif" /><img alt="108.5" style="padding: 0;" width="100px" height="16px" src="/images/rating_bar.gif" /><img alt="108.5" src="/images/rating_right.gif" />' \
                    '                    </div>' \
                    '                    <div style="font-weight: bold;">108.5&nbsp;</div>' \
                    '                </td>' \
                    '                <td style="text-align: center;">' \
                    '                    as C' \
                    '                </td>' \
                    '                <td colspan="2" style="padding: 0px; vertical-align: middle">' \
                    '                    <div style="float: left;">' \
                    '                        <img alt="102.2" style="padding: 0;" src="/images/rating_left.gif" /><img alt="102.2" style="padding: 0;" width="94px" height="16px" src="/images/rating_bar.gif" /><img alt="102.2" src="/images/rating_right.gif" />' \
                    '                    </div>' \
                    '                    <div style="font-weight: bold;">102.2</div>' \
                    '                </td>' \
                    '            </tr>' \
                    '' \
                    '        </div>' \
                    '' \
                    '    </table>' \
                    '    <br />' \
                    '' \
                    '    <div style="text-align: center;">' \
                    '        <span id="ctl00_cphContent_lblTeamEffort">Your team effort for this game: Playoff Crunch Time</span>' \
                    '        <br />' \
                    '        <span id="ctl00_cphContent_lblEffort">Both teams played at the same effort level.</span>' \
                    '    </div>' \
                    '    <hr width="99%" align="left" />' \
                    '' \
                    '    <div style="text-align: center;">' \
                    '        <span style="font-weight:normal;">Stats</span>' \
                    '    </div>' \
                    '' \
                    '    <table border="0" cellpadding="1" cellspacing="1" width="99%">' \
                    '        <tr class="tableheader">' \
                    '            <td align="left" colspan="2" valign="top">' \
                    '                Ethereum Traders' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Minutes played">MIN</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Total Field Goals (2FG + 3FG)">FG</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Three Point Field Goals">3FG</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Free Throws">FT</span></td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_tdTop" align="center" valign="top">' \
                    '                <span id="ctl00_cphContent_awayTeamBoxScore_Label1">+/-</span></td>' \
                    '' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Offensive Rebounds">OR</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Total Rebounds (OR + DR)">TR</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Assists">AST</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Turnovers">TO</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Steals">STL</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Blocks">BLK</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Fouls">PF</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Points">PTS</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Player Rating">RTNG</span></td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tr">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                C' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/35521904/overview.aspx" style="font-weight: bold;">' \
                    '                    A. Nerecionis' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                36' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>6 - 16</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 1</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>8 - 8</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                -22' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                5' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                17' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                20' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl01_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                15.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tr" bgcolor="#EEEEEE">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                PF' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/32957585/overview.aspx" style="font-weight: bold;">' \
                    '                    Â. Frazão' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                35' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>7 - 18</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>1 - 3</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>2 - 6</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                -14' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                7' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                16' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                17' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl02_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                13.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tr">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                SG' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/27709839/overview.aspx" style="font-weight: bold;">' \
                    '                    M. Ilić' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                40' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>6 - 26</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>1 - 8</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>2 - 2</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                -19' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                5' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                6' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                15' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl03_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                11.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tr" bgcolor="#EEEEEE">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                PG' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/43023368/overview.aspx" style="font-weight: bold;">' \
                    '                    F. Adamčík' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                37' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>3 - 13</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 4</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>5 - 6</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                -15' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                6' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                11' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl04_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                14.5' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tr">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                PG' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/43109016/overview.aspx" style="">' \
                    '                    M. Kaprál' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                20' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>4 - 10</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 2</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 0</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                +4' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                7' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                8' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl05_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                14.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tr" bgcolor="#EEEEEE">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                PF' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/43919669/overview.aspx" style="">' \
                    '                    B. Bulejka' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                13' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>2 - 6</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 2</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>2 - 2</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                -3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                4' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                6' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl06_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                12.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tr">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                C' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/32974535/overview.aspx" style="">' \
                    '                    V. Lisenko' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                12' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>2 - 3</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 0</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 0</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                +7' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                4' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl07_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                12.5' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tr" bgcolor="#EEEEEE">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                SF' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/31837161/overview.aspx" style="font-weight: bold;">' \
                    '                    C. Rubio La Fuente' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                35' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>1 - 10</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 4</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 0</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                -19' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                7' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl08_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                9.5' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tr">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                SF' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/30218918/overview.aspx" style="">' \
                    '                    A. Biezums' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                13' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 2</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 1</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 0</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                +6' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                4' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_Repeater1_ctl09_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                11.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr class="headline">' \
                    '            <td align="left" colspan="2" valign="top">' \
                    '                Ethereum Traders' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                <nobr>31 - 104</nobr>' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                <nobr>2 - 25</nobr>' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                <nobr>19 - 24</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_tdTotalPlusMinus">&nbsp;</td>' \
                    '' \
                    '            <td align="center" valign="top">' \
                    '                19' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                60' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                19' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                12' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                6' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                7' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                19' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                83' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_awayTeamBoxScore_tdBottom" align="center" valign="top">' \
                    '            </td>' \
                    '' \
                    '            <td align="center" valign="top">' \
                    '            </td>' \
                    '        </tr>' \
                    '    </table>' \
                    '' \
                    '    <br />' \
                    '' \
                    '    <table border="0" cellpadding="1" cellspacing="1" width="99%">' \
                    '        <tr class="tableheader">' \
                    '            <td align="left" colspan="2" valign="top">' \
                    '                BK sever 5' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Minutes played">MIN</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Total Field Goals (2FG + 3FG)">FG</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Three Point Field Goals">3FG</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Free Throws">FT</span></td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_tdTop" align="center" valign="top">' \
                    '                <span id="ctl00_cphContent_homeTeamBoxScore_Label1">+/-</span></td>' \
                    '' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Offensive Rebounds">OR</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Total Rebounds (OR + DR)">TR</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Assists">AST</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Turnovers">TO</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Steals">STL</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Blocks">BLK</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Fouls">PF</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Points">PTS</span></td>' \
                    '            <td align="center" valign="top">' \
                    '                <span title="Player Rating">RTNG</span></td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tr">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                SG' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/36218011/overview.aspx" style="font-weight: bold;">' \
                    '                    G. Geay' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                30' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>6 - 13</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 5</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>8 - 8</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                +28' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                5' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                20' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl01_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                12.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tr" bgcolor="#EEEEEE">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                C' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/36877385/overview.aspx" style="font-weight: bold;">' \
                    '                    H. Nazgul' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                36' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>8 - 19</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>1 - 3</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 0</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                +16' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                4' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                13' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                5' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                17' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl02_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                15.5' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tr">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                SG' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/39156549/overview.aspx" style="">' \
                    '                    A. Acosta' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                18' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>6 - 16</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>1 - 4</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>2 - 2</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                -13' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                15' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl03_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                15.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tr" bgcolor="#EEEEEE">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                SF' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/39388729/overview.aspx" style="font-weight: bold;">' \
                    '                    A. Minart' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                36' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>5 - 9</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 0</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 0</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                +19' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                4' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                10' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl04_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                11.5' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tr">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                PG' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/36894298/overview.aspx" style="font-weight: bold;">' \
                    '                    M. Miró' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                36' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>3 - 9</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 1</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>4 - 8</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                +16' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                7' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                6' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                4' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                10' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl05_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                12.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tr" bgcolor="#EEEEEE">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                PF' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/28668697/overview.aspx" style="font-weight: bold;">' \
                    '                    F. Le Goff' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                26' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>3 - 9</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 1</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>2 - 2</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                +14' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                14' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                8' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl06_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                14.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tr">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                C' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/40921645/overview.aspx" style="">' \
                    '                    P. Belengué' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                12' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>3 - 6</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 0</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 0</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                -1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                4' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                6' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl07_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                15.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tr" bgcolor="#EEEEEE">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                PF' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/39786791/overview.aspx" style="">' \
                    '                    E. Steward' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                22' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>1 - 4</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 0</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>3 - 4</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                +1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                7' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                5' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl08_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                14.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tr">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                SF' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/35115556/overview.aspx" style="">' \
                    '                    C. Harris' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                12' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>2 - 7</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 3</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>1 - 2</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                -4' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                3' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                5' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl09_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                13.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tr" bgcolor="#EEEEEE">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '                PG' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/41525134/overview.aspx" style="">' \
                    '                    P. Hraška' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdMinutes" style="width: 25px" align="center" valign="top">' \
                    '                12' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdFG" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>1 - 4</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_td3pts" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 1</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdFT" style="width: 50px" align="center" valign="top">' \
                    '                <nobr>0 - 0</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdPlusMinus" style="width: 25px" align="center" valign="top">' \
                    '                -1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdOffReb" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdTotReb" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdAssists" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdTO" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdSteals" style="width: 25px" align="center" valign="top">' \
                    '                0' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdBlocks" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdFouls" style="width: 25px" align="center" valign="top">' \
                    '                1' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdPoints" style="width: 25px" align="center" valign="top">' \
                    '                2' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl10_tdRating" style="width: 50px" align="center" valign="top">' \
                    '                11.0' \
                    '            </td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl11_tr">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/42239973/overview.aspx" style="">' \
                    '                    E. Kašinský' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl11_tdDNP" colspan="14" align="center" valign="top">' \
                    '                Did Not Play - Coachs Decision</td>' \
                    '        </tr>' \
                    '' \
                    '        <tr id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl12_tr" bgcolor="#EEEEEE">' \
                    '            <td style="width: 20px; font-weight: bold;" valign="top">' \
                    '' \
                    '            </td>' \
                    '            <td style="width: 160px;" align="left" valign="top">' \
                    '                <a href="/player/44606688/overview.aspx" style="">' \
                    '                    M. Vojtkuliak' \
                    '                </a>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_Repeater1_ctl12_tdDNP" colspan="14" align="center" valign="top">' \
                    '                Did Not Play - Coachs Decision</td>' \
                    '        </tr>' \
                    '' \
                    '        <tr class="headline">' \
                    '            <td align="left" colspan="2" valign="top">' \
                    '                BK sever 5' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                <nobr>38 - 96</nobr>' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                <nobr>2 - 18</nobr>' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                <nobr>20 - 26</nobr>' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_tdTotalPlusMinus">&nbsp;</td>' \
                    '' \
                    '            <td align="center" valign="top">' \
                    '                16' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                59' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                19' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                9' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                5' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                12' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                16' \
                    '            </td>' \
                    '            <td align="center" valign="top">' \
                    '                98' \
                    '            </td>' \
                    '            <td id="ctl00_cphContent_homeTeamBoxScore_tdBottom" align="center" valign="top">' \
                    '            </td>' \
                    '' \
                    '            <td align="center" valign="top">' \
                    '            </td>' \
                    '        </tr>' \
                    '    </table>' \
                    '' \
                    '    <hr width="99%" align="left" />' \
                    '' \
                    '    <span id="ctl00_cphContent_lblMatchType1" style="font-weight:bold;">Match Type:</span>&nbsp;' \
                    '    <span id="ctl00_cphContent_lblMatchType2">League Playoff Game</span>' \
                    '    <br />' \
                    '' \
                    '    <span id="ctl00_cphContent_lblArena1" style="font-weight:bold;">Arena:</span>&nbsp;' \
                    '    <a id="ctl00_cphContent_hlArena" href="../../team/58377/arena.aspx">Liptov arena</a>&nbsp;' \
                    '' \
                    '    <br />' \
                    '' \
                    '    <span id="ctl00_cphContent_lblAttendance1" style="font-weight:bold;">Attendance:</span>&nbsp;' \
                    '    <span id="ctl00_cphContent_lblAttendance2">14756</span>' \
                    '    <br />' \
                    '' \
                    '    <span id="ctl00_cphContent_lblTimeOfGame1" style="font-weight:bold;">Time of Game:</span>&nbsp;' \
                    '    <span id="ctl00_cphContent_lblTimeOfGame2">1:46</span>' \
                    '' \
                    '</div>'
