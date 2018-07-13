import scrapy
import re
from datetime import datetime
from bs4 import BeautifulSoup
from scrapy import FormRequest

from buzzerbeater_scraper.items import PlayerItem, PlayerSkillsItem, TeamItem, PlayerHistoryItem
from buzzerbeater_scraper.formdata import BB_LOGIN, BB_TRANSFER_SEARCH_FORMDATA, BB_TRANSFER_NEXT_PAGE_FORMDATA


class BuzzerbeaterTransfersSpider(scrapy.Spider):
    transfer_list_page = 0
    name = "transfers_spider"
    allowed_domains = ["buzzerbeater.com"]
    start_urls = (
        'http://www.buzzerbeater.com/default.aspx',
    )
    urls = [
        'http://www.buzzerbeater.com/manage/transferlist.aspx',
    ]

    def parse(self, response):
        # Opening a login request
        return scrapy.FormRequest.from_response(
            response,
            formdata=BB_LOGIN,
            callback=self.after_login
        )

    def after_login(self, response):
        # Check login succeed before going on
        soup = BeautifulSoup(response.text, 'lxml')
        title = soup.h1.get_text()
        print(title)
        if title != "Welcome to BuzzerBeater!":
            self.logger.error("Login failed")
        else:
            self.logger.info("Login successful")
            for url in self.urls:
                self.logger.info(["URL", url])
                yield scrapy.Request(url, callback=self.parse_transfer_search)

    # Sends a transfer search request to obtain the players on the market
    def parse_transfer_search(self, response):
        viewstate = response.xpath('//input[@name="__VIEWSTATE"]/@value').extract_first()
        eventvalidation = response.xpath('//input[@name="__EVENTVALIDATION"]/@value').extract_first()
        print(eventvalidation)

        formdata = BB_TRANSFER_SEARCH_FORMDATA
        formdata['__EVENTVALIDATION'] = eventvalidation
        formdata['__VIEWSTATE'] = viewstate

        yield FormRequest(url=self.urls[0], callback=self.parse_transfers, formdata=formdata)

    # Parses the search results and follows the links to the individual player overviews
    def parse_transfers(self, response):
        self.transfer_list_page += 1
        self.logger.info(msg=("Transfer list page: ", self.transfer_list_page))
        viewstate = response.xpath('//input[@name="__VIEWSTATE"]/@value').extract_first()
        eventvalidation = response.xpath('//input[@name="__EVENTVALIDATION"]/@value').extract_first()
        previouspage = response.xpath('//input[@name="__PREVIOUSPAGE"]/@value').extract_first()
        page = response.xpath('//input[@name="ctl00$cphContent$hdnPage"]/@value').extract_first()
        search_id = response.xpath('//input[@name="ctl00$cphContent$hdnSearchID"]/@value').extract_first()
        search_date = response.xpath('//input[@name="ctl00$cphContent$hdnSearchDate"]/@value').extract_first()

        formdata = BB_TRANSFER_NEXT_PAGE_FORMDATA
        formdata['_PREVIOUSPAGE'] = previouspage
        formdata['_EVENTVALIDATION'] = eventvalidation
        formdata['_VIEWSTATE'] = viewstate
        formdata['tl00$cphContent$hdnPage'] = page
        formdata['tl00$cphContent$hdnSearchID'] = search_id
        formdata['tl00$cphContent$hdnSearchDate'] = search_date

        for row in response.xpath('//div[@id="playerbox"]'):
            player_link = row.xpath('div[@class="boxheader"]/a/@href')
            yield response.follow(player_link.extract_first(), self.parse_player)

        # If the 'next page' button is not present, it's the last page and stop
        if response.xpath('//input[@name="ctl00$cphContent$btnNextPage"]/@value').extract_first() is not None:
            self.logger.info(msg="Next Page button present")
            yield FormRequest(url=self.urls[0], formdata=formdata, callback=self.parse_transfers)

    # TODO add potential and role scraping
    # TODO move this to a more relevant .py the moment you have it
    # Parses individual player overviews
    def parse_player(self, response):

        # Getting player's name and ID
        player_id = re.search('/player\/(\d+)\/overview.aspx', response.url).group(1)
        player_name = response.xpath('//h1/text()').extract_first()

        # Extracting basic info (the "left" column) available about all players
        if player_name != "Player Not Found":

            personal_info = response.xpath('//td[@id="playerPersonalInfo"]')

            try:
                team_id = personal_info.xpath("div/a/@href").extract_first()
                team_id = re.search('/team\/(\d+)\/overview.aspx', team_id).group(1)
                team_name = personal_info.xpath("div/a/text()").extract_first()
            except AttributeError as e:
                team_id = "0000000000"
                team_name = "000000000"

            personal_info_text = personal_info.extract_first()
            weekly_salary = re.search('\$.(.+)<br', personal_info_text).group(1)
            weekly_salary = weekly_salary.replace(" ", "").replace('\xa0', '')
            dmi = re.search('DMI:.\s+(\d+)', personal_info_text).group(1)
            age = re.search('Age:.\s+(\d+)', personal_info_text).group(1)
            height = re.search('Height:\s+.+ \/ (\d+) cm<br', personal_info_text).group(1)
            game_shape = personal_info.xpath('//a[@id="ctl00_cphContent_playerForm_linkDen"]/text()').extract_first()
            position = personal_info.xpath('//div[@style="float: right; display: block;"]/text()').extract_first()

            # TODO replace is ugly, do through regex
            position = re.search('\s+(.+)\s+', position).group(1).replace("\r", "")

            # Extracting transfer info (if exists)
            transfer_info = response.xpath(
                '//span[@id="ctl00_cphContent_LbtTransferEstimateIntroNew"]/text()').extract_first()

            # Looping through each element that contains transfer info
            if transfer_info is not None:
                i = 1
                transfer_estimate = []
                while i <= 3:
                    span = response.xpath(
                        '//span[@id="ctl00_cphContent_LblTransferEstimate' + str(i) + 'new"]/text()').extract_first()
                    print(span)

                    if span is not None:
                        transfer_estimate.append(span.replace('\xa0', ''))
                    i += 1
                transfer_estimate = ' '.join(transfer_estimate)

            team_item = TeamItem(id=team_id,
                                 name=team_name)
            player_item = PlayerItem(id=player_id,
                                     weekly_salary=weekly_salary,
                                     dmi=dmi,
                                     age=age,
                                     height=height,
                                     position=position,
                                     name=player_name,
                                     team_id=team_id,
                                     transfer_estimate=transfer_estimate)
            yield team_item
            yield player_item

            # Extracting skills (the "right" column)
            skills_div = response.xpath('//div[@id="ctl00_cphContent_faceContainer"]/following-sibling::div[1]')
            skills_td = skills_div.xpath('table/tr/td/following-sibling::td[1]')

            if skills_td.xpath("table").extract_first() is not None:
                skills_table = skills_td.xpath('table[1]')

                for skill in skills_table.xpath('tr/td'):
                    if skill.xpath("a").extract_first() is not None:
                        skill_name = re.search('<td>\s+(.+)\:', skill.extract()).group(1)
                        skill_value = skill.xpath('a/@title').extract_first()

                        player_skills_item = PlayerSkillsItem(player_id=player_id,
                                                              skill=skill_name,
                                                              value=skill_value)
                        yield player_skills_item
                    else:
                        print("Empty row")

            player_history_link = response.xpath('//a[@title="Player History"]/@href')
            yield response.follow(player_history_link.extract_first(), self.parse_player_history)

        else:
            print("Player not found")

    # TODO move this to a more relevant .py the moment you have it
    # Parses the player history page
    def parse_player_history(self, response):
        player_id = re.search('/player\/(\d+)\/history.aspx', response.url).group(1)
        history_table = response.xpath('//table[@class="history stats"]')

        for idx, row in enumerate(history_table.xpath('tr')):
            if idx != 0:
                event = row.xpath('td[1]/text()').extract_first()
                date = row.xpath('td[2]/text()').extract_first()
                date = datetime.strptime(date, '%m/%d/%Y')
                season = row.xpath('td[3]/text()').extract_first()

                # TODO Parse details and save to separate tables
                details = row.xpath('td[4]/descendant-or-self::*/text()').extract()

                player_history_item = PlayerHistoryItem(player_id=player_id,
                                                        event=event,
                                                        date=date,
                                                        season=season,
                                                        details=''.join(details))
                yield player_history_item
