from bs4 import BeautifulSoup
import requests
import time
from .categories import OSRSInfo
from .base import OSRSBase, with_get_attr


@with_get_attr
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
        self._instantiate(**kwargs)

    def _is_skill(self, **kwargs):
        try:
            self.xp = kwargs.get('xp')
            self.level = kwargs.get('level')
            self.skill = kwargs.get('skill')
        except Exception as err:
            raise err

    def _is_non_skill(self, **kwargs):
        try:
            self.score = kwargs.get('score')
        except Exception as err:
            raise err

    def _instantiate(self, **kwargs):
        self.rank = kwargs.get('rank')
        if self.type == 'skill':
            self._is_skill(**kwargs)
        elif self.type == 'nonskill':
            self._is_non_skill(**kwargs)
        else:
            raise ValueError('Target type is not a valid identifier (skill/nonskill')


class Rankings(OSRSBase):
    """Rankings

    This class obtains and formats the user info for a rank and target.

    Args:
        target str: The target Highscores to lookup username. Defaults to `default`
                  - Accepted Values: [default, ironman, ultamite, hardcore_ironman, seasonal, tournament, deadman]

    Returns:
        None
    """
    def __init__(self, target="default"):
        super(Rankings, self).__init__(target)
        self.index = "overall.ws"

    def get_rank_in_skill(self, skill, rank):
        """get_rank_in_skill

        Acquires an OSRSRank Object based on the target lookup and rank number.

        Args:
            target str: Target skill, (e.g. attack, strength etc.)
            rank int: Rank target to lookup

        Returns:
            OSRSRank object
        """
        # Enforced sleep between calls, as this will hit the direct UI page and scrape information
        # Only added to avoid any implementations that may hurt the OSRS servers with load
        time.sleep(0.1)

        table = OSRSInfo().index_inverse[skill]
        rank_page = int(float(rank/25))
        table_string = "{}&page={}".format(table, rank_page)
        target_url = self._request_build(table=table_string)
        response = requests.get(target_url).content
        bs = BeautifulSoup(response, "html.parser")
        rows = bs.find("table").find("tbody").findAll("tr")
        for row in rows:
            cells = row.findAll("td")
            try:
                check_rank = cells[0].getText().replace('\n', '').replace(',', '')
                if check_rank == str(rank):
                    user = cells[1].getText().replace('\n', '')
                    level = cells[2].getText().replace('\n', '')
                    xp = cells[3].getText().replace('\n', '')
                    return OSRSRank(user, 'skill', rank=rank, level=level, xp=xp, skill=skill)
            except TypeError:
                pass

    def get_rank_in_target(self, target, rank):
        """get_rank_in_target

        Acquires an OSRSRank Object based on the target lookup and rank number.

        Args:
            target str: Target alternative nonskill, (e.g. abyssal_sire, clue_scroll_all etc.)
            rank int: Rank target to lookup

        Returns:
            OSRSRank object
        """
        # Enforced sleep between calls, as this will hit the direct UI page and scrape information
        # Only added to avoid any implementations that may hurt the OSRS servers with load
        time.sleep(0.1)

        table = OSRSInfo().alt_index_inverse[target]
        rank_page = int(float(rank / 25))
        category_string = "1&table={}&page={}".format(table, rank_page)
        target_url = self._request_build(category_type=category_string)
        response = requests.get(target_url).content
        bs = BeautifulSoup(response, "html.parser")
        rows = bs.find("table").find("tbody").findAll("tr")
        for row in rows:
            cells = row.findAll("td")
            try:
                check_rank = cells[0].getText().replace('\n', '').replace(',', '')
                if check_rank == str(rank):
                    user = cells[1].getText().replace('\n', '')
                    score = cells[2].getText().replace('\n', '')
                    return OSRSRank(user, 'nonskill', rank=rank, score=score)
            except TypeError:
                pass
