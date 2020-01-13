
class OSRSBase(object):
    def __init__(self, target="default"):
        self.base_url = "https://secure.runescape.com"
        self.target = target
        self.index = "index_lite.ws"

    def _format_url(self, target_path, **kwargs):
        """_format_url

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

    def _request_build(self, **kwargs):
        """_request_build

        *Internal Method* Returns URI for highscores path. Used for self.target_url value Formulation.

        Args:
            self

        Returns:
            self._format_url Pointer with provided Value from if/else self.target param.
        """
        if self.target == 'default':
            return self._format_url("hiscore_oldschool", **kwargs)
        elif self.target == 'ironman':
            return self._format_url("hiscore_oldschool_ironman", **kwargs)
        elif self.target == 'ultimate':
            return self._format_url("hiscore_oldschool_ultimate", **kwargs)
        elif self.target == 'hardcore_ironman':
            return self._format_url("hiscore_oldschool_hardcore_ironman", **kwargs)
        elif self.target == 'seasonal':
            return self._format_url("hiscore_oldschool_seasonal", **kwargs)
        elif self.target == 'deadman':
            return self._format_url("hiscore_oldschool_deadman", **kwargs)
        elif self.target == 'tournament':
            return self._format_url("hiscore_oldschool_tournament", **kwargs)
        else:
            raise ValueError('Invalid target param for Highscores Instance.')