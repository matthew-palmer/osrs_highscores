import time
import requests
from .__version__ import __version__, __url__
from .resources.categories import default_list

# Maps the `target` value accepted by this library to the OSRS hiscores path for that game mode.
targets = {
    "default": "hiscore_oldschool",
    "ironman": "hiscore_oldschool_ironman",
    "ultimate": "hiscore_oldschool_ultimate",
    "hardcore_ironman": "hiscore_oldschool_hardcore_ironman",
    "seasonal": "hiscore_oldschool_seasonal",
    "deadman": "hiscore_oldschool_deadman",
    "tournament": "hiscore_oldschool_tournament",
    "fresh_start": "hiscore_oldschool_fresh_start",
    "skiller": "hiscore_oldschool_skiller",
    "skiller_defence": "hiscore_oldschool_skiller_defence",
}

headers = {"User-Agent": "osrs_highscores/{} (+{})".format(__version__, __url__)}
timeout = 10
max_retries = 5


def with_get_attr(cls):
    for entry in default_list:
        setattr(cls, entry, dict())
    return cls


@with_get_attr
class OSRSBase(object):
    """OSRSBase

    This class is the base class abstraction for highscores lookup. It sets up base functions for creating request URLs.

    Args:
        target str(optional): Sets the target lookup URI for the class instance.
                - Accepted Values: [default, ironman, ultimate, hardcore_ironman, seasonal, deadman, tournament,
                                    fresh_start, skiller, skiller_defence]

    Returns:
        None
    """
    def __init__(self, target="default"):
        if target not in targets:
            raise ValueError('Invalid target param for Highscores Instance.')
        self.base_url = "https://secure.runescape.com"
        self.target = target
        self.index = "index_lite.json"

    def __format_url(self, target_path, **kwargs):
        """__format_url

        Creates the Fully Qualified URL for highscores lookup request.

        Args:
            self
            target_path str: Unique string based on the available highscore gamemode paths

        Returns:
            url str: Fully Qualified URL for highscores lookup

        """
        url = "{}/m={}/{}".format(self.base_url, target_path, self.index)
        for key, value in kwargs.items():
            url += "?{}={}".format(key, value)

        return url

    def __request_build(self, **kwargs):
        """__request_build

        *Internal Method* Returns URI for highscores path. Used for self.target_url value Formulation.

        Args:
            self

        Returns:
            self._format_url Pointer with provided Value from self.target param.
        """
        if self.target not in targets:
            raise ValueError('Invalid target param for Highscores Instance.')
        return self.__format_url(targets[self.target], **kwargs)

    @staticmethod
    def _get(url, params=None):
        """_get

        *Internal Method* Performs a GET request against the OSRS hiscores, retrying transient failures.

        Args:
            url str: Fully Qualified URL to request
            params dict(optional): Query params for the request

        Returns:
            requests.Response

        Raises:
            ValueError: The hiscores returned 404 (e.g. the player does not exist on the target hiscores)
            requests.RequestException: The request kept failing after all retries
        """
        retry = 0
        while True:
            try:
                response = requests.get(url, params=params, headers=headers, timeout=timeout)
                if response.status_code == 404:
                    raise ValueError("No data loaded! Player not found on the target hiscores.")
                response.raise_for_status()
                return response
            except requests.RequestException:
                if retry >= max_retries:
                    raise
                retry += 1
                time.sleep(0.5 * retry)
