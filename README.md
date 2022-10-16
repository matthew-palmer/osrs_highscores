[![Build Status](https://travis-ci.com/matthew-palmer/osrs_highscores.svg?branch=master)](https://travis-ci.com/matthew-palmer/osrs_highscores)
![types](https://img.shields.io/badge/python-3.7%2B-yellow)
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
**PLEASE NOTE** This Table may not be updated. It was last updated on
16 October 2022.

*Ref # is the associated osrs_highscores dict index number*

*Table # is the associated OSRS highscores URL reference lookup query param*

- Category=0 assumed for skill refs.
- Category=1 for all nonskills.




| Attribute Name                   |Ref #|Table # (relative to category)|
|----------------------------------|--|---|
| overall                          |0|0|
| attack                           |1|1|
| defence                          |2|2|
| strength                         |3|3|
| hitpoints                        |4|4|
| ranged                           |5|5|
| prayer                           |6|6|
| magic                            |7|7|
| cooking                          |8|8|
| woodcutting                      |9|9|
| fletching                        |10|10|
| fishing                          |11|11|
| firemaking                       |12|12|
| crafting                         |13|13|
| smithing                         |14|14|
| mining                           |15|15|
| herblore                         |16|16|
| agility                          |17|17|
| thieving                         |18|18|
| slayer                           |19|19|
| farming                          |20|20|
| runecraft                        |21|21|
| hunter                           |22|22|
| construction                     |23|23|
| league_points                    |24|0|
| bounty_hunter_hunter             |25|1|
| bounty_hunter_rogue              |26|2|
| clue_scrolls_all                 |27|3|
| clue_scrolls_beginner            |28|4|
| clue_scrolls_easy                |29|5|
| clue_scrolls_medium              |30|6|
| clue_scrolls_hard                |31|7|
| clue_scrolls_elite               |32|8|
| clue_scrolls_master              |33|9|
| lms_rank                         |34|10|
| pvp_arena_rank                   |35|11|
| soul_wars_zeal                   |36|12|
| rifts_closed                     |37|13|
| abyssal_sire                     |38|14|
| alchemical_hydra                 |39|15|
| barrows_chests                   |40|16|
| bryophyta                        |41|17|
| callisto                         |42|18|
| cerberus                         |43|19|
| chambers_of_xeric                |44|20|
| chambers_of_xeric_challenge_mode |45|21|
| chaos_elemental                  |46|22|
| chaos_fanatic                    |47|23|
| commander_zilyana                |48|24|
| corporeal_beast                  |49|25|
| crazy_archaeologist              |50|26|
| dagannoth_prime                  |51|27|
| dagannoth_rex                    |52|28|
| dagannoth_supreme                |53|29|
| deranged_archaeologist           |54|30|
| general_graardor                 |55|31|
| giant_mole                       |56|32|
| grotesque_guardians              |57|33|
| hespori                          |58|34|
| kalphite_queen                   |59|35|
| king_black_dragon                |60|36|
| kraken                           |61|37|
| kree_arra                        |62|38|
| kril_tsutsaroth                  |63|39|
| mimic                            |64|40|
| nightmare                        |65|41|
| phosanis_nightmare               |66|42|
| obor                             |67|43|
| sarachnis                        |68|44|
| scorpia                          |69|45|
| skotizo                          |70|46|
| tempoross                        |71|47|
| the_gauntlet                     |72|48|
| the_corrupted_gauntlet           |73|49|
| theatre_of_blood                 |74|50|
| thermonuclear_smoke_devil        |75|51|
| tzkal_zuk                        |76|52|
| tztok_jad                        |77|53|
| venenatis                        |78|54|
| vet_ion                          |79|55|
| vorkath                          |80|56|
| wintertodt                       |81|57|
| zalcano                          |82|58|
| zulra                            |83|59|
