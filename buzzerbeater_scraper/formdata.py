from buzzerbeater_scraper.config import BB_USERNAME, BB_PASSWORD, BB_API_PASSWORD

BB_LOGIN = {
    'ctl00$txtLoginName': BB_USERNAME,
    'ctl00$txtPassword': BB_PASSWORD
}

BB_API_LOGIN = {
    'login': BB_USERNAME,
    'code': BB_API_PASSWORD
}

BB_TRANSFER_SEARCH_FORMDATA = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    'ctl00$hdnNetlogLang': '',
    'ctl00$myURL': 'http://www.buzzerbeater.com/manage/transferlist.aspx',
    'ctl00$tbCurrentPageName': 'Link Name',
    'ctl00$tbCustomLinkText': 'Link Name',
    'ctl00$tbCustomLinkURL': 'Link URL',
    'ctl00$cphContent$ddlSkill1': '0',
    'ctl00$cphContent$ddlSkill2': '0',
    'ctl00$cphContent$ddlSkill3': '0',
    'ctl00$cphContent$ddlSkill4': '0',
    'ctl00$cphContent$ddlSkill5': '0',
    'ctl00$cphContent$ddlSkill6': '0',
    'ctl00$cphContent$ddlSkill7': '0',
    'ctl00$cphContent$ddlSkill8': '0',
    'ctl00$cphContent$tbMinAge': '',
    'ctl00$cphContent$tbMaxAge': '',
    'ctl00$cphContent$tbMinSalary': '',
    'ctl00$cphContent$tbMaxSalary': '',
    'ctl00$cphContent$tbMinCurrentBid': '',
    'ctl00$cphContent$tbMaxCurrentBid': '',
    'ctl00$cphContent$ddlHeightMin': '0',
    'ctl00$cphContent$ddlHeightMax': '0',
    'ctl00$cphContent$ddlPotentialMin': '0',
    'ctl00$cphContent$ddlPotentialMax': '0',
    'ctl00$cphContent$ddlExperienceMin': '0',
    'ctl00$cphContent$ddlExperienceMax': '0',
    'ctl00$cphContent$ddlGameShapeMin': '0',
    'ctl00$cphContent$ddlGameShapeMax': '0',
    'ctl00$cphContent$ddlCountry': '0',
    'ctl00$cphContent$ddlInjury1': '0',
    'ctl00$cphContent$tbGuardSkillPoints': '',
    'ctl00$cphContent$tbMaxGuardSkillPoints': '',
    'ctl00$cphContent$tbForwardSkillPoints': '',
    'ctl00$cphContent$tbMaxForwardSkillPoints': '',
    'ctl00$cphContent$tbTotalSkillPoints': '',
    'ctl00$cphContent$tbMaxTotalSkillPoints': '',
    'ctl00$cphContent$ddlBestposition': '0',
    'ctl00$cphContent$ddlBestposition2': '0',
    'ctl00$cphContent$ddlsortBy': '1',
    'ctl00$cphContent$btnSearch': 'Search',
    'ctl00$cphContent$tbNewLabel': ''
}

BB_TRANSFER_NEXT_PAGE_FORMDATA = {
    '__EVENTTARGET': '',
    '__EVENTARGUMENT': '',
    'ctl00$hdnNetlogLang': '',
    'ctl00$myURL': 'http://www.buzzerbeater.com/manage/transferlist.aspx',
    'ctl00$tbCurrentPageName': 'Link Name',
    'ctl00$tbCustomLinkText': 'Link Name',
    'ctl00$tbCustomLinkURL': 'Link URL',
    'ctl00$cphContent$btnNextPage': 'Next Page',
    'ctl00$cphContent$hdnTotalPages': '100',
    'ctl00$cphContent$hdnTotalResults': '1000',
    'ctl00$cphContent$hdnSearchParams': '',
    'ctl00$cphContent$hdnSortBy': '1',
    'ctl00$cphContent$hdnPlayerCompare': '0'
}
