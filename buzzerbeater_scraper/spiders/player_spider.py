import scrapy
from datetime import datetime
import re

from buzzerbeater_scraper.items import PlayerItem, TeamItem, \
    PlayerSkillsItem, PlayerHistoryItem
from buzzerbeater_scraper.formdata import BB_LOGIN


# Turns the formatted skill name into a slug
def get_slug(string):
    return string.replace('.', '').replace(' ', '_').lower()


class PlayerSpider(scrapy.Spider):
    name = "player_spider"
    allowed_domains = ["buzzerbeater.com"]
    start_urls = (
        'http://www.buzzerbeater.com/default.aspx',
    )
    urls = []

    def __init__(self, player_ids='43023368', **kwargs):
        player_ids = player_ids.split(',')
        for player_id in player_ids:
            self.urls.append(
                'http://www.buzzerbeater.com/player/%s/overview.aspx' % player_id
            )
        super().__init__(**kwargs)  # python3

    def parse(self, response):
        # Opening a login request
        return scrapy.FormRequest.from_response(
            response,
            formdata=BB_LOGIN,
            callback=self.after_login
        )

    def after_login(self, response):
        # Check login succeed before going on
        title = response.xpath('//h1/text()').extract_first()
        print(title)
        if title != "Welcome to BuzzerBeater!":
            self.logger.error("Login failed")
        else:
            self.logger.info("Login successful")

            for url in self.urls:
                self.logger.info(["URL", url])
                yield scrapy.Request(url, callback=self.parse_player)

    # Wraps the parse_player_html method and yields items
    def parse_player(self, response):
        player = self.parse_player_html(response=response)

        if player is not None:
            player_item = player['player_item']
            team_item = player['team_item']
            skill_item = player['player_skills_item']

            yield team_item
            yield player_item
            yield skill_item

            player_history_link = player['player_history_link']
            yield response.follow(player_history_link,
                                  self.parse_player_history)

    # Parses the player history page
    def parse_player_history(self, response):
        player_history_items = self.parse_player_history_html(
            response=response)

        for item in player_history_items:
            yield item

    # Static method for parsing the html response of the player overview page
    @staticmethod
    def parse_player_html(response):

        # Getting player's name and ID
        try:
            player_id = re.search('/player/(\d+)/overview.aspx',
                                  response.url).group(1)
        except AttributeError as e:
            print('Invalid player id')
            print(e)

        player_name = response.xpath('//h1/text()').extract_first()

        # Extracting basic info (the "left" column) available about all players
        if player_name not in ("Player Not Found", None):

            personal_info = response.xpath('//td[@id="playerPersonalInfo"]')

            # Checking if the player is retired
            try:
                team_id = personal_info.xpath("div/a/@href").extract_first()
                team_id = re.search('/team/(\d+)/overview.aspx',
                                    team_id).group(1)
                team_name = personal_info.xpath(
                    "div/a/text()").extract_first()
            except AttributeError:
                team_id = "0000000000"
                team_name = "000000000"

            personal_info_text = personal_info.extract_first()
            weekly_salary = re.search('\sWeekly salary:\s+\$.(.+)<br',
                                      personal_info_text).group(1)
            weekly_salary = int(
                weekly_salary.replace(" ", "").replace('\xa0', ''))
            dmi = int(
                re.search('DMI:.\s+(\d+)', personal_info_text).group(1))
            age = int(
                re.search('Age:.\s+(\d+)', personal_info_text).group(1))
            height = int(re.search('Height:\s+.+ / (\d+) cm<br',
                                   personal_info_text).group(1))
            game_shape = int(personal_info.xpath(
                '//a[@id="ctl00_cphContent_playerForm_linkDen"]/@title').extract_first())
            potential = personal_info.xpath(
                '//a[@id="ctl00_cphContent_potential_linkDen"]/@title')
            potential = int(potential.extract_first().replace('10+', '11'))
            position = personal_info.xpath(
                '//div[@style="float: right; display: block;"]/text()').extract_first()

            position = re.search('\s+(.+)\s+', position).group(1).replace(
                "\r", "")

            # Extracting transfer info (if exists)
            transfer_info = response.xpath(
                '//span[@id="ctl00_cphContent_LbtTransferEstimateIntroNew"]/text()').extract_first()

            # Looping through each element that contains transfer info
            transfer_estimate = []
            if transfer_info is not None:
                i = 1
                while i <= 3:
                    span = response.xpath(
                        '//span[@id="ctl00_cphContent_LblTransferEstimate' + str(
                            i) + 'new"]/text()').extract_first()

                    if span is not None:
                        transfer_estimate.append(span.replace('\xa0', ''))
                    i += 1
                transfer_estimate = ' '.join(transfer_estimate)

            if not transfer_estimate:
                transfer_estimate = None

            team_item = TeamItem(id=team_id,
                                 name=team_name)
            player_item = PlayerItem(
                id=player_id,
                weekly_salary=weekly_salary,
                dmi=dmi,
                age=age,
                height=height,
                position=position,
                name=player_name,
                team_id=team_id,
                transfer_estimate=transfer_estimate,
                potential=potential
            )
            player_skills_item = PlayerSkillsItem(
                player_id=player_id,
                game_shape=game_shape,
            )

            # TODO Maybe, um, create a fucking players class?!?!
            yields = {
                'team_item': team_item,
                'player_item': player_item,
            }

            # Extracting skills (the "right" column)
            skills_div = response.xpath(
                '//div[@id="ctl00_cphContent_faceContainer"]/following-sibling::div[1]')
            skills_td = skills_div.xpath(
                'table/tr/td/following-sibling::td[1]')

            # TODO skills_td.xpath("table") je double asi
            # Checking if the skills table exists (unless own player or on the market, it never does)
            if skills_td.xpath("table").extract_first() is not None:
                skills_table = skills_td.xpath('table[1]')

                for skill in skills_table.xpath('tr/td'):
                    if skill.xpath('a').extract_first() is not None:
                        skill_name = re.search('<td>\s+(.+):',
                                               skill.extract()).group(1)
                        skill_name = get_slug(skill_name)
                        skill_value = skill.xpath(
                            'a/@title').extract_first()
                        player_skills_item[skill_name] = int(skill_value)

            player_history_link = response.xpath(
                '//a[@title="Player History"]/@href').extract_first()
            yields['player_skills_item'] = player_skills_item
            yields['player_history_link'] = player_history_link
            return yields
        else:
            print('Player not found')

    # Static method for parsing the html response of the player history page
    @staticmethod
    def parse_player_history_html(response):
        player_id = re.search('/player/(\d+)/history.aspx',
                              response.url).group(1)
        history_table = response.xpath('//table[@class="history stats"]')

        player_history_items = []
        for idx, row in enumerate(history_table.xpath('tr')):
            if idx != 0:
                event = row.xpath('td[1]/text()').extract_first()
                date = row.xpath('td[2]/text()').extract_first()
                date = datetime.strptime(date, '%m/%d/%Y')
                season = row.xpath('td[3]/text()').extract_first()

                # TODO Parse details and save to separate tables
                details = row.xpath(
                    'td[4]/descendant-or-self::*/text()').extract()
                details = ''.join(details).replace('\xa0', '')

                item = PlayerHistoryItem(player_id=player_id,
                                         event=event,
                                         date=date,
                                         season=season,
                                         details=details)
                player_history_items.append(item)

        return player_history_items
