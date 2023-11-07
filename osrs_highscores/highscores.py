import requests
import time
import urllib3
from addict import Dict
from .resources.dotnotationcreator import dotnotation
from .resources.category import categories
from .resources.utils import OSRSXp
from .resources.bossslicer import startBossList
from .resources.listslicer import StartOfBosses
from .resources.listslicer import EndOfSkill
from .base import OSRSBase
from bs4 import BeautifulSoup


class Highscores(OSRSBase):
    """Highscores

    This class obtains and formats the data requested from the runescape Highscores for OldSchool

    Args:
        username str: Target Username for Account
        target   str: The target Highscores to lookup username. Defaults to `default`
                  - Accepted Values: [default, ironman, ultamite, hardcore_ironman, seasonal, tournament, deadman]

    Returns:
        None

    """

    def __init__(self, username, target='default'):
        super(Highscores, self).__init__(target)
        self.username = username
        self.target_url = self._OSRSBase__request_build(player=username)
        self.skill = dict()
        self.minigame = dict()
        self.boss = dict()
        self.category = dict()
        self.__instantiate()

    def __process_data(self):
        """__process_data

        Formats the returned raw string value into consumable self.* attributes
        self.skill
        self.minigame
        self.boss

        Args:
            self

        Returns:
            None

        """
        skill = dict()
        minigame = dict()
        boss = dict()
        xp_calc = OSRSXp()
        fullList = []

        page = BeautifulSoup(self.categoriesdata.data, 'html.parser')
        category = page.find("div", {"id": "contentCategory"})
        anchors = category.find_all("a", href=True)
        for anchor in anchors:
            fullList.append(anchor.get_text(strip=True))
        # for index, anchor in enumerate(anchors):
        #
        #
        #
        #     if len(self.data[index].split(',')) == 3:
        #         infomation = self.data[index].split(',')
        #         info = dotnotation({
        #             'rank': infomation[0],
        #             'level': infomation[1],
        #             'XP': infomation[2]
        #         })
        #         self.categories[anchor.get_text(strip=True)] = info
        #         # print(self.categories[anchor.get_text(strip=True)])
        #     elif len(self.data[index].split(',')) == 2:
        #         info = dotnotation({
        #             'rank': infomation[0],
        #             'score': infomation[1]
        #         })
        #         self.categories[anchor.get_text(strip=True)] = info
        # self.categories = dotnotation(self.categories)
        skills = fullList[:fullList.index(EndOfSkill) + 1]
        minigames = fullList[fullList.index(EndOfSkill) + 1:fullList.index(StartOfBosses)]
        bosses = fullList[fullList.index(StartOfBosses):]
        count = 0
        for sk in skills:
            data = self.data[count].split(',')
            categories.Skill[sk] = dotnotation({
                'rank': data[0],
                'level': data[1],
                'xp': data[2],
                'xp_to_level': xp_calc.level_to_xp(int(data[1]) + 1) - int(data[2])
            })
            count += 1
        for mini in minigames:
            data = self.data[count].split(',')
            categories.MiniGame[mini] = dotnotation({
                'rank': data[0],
                'score': data[1]
            })
            count += 1
        for boss in bosses:
            data = self.data[count].split(',')
            categories.Boss[boss] = dotnotation({
                'rank': data[0],
                'kills': data[1]
            })
            count += 1
        self.category = dotnotation(categories)
        self.skill = dotnotation(categories.Skill)
        self.minigame = dotnotation(categories.MiniGame)
        self.boss = dotnotation(categories.Boss)

    def __instantiate(self):
        """__instantiate

        Runs a full query and process request on the target URL for username/target provided.

        Args:
            self

        Returns:
            None
        """
        max_retries = 5
        retry = 0

        self.data = requests.get(self.target_url).content.decode('utf-8').split('\n')
        urlpage = "https://secure.runescape.com/m=hiscore_oldschool/overall"
        http = urllib3.PoolManager()
        self.categoriesdata = http.request("GET", urlpage)
        self.time = time.time()
        self.__process_data()

    def update(self):
        """update

        Updates existing information by making a new request to the OSRS Highscores

        Args:
            self

        Returns:
            None
        """
        self.__instantiate()
