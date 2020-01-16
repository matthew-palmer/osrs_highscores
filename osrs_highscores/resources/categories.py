default_skills = [
    "overall",
    "attack",
    "defence",
    "strength",
    "hitpoints",
    "ranged",
    "prayer",
    "magic",
    "cooking",
    "woodcutting",
    "fletching",
    "fishing",
    "firemaking",
    "crafting",
    "smithing",
    "mining",
    "herblore",
    "agility",
    "thieving",
    "slayer",
    "farming",
    "runecraft",
    "hunter",
    "construction",
]

default_optional_ranks = [
    "league_points",
    "bounty_hunter_hunter",
    "bounty_hunter_rogue",
    "clue_scrolls_all",
    "clue_scrolls_beginner",
    "clue_scrolls_easy",
    "clue_scrolls_medium",
    "clue_scrolls_hard",
    "clue_scrolls_elite",
    "clue_scrolls_master",
    "lms_rank",
]

default_boss_ranks = [
    "abyssal_sire",
    "alchemical_hydra",
    "barrows_chests",
    "bryophyta",
    "callisto",
    "cerberus",
    "chambers_of_xeric",
    "chambers_of_xeric_challenge_mode",
    "chaos_elemental",
    "chaos_fanatic",
    "commander_zilyana",
    "corporeal_beast",
    "crazy_archaeologist",
    "dagannoth_prime",
    "dagannoth_rex",
    "dagannoth_supreme",
    "deranged_archaeologist",
    "general_graardor",
    "giant_mole",
    "grotesque_guardians",
    "hespori",
    "kalphite_queen",
    "king_black_dragon",
    "kraken",
    "kree'arra",
    "k'ril_tsutsaroth",
    "mimic",
    "obor",
    "sarachnis",
    "scorpia",
    "skotizo",
    "the_gauntlet",
    "the_corrupted_gauntlet",
    "theatre_of_blood",
    "thermonuclear_smoke_devil",
    "tzkal-zuk",
    "tztok-jad",
    "venenatis",
    "vet'ion",
    "vorkath",
    "wintertodt",
    "zalcano",
    "zulrah",
]

default_list = default_skills + default_optional_ranks + default_boss_ranks

skill_dict = dict()
alt_dict = dict()
ranking_dict = dict()
count = 0
for entry in default_skills:
    info = {
        "type": "skill",
        "name": entry
    }
    skill_dict[count] = info
    ranking_dict[count] = info
    count += 1

alt_count = 0
for entry in default_optional_ranks:
    info = {
        "type": "minigame",
        "name": entry
    }
    alt_dict[alt_count] = info
    ranking_dict[count] = info
    count += 1
    alt_count += 1

for entry in default_boss_ranks:
    info = {
        "type": "boss",
        "name": entry
    }
    alt_dict[alt_count] = info
    ranking_dict[count] = info
    count += 1
    alt_count += 1


class OSRSInfo (object):
    """OSRSInfo

    Class to combine all skills and nonskills to a lookup dict. Inverting the lists is required for table# from the UI
    """
    def __init__(self):
        self.index = skill_dict
        self.index_inverse = self.inverse_dict(self.index)
        self.alt_index = alt_dict
        self.alt_index_inverse = self.inverse_dict(self.alt_index)

    @staticmethod
    def inverse_dict(target_dict):
        rev_info = dict()
        for key, value in target_dict.items():
            rev_info[value["name"]] = key
        return rev_info
