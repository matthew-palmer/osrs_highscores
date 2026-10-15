import time
from addict import Dict
from .resources.categories import default_optional_ranks, normalize_name
from .resources.utils import OSRSXp
from .base import OSRSBase


class Highscores(OSRSBase):
    """Highscores

    This class obtains and formats the data requested from the runescape Highscores for OldSchool

    Args:
        username str: Target Username for Account
        target   str: The target Highscores to lookup username. Defaults to `default`
                  - Accepted Values: [default, ironman, ultimate, hardcore_ironman, seasonal, deadman, tournament,
                                      fresh_start, skiller, skiller_defence]

    Returns:
        None

    """
    def __init__(self, username, target='default'):
        super(Highscores, self).__init__(target)
        self.username = username
        self.target_url = self._OSRSBase__request_build()
        self.skill = dict()
        self.minigame = dict()
        self.boss = dict()
        self.__instantiate()

    def __process_data(self):
        """__process_data

        Formats the returned JSON payload into consumable self.* attributes
        self.skill
        self.minigame
        self.boss

        Entries are matched by name rather than position, so new skills, minigames and bosses added to the
        OSRS hiscores are picked up automatically.

        Args:
            self

        Returns:
            None

        """
        skill = dict()
        minigame = dict()
        boss = dict()
        xp_calc = OSRSXp()

        for entry in self.data.get('skills', []):
            name = normalize_name(entry['name'])
            level = int(entry['level'])
            xp = int(entry['xp'])
            if name == 'overall' or level >= 99:
                xp_to_level = 0
            else:
                xp_to_level = xp_calc.level_to_xp(level + 1) - xp
            info = {
                'rank': str(entry['rank']),
                'level': str(level),
                'xp': str(xp),
                'xp_to_level': xp_to_level
            }
            skill[name] = info
            setattr(self, name, Dict(info))

        for entry in self.data.get('activities', []):
            name = normalize_name(entry['name'])
            if name in default_optional_ranks:
                info = {
                    'rank': str(entry['rank']),
                    'score': str(entry['score']),
                }
                minigame[name] = info
            else:
                info = {
                    'rank': str(entry['rank']),
                    'kills': str(entry['score']),
                }
                boss[name] = info
            setattr(self, name, Dict(info))

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

        Raises:
            ValueError: The player was not found on the target hiscores, or no data was returned
        """
        try:
            self.data = self._get(self.target_url, params={'player': self.username}).json()
        except ValueError as err:
            # Includes a 404 from the hiscores and an unparsable (non-JSON) body
            raise ValueError("No data loaded! {}".format(err)) from err
        if not self.data.get('skills'):
            raise ValueError("No data loaded!")
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
