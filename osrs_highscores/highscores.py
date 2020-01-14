import requests
import time
from addict import Dict
from .categories import ranking_dict
from .base import OSRSBase


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
        self.__instantiate()
        # Exposes all values as top level attributes
        self.__dict__ = Dict(dict(**self.skill, **self.minigame, **self.boss, **self.__dict__))

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
        if len(self.data) < 78:
            raise ValueError("No data loaded!")

        skill = dict()
        minigame = dict()
        boss = dict()

        count = 0
        for _ in ranking_dict:
            data = self.data[count].split(',')

            if ranking_dict[count]['type'] == 'skill':
                info = {
                    'rank': data[0],
                    'level': data[1],
                    'xp': data[2],
                }
                skill[ranking_dict[count]['name']] = info
            elif ranking_dict[count]['type'] == 'minigame':
                info = {
                    'rank': data[0],
                    'score': data[1],
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

    def __instantiate(self):
        """__instantiate

        Runs a full query and process request on the target URL for username/target provided.

        Args:
            self

        Returns:
            None
        """
        self.data = requests.get(self.target_url).content.decode('utf-8').split('\n')
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
