from .resources.categories import default_list


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
                - Accepted Values: [default, ironman, ultamite, hardcore_ironman, seasonal, tournament, deadman]

    Returns:
        None
    """
    def __init__(self, target="default"):
        self.base_url = "https://secure.runescape.com"
        self.target = target
        self.index = "index_lite.ws"

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
            self._format_url Pointer with provided Value from if/else self.target param.
        """
        if self.target == 'default':
            return self.__format_url("hiscore_oldschool", **kwargs)
        elif self.target == 'ironman':
            return self.__format_url("hiscore_oldschool_ironman", **kwargs)
        elif self.target == 'ultimate':
            return self.__format_url("hiscore_oldschool_ultimate", **kwargs)
        elif self.target == 'hardcore_ironman':
            return self.__format_url("hiscore_oldschool_hardcore_ironman", **kwargs)
        elif self.target == 'seasonal':
            return self.__format_url("hiscore_oldschool_seasonal", **kwargs)
        elif self.target == 'deadman':
            return self.__format_url("hiscore_oldschool_deadman", **kwargs)
        elif self.target == 'tournament':
            return self.__format_url("hiscore_oldschool_tournament", **kwargs)
        else:
            raise ValueError('Invalid target param for Highscores Instance.')
