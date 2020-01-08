import requests
from .categories import ranking_dict


class Highscores(object):
    def __init__(self, username, target='default'):
        self.username = username
        self.target = target
        self.base_url = 'https://secure.runescape.com'
        self.skill = dict()
        self.minigame = dict()
        self.boss = dict()
        self.instantiate()

    def format_url(self, target_path):
        url = "{}/m={}/index_lite.ws?player={}".format(self.base_url, target_path, self.username)
        return url

    def request_build(self):
        if self.target == 'default':
            return self.format_url("hiscore_oldschool")
        elif self.target == 'ironman':
            return self.format_url("hiscore_oldschool_ironman")
        elif self.target == 'ultimate':
            return self.format_url("hiscore_oldschool_ultimate")
        elif self.target == 'seasonal':
            return self.format_url("hiscore_oldschool_seasonal")
        elif self.target == 'deadman':
            return self.format_url("hiscore_oldschool_deadman")
        elif self.target == 'tournament':
            return self.format_url("hiscore_oldschool_tournament")
        else:
            raise Exception('Invalid target param for Highsores Instance.')

    def process_data(self):
        if not self.data:
            raise ValueError("No data loaded!")
        count = 0
        skill = dict()
        minigame = dict()
        boss = dict()
        for _ in ranking_dict:
            data = self.data[count].split(',')

            if ranking_dict[count]['type'] == 'skill':
                info = {
                    'rank': data[0],
                    'level': data[1],
                    'experience': data[2],
                }
                skill[ranking_dict[count]['name']] = info
            elif ranking_dict[count]['type'] == 'minigame':
                info = {
                    'rank': data[0],
                    'amount': data[1],
                }
                minigame[ranking_dict[count]['name']] = info
            elif ranking_dict[count]['type'] == 'boss':
                info = {
                    'rank': data[0],
                    'kills': data[1],
                }
                boss[ranking_dict[count]['name']] = info
            count += 1
        self.skill = skill
        self.minigame = minigame
        self.boss = boss

    def instantiate(self):
        self.data = requests.get(self.request_build()).content.decode('utf-8').split('\n')
        self.process_data()

    def update(self):
        self.instantiate()
