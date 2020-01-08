import requests
import time
from .categories import ranking_dict


class Highscores(object):
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
        self.username = username
        self.target = target
        self.base_url = 'https://secure.runescape.com'
        self.target_url = self._request_build()
        self.skill = dict()
        self.minigame = dict()
        self.boss = dict()
        self._instantiate()

    def _format_url(self, target_path):
        """_format_url

        Creates the Fully Qualified URL for highscores lookup request.

        Args:
            self
            target_path str: Unique string based on the available highscore gamemode paths

        Returns:
            url str: Fully Qualified URL for highscores lookup

        """
        url = "{}/m={}/index_lite.ws?player={}".format(self.base_url, target_path, self.username)
        return url

    def _request_build(self):
        """_request_build

        *Internal Method* Returns URI for highscores path. Used for self.target_url value Formulation.

        Args:
            self

        Returns:
            self._format_url Pointer with provided Value from if/else self.target param.
        """
        if self.target == 'default':
            return self._format_url("hiscore_oldschool")
        elif self.target == 'ironman':
            return self._format_url("hiscore_oldschool_ironman")
        elif self.target == 'ultimate':
            return self._format_url("hiscore_oldschool_ultimate")
        elif self.target == 'hardcore_ironman':
            return self._format_url("hiscore_oldschool_hardcore_ironman")
        elif self.target == 'seasonal':
            return self._format_url("hiscore_oldschool_seasonal")
        elif self.target == 'deadman':
            return self._format_url("hiscore_oldschool_deadman")
        elif self.target == 'tournament':
            return self._format_url("hiscore_oldschool_tournament")
        else:
            raise ValueError('Invalid target param for Highscores Instance.')

    def _process_data(self):
        """_process_data

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

    def _instantiate(self):
        """_instantiate

        Runs a full query and process request on the target URL for username/target provided.

        Args:
            self

        Returns:
            None
        """
        self.data = requests.get(self.target_url).content.decode('utf-8').split('\n')
        self.time = time.time()
        self._process_data()

    def update(self):
        """update

        Updates existing information by making a new request to the OSRS Highscores

        Args:
            self

        Returns:
            None
        """
        self._instantiate()
