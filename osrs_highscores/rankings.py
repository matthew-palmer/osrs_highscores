from bs4 import BeautifulSoup
import requests
import time
from .resources.categories import OSRSInfo, normalize_name
from .base import OSRSBase, max_retries, targets


class OSRSRank(object):
    """OSRSRank

    This is a placeholder class for information from a target rank. Returns from Ranking class

    Args:
        username  str: Username of Account at rank
        rank_type str: skill/nonskill identifier
        **kwargs: Additional keywords for attributes to be applied.

    """
    def __init__(self, username, rank_type, **kwargs):
        self.username = username
        self.type = rank_type
        self.__instantiate(**kwargs)

    def __is_skill(self, **kwargs):
        """__is_skill

        Method to set information relative to a target Skill instance

        Args:
            **kwargs : Keyword args relative to skill (xp, level and skill)

        Returns:
            None
        """
        try:
            self.xp = kwargs.get('xp').replace(',', '')
            self.level = kwargs.get('level')
            self.skill = kwargs.get('skill')
        except Exception as err:
            raise err

    def __is_non_skill(self, **kwargs):
        """__is_non_skill

        Method to set information relative to target nonskill instance

        Args:
            **kwargs :  Keyword args relative to nonskill (score, type)

        Returns:
            None
        """
        try:
            self.score = kwargs.get('score').replace(',', '')
            self.type = kwargs.get('type')
        except Exception as err:
            raise err

    def __instantiate(self, **kwargs):
        """__instantiate

        Method to select population method for object instance based on self.type

        Args:
            **kwargs : Keyword args relative to target instance of Rank (skill/nonskill)
        """
        self.rank = kwargs.get('rank')
        if self.type == 'skill':
            self.__is_skill(**kwargs)
        elif self.type == 'nonskill':
            self.__is_non_skill(**kwargs)
        else:
            raise ValueError('Target type is not a valid identifier (skill/nonskill')


class Rankings(OSRSBase):
    """Rankings

    This class obtains and formats the user info for a rank and target.

    Args:
        target str: The target Highscores to lookup username. Defaults to `default`
                  - Accepted Values: [default, ironman, ultimate, hardcore_ironman, seasonal, deadman, tournament,
                                      fresh_start, skiller, skiller_defence]

    Returns:
        None
    """
    # Any player present on the main hiscores; used to read the live table numbers for each skill/activity.
    reference_player = "Lynx Titan"

    def __init__(self, target="default"):
        super(Rankings, self).__init__(target)
        self.index = "overall.ws"
        self.__tables = None

    def __load_tables(self):
        """__load_tables

        Reads the current table number for every skill and activity from the hiscores JSON endpoint, falling back to
        the bundled category list if it can't be reached. Table numbers are the same across all game modes.

        Returns:
            (dict, dict): skill name -> table number, activity name -> table number
        """
        if self.__tables is None:
            info = OSRSInfo()
            skills, activities = dict(info.index_inverse), dict(info.alt_index_inverse)
            try:
                url = "{}/m={}/index_lite.json".format(self.base_url, targets["default"])
                data = self._get(url, params={"player": self.reference_player}).json()
                skills.update({normalize_name(entry["name"]): entry["id"] for entry in data["skills"]})
                activities.update({normalize_name(entry["name"]): entry["id"] for entry in data["activities"]})
            except (ValueError, KeyError, requests.RequestException):
                pass
            self.__tables = (skills, activities)
        return self.__tables

    def __process_data(self, params):
        target_url = self._OSRSBase__request_build()
        retry = 0
        while True:
            bs = BeautifulSoup(self._get(target_url, params=params).content, "html.parser")
            try:
                return bs.find("table").find("tbody").find_all("tr")
            except AttributeError:
                if retry >= max_retries:
                    raise
                retry += 1
                time.sleep(0.5 * retry)

    def get_rank_in_skill(self, skill, rank):
        """get_rank_in_skill

        Acquires an OSRSRank Object based on the target lookup and rank number.

        Args:
            skill str: Target skill, (e.g. attack, strength etc.)
            rank int: Rank target to lookup

        Returns:
            OSRSRank object
        """
        # Enforced sleep between calls, as this will hit the direct UI page and scrape information
        # Only added to avoid any implementations that may hurt the OSRS servers with load
        time.sleep(0.1)

        table = self.__load_tables()[0][skill]
        rank_page = (rank - 1) // 25 + 1
        rows = self.__process_data({"table": table, "page": rank_page})

        for row in rows:
            cells = row.find_all("td")
            try:
                check_rank = cells[0].getText().replace('\n', '').replace(',', '')
                if check_rank == str(rank):
                    user = cells[1].getText().replace('\n', '')
                    level = cells[2].getText().replace('\n', '')
                    xp = cells[3].getText().replace('\n', '')
                    return OSRSRank(user, 'skill', rank=rank, level=level, xp=xp, skill=skill)
            except (TypeError, IndexError):
                pass

    def get_rank_in_target(self, target, rank):
        """get_rank_in_target

        Acquires an OSRSRank Object based on the target lookup and rank number.

        Args:
            target str: Target alternative nonskill, (e.g. abyssal_sire, clue_scrolls_all etc.)
            rank int: Rank target to lookup

        Returns:
            OSRSRank object
        """
        # Enforced sleep between calls, as this will hit the direct UI page and scrape information
        # Only added to avoid any implementations that may hurt the OSRS servers with load
        time.sleep(0.1)

        table = self.__load_tables()[1][target]
        rank_page = (rank - 1) // 25 + 1
        rows = self.__process_data({"category_type": 1, "table": table, "page": rank_page})

        for row in rows:
            cells = row.find_all("td")
            try:
                check_rank = cells[0].getText().replace('\n', '').replace(',', '')
                if check_rank == str(rank):
                    user = cells[1].getText().replace('\n', '')
                    score = cells[2].getText().replace('\n', '')
                    return OSRSRank(user, 'nonskill', rank=rank, score=score, type=target)
            except (TypeError, IndexError):
                pass
