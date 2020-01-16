[![Build Status](https://travis-ci.com/matt-palmer-tfs/osrs_highscores.svg?branch=master)](https://travis-ci.com/matt-palmer-tfs/osrs_highscores)
![types](https://img.shields.io/badge/python-3.6%2B-yellow)
# osrs_highscores

## Project Purpose
This is a simple wrapper library to make the OSRS Highscores usable from a python perspective. This wrapper provides straight information from the OSRS Highscores with no post processing, with lookups via snake_case naming.

## Installing and Usage

### Installation
```
python -m pip install osrs_highscores
```

### Upgrading
```
python -m pip install osrs_highscores --upgrade
```

### Basic Usage

#### Highscores
```
>>> from osrs_highsores import Highscores

# Instantiates a new user object from username=zezima from default highscores.
>>> user = Highscores('Zezima')
>>> user.overall
{'rank': '5238', 'level': '1889', 'experience': '175809308'}

# Target A specific game mode
# Avilable targets are based on the runescape URI (ironman, ultamite, hardcore_ironman, seasonal, deadman, tournament)
>>> user = Highscores('dids', target='ironman')
>>> user.attack.level
99

# Update existing data of object
user.update()

```

#### Rankings
*The OSRS API does not have a specific endpoint, so queries using ranks is done with bs4 and scraping the UI result.*
*Implementation of this Function may not work on all systems if you have issues with bs4.*
```
>>> from osrs_highscores import Rankings

>>> ranks = Rankings()
>>> attack_top = ranks.get_rank_in_skill('attack', 1)
>>> print(attack_top.username)
Heur

>>>print(attack_top.level)
99

```


#### Highscores Attributes
Table of all available attributes for highscores object

##### Advanced Use
In the list below, the following are exposed as top level attributes for the return for processing/use.

- user.*skill (e.g. attack, runecraft, herblore)
    - rank
    - level
    - xp
    - xp_to_level
- user.*minigame (e.g. clue_scrolls_easy, lms_rank, bounty_hunter_hunter)
    - rank
    - score
- user.*boss (e.g. chaos_elemental, hespori, the_gauntlet)
    - rank
    - kills

###### Example
````
user = Highscores('Lynx Titan')
print("Lynx_titan:\n"
      "Attack %s overall: %s\n"
      "Dag Rex Kills: %s\n"
      "All Clues Completed: %s\n"
      "All Clues Rank: %s" % (
           user.attack.level,
           user.overall,
           user.dagannoth_rex.kills,
           user.clue_scrolls_all.score,
           user.clue_scrolls_all.rank))
````
Output
```
Lynx_titan:
Attack 99 overall: {'rank': '1', 'level': '2277', 'xp': '4600000000'}
Dag Rex Kills: -1
All Clues Completed: 22
All Clues Rank: 433023
```

###### Reference Table
*Ref # is the associated osrs_highscores dict index number*

*Table # is the associated OSRS highscores URL reference lookup query param*

- Category=0 assumed for skill refs. 
- Category=1 for all nonskills. 




|Attribute Name|Ref #|Table # (relative to category)|
|---|---|---|
|overall|0|0|
|attack|1|1|
|defence|2|2|
|strength|3|3|
|hitpoints|4|4|
|ranged|5|5|
|prayer|6|6|
|magic|7|7|
|cooking|8|8|
|woodcutting|9|9|
|fletching|10|10|
|fishing|11|11|
|firemaking|12|12|
|crafting|13|13|
|smithing|14|14|
|mining|15|15|
|herblore|16|16|
|agility|17|17|
|thieving|18|18|
|slayer|19|19|
|farming|20|20|
|runecraft|21|21|
|hunter|22|22|
|construction|23|23|
|league_points|24|0|
|bounty_hunter_hunter|25|1|
|bounty_hunter_rogue|26|2|
|clue_scrolls_all|27|3|
|clue_scrolls_beginner|28|4|
|clue_scrolls_easy|29|5|
|clue_scrolls_medium|30|6|
|clue_scrolls_hard|31|7|
|clue_scrolls_elite|32|8|
|clue_scrolls_master|33|9|
|lms_rank|34|10|
|abyssal_sire|35|11|
|alchemical_hydra|36|12|
|barrows_chests|37|13|
|bryophyta|38|14|
|callisto|39|15|
|cerberus|40|16|
|chambers_of_xeric|41|17|
|chambers_of_xeric_challenge_mode|42|18|
|chaos_elemental|43|19|
|chaos_fanatic|44|20|
|commander_zilyana|45|21|
|corporeal_beast|46|22|
|crazy_archaeologist|47|23|
|dagannoth_prime|48|24|
|dagannoth_rex|49|25|
|dagannoth_supreme|50|26|
|deranged_archaeologist|51|27|
|general_graardor|52|28|
|giant_mole|53|29|
|grotesque_guardians|54|30|
|hespori|55|31|
|kalphite_queen|56|32|
|king_black_dragon|57|33|
|kraken|58|34|
|kree'arra|59|35|
|k'ril_tsutsaroth|60|36|
|mimic|61|37|
|obor|62|38|
|sarachnis|63|39|
|scorpia|64|40|
|skotizo|65|41|
|the_gauntlet|66|42|
|the_corrupted_gauntlet|67|43|
|theatre_of_blood|68|44|
|thermonuclear_smoke_devil|69|45|
|tzkal-zuk|70|46|
|tztok-jad|71|47|
|venenatis|72|48|
|vet'ion|73|49|
|vorkath|74|50|
|wintertodt|75|51|
|zalcano|76|52|
|zulra|77|53|
