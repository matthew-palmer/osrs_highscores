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

#### Targets
Table of all available OSRS Highscore boards and the associated ```target``` value used when instantiating a
```Highscores``` object to query them.

| Target             | Value                  |
|--------------------|------------------------|
| OSRS Highscores    | ```default```          |
| Ironman            | ```ironman```          |
| Ultimate Ironman   | ```ultimate```         |
| Hardcore Ironman   | ```hardcore_ironman``` |
| Seasonal           | ```seasonal```         |
| Deadman Mode       | ```deadman```          |
| Tournament         | ```tournament```       |
| Fresh Start Worlds | ```fresh_start```      |
| Skiller            | ```skiller```          |
| 1 Defence          | ```skiller_defence```  |


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
print("Lynx Titan:\n"
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
Lynx Titan:
Attack 99 overall: {'rank': '1', 'level': '2277', 'xp': '4600000000'}
Dag Rex Kills: -1
All Clues Completed: 22
All Clues Rank: 433023
```

###### Reference Table
**PLEASE NOTE** This table may not be up-to-date. It was last updated on
26 July 2023.

*Ref # is the associated osrs_highscores dict index number*

*Table # is the associated OSRS highscores URL reference lookup query param*

- Category=0 assumed for skill refs.
- Category=1 for all nonskills.




| Attribute Name                   | Ref # | Table # (relative to category) |
|----------------------------------|-------|--------------------------------|
| overall                          | 0     | 0                              |
| attack                           | 1     | 1                              |
| defence                          | 2     | 2                              |
| strength                         | 3     | 3                              |
| hitpoints                        | 4     | 4                              |
| ranged                           | 5     | 5                              |
| prayer                           | 6     | 6                              |
| magic                            | 7     | 7                              |
| cooking                          | 8     | 8                              |
| woodcutting                      | 9     | 9                              |
| fletching                        | 10    | 10                             |
| fishing                          | 11    | 11                             |
| firemaking                       | 12    | 12                             |
| crafting                         | 13    | 13                             |
| smithing                         | 14    | 14                             |
| mining                           | 15    | 15                             |
| herblore                         | 16    | 16                             |
| agility                          | 17    | 17                             |
| thieving                         | 18    | 18                             |
| slayer                           | 19    | 19                             |
| farming                          | 20    | 20                             |
| runecraft                        | 21    | 21                             |
| hunter                           | 22    | 22                             |
| construction                     | 23    | 23                             |
| league_points                    | 24    | 0                              |
| bounty_hunter_hunter             | 25    | 1                              |
| bounty_hunter_rogue              | 26    | 2                              |
| bounty_hunter_legacy_hunter      | 27    | 3                              |
| bounty_hunter_legacy_rogue       | 28    | 4                              |
| clue_scrolls_all                 | 29    | 5                              |
| clue_scrolls_beginner            | 30    | 6                              |
| clue_scrolls_easy                | 31    | 7                              |
| clue_scrolls_medium              | 32    | 8                              |
| clue_scrolls_hard                | 33    | 9                              |
| clue_scrolls_elite               | 34    | 10                             |
| clue_scrolls_master              | 35    | 11                             |
| lms_rank                         | 36    | 12                             |
| pvp_arena_rank                   | 37    | 13                             |
| soul_wars_zeal                   | 38    | 14                             |
| rifts_closed                     | 39    | 15                             |
| abyssal_sire                     | 40    | 16                             |
| alchemical_hydra                 | 41    | 17                             |
| artio                            | 42    | 18                             |
| barrows_chests                   | 43    | 19                             |
| bryophyta                        | 44    | 20                             |
| callisto                         | 45    | 21                             |
| calvar_ion                       | 46    | 22                             |
| cerberus                         | 47    | 23                             |
| chambers_of_xeric                | 48    | 24                             |
| chambers_of_xeric_challenge_mode | 49    | 25                             |
| chaos_elemental                  | 50    | 26                             |
| chaos_fanatic                    | 51    | 27                             |
| commander_zilyana                | 52    | 28                             |
| corporeal_beast                  | 53    | 29                             |
| crazy_archaeologist              | 54    | 30                             |
| dagannoth_prime                  | 55    | 31                             |
| dagannoth_rex                    | 56    | 32                             |
| dagannoth_supreme                | 57    | 33                             |
| deranged_archaeologist           | 58    | 34                             |
| duke_sucellus                    | 59    | 35                             |
| general_graardor                 | 60    | 36                             |
| giant_mole                       | 61    | 37                             |
| grotesque_guardians              | 62    | 38                             |
| hespori                          | 63    | 39                             |
| kalphite_queen                   | 64    | 40                             |
| king_black_dragon                | 65    | 41                             |
| kraken                           | 66    | 42                             |
| kree_arra                        | 67    | 43                             |
| kril_tsutsaroth                  | 68    | 44                             |
| mimic                            | 69    | 45                             |
| nightmare                        | 70    | 46                             |
| phosanis_nightmare               | 71    | 47                             |
| obor                             | 72    | 48                             |
| phantom_muspah                   | 73    | 49                             |
| sarachnis                        | 74    | 50                             |
| scorpia                          | 75    | 51                             |
| skotizo                          | 76    | 52                             |
| spindel                          | 77    | 53                             |
| tempoross                        | 78    | 54                             |
| the_gauntlet                     | 79    | 55                             |
| the_corrupted_gauntlet           | 80    | 56                             |
| the_leviathan                    | 81    | 57                             |
| the_whisperer                    | 82    | 58                             |
| theatre_of_blood                 | 83    | 59                             |
| thermonuclear_smoke_devil        | 84    | 60                             |
| tzkal_zuk                        | 85    | 61                             |
| tztok_jad                        | 86    | 62                             |
| vardorvis                        | 87    | 63                             |
| venenatis                        | 88    | 64                             |
| vet_ion                          | 89    | 65                             |
| vorkath                          | 90    | 66                             |
| wintertodt                       | 91    | 67                             |
| zalcano                          | 92    | 68                             |
| zulrah                           | 93    | 69                             |
