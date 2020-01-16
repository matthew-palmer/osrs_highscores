import math


class OSRSXp:
    """OSRSXp

    Class to encompass the math required for calculating xp for a specific level in OSRS.
    """
    @staticmethod
    def __calc(level):
        """calc

        Calculates the xp difference for target xp of level.

        Args:
            level int: Target level to calculate the difference of xp

        Returns:
            int: Value calculated from the equation for OSRS xp difference
        """
        return math.floor(level + 300 * (2 ** (level / 7.0)))

    def level_to_xp(self, level):
        """level_to_xp

        Returns the xp required to reach target level in OSRS

        Args:
            level int: Target level to calculate total XP required

        Returns:
            int: Value of total XP required for level
        """
        return math.floor(
            sum((self.__calc(target) for target in range(1, level))) / 4)
