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
15 October 2024.

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
| deadman_points                   | 25    | 1                              |
| bounty_hunter_hunter             | 26    | 2                              |
| bounty_hunter_rogue              | 27    | 3                              |
| bounty_hunter_legacy_hunter      | 28    | 4                              |
| bounty_hunter_legacy_rogue       | 29    | 5                              |
| clue_scrolls_all                 | 30    | 6                              |
| clue_scrolls_beginner            | 31    | 7                              |
| clue_scrolls_easy                | 32    | 8                              |
| clue_scrolls_medium              | 33    | 9                              |
| clue_scrolls_hard                | 34    | 10                             |
| clue_scrolls_elite               | 35    | 11                             |
| clue_scrolls_master              | 36    | 12                             |
| lms_rank                         | 37    | 13                             |
| pvp_arena_rank                   | 38    | 14                             |
| soul_wars_zeal                   | 39    | 15                             |
| rifts_closed                     | 40    | 16                             |
| colosseum_glory                  | 41    | 17                             |
| abyssal_sire                     | 42    | 18                             |
| alchemical_hydra                 | 43    | 19                             |
| amoxliatl                        | 44    | 20                             |
| arraxor                          | 45    | 21                             |
| artio                            | 46    | 22                             |
| barrows_chests                   | 47    | 23                             |
| bryophyta                        | 48    | 24                             |
| callisto                         | 49    | 25                             |
| calvar_ion                       | 50    | 26                             |
| cerberus                         | 51    | 27                             |
| chambers_of_xeric                | 52    | 28                             |
| chambers_of_xeric_challenge_mode | 53    | 29                             |
| chaos_elemental                  | 54    | 30                             |
| chaos_fanatic                    | 55    | 31                             |
| commander_zilyana                | 56    | 32                             |
| corporeal_beast                  | 57    | 33                             |
| crazy_archaeologist              | 58    | 34                             |
| dagannoth_prime                  | 59    | 35                             |
| dagannoth_rex                    | 60    | 36                             |
| dagannoth_supreme                | 61    | 37                             |
| deranged_archaeologist           | 62    | 38                             |
| duke_sucellus                    | 63    | 39                             |
| general_graardor                 | 64    | 40                             |
| giant_mole                       | 65    | 41                             |
| grotesque_guardians              | 66    | 42                             |
| hespori                          | 67    | 43                             |
| kalphite_queen                   | 68    | 44                             |
| king_black_dragon                | 69    | 45                             |
| kraken                           | 70    | 46                             |
| kree_arra                        | 71    | 47                             |
| kril_tsutsaroth                  | 72    | 48                             |
| lunar_chests                     | 73    | 49                             |
| mimic                            | 74    | 50                             |
| nex                              | 75    | 51                             |
| nightmare                        | 76    | 52                             |
| phosanis_nightmare               | 77    | 53                             |
| obor                             | 78    | 54                             |
| phantom_muspah                   | 79    | 55                             |
| sarachnis                        | 80    | 56                             |
| scorpia                          | 81    | 57                             |
| scurrius                         | 82    | 58                             |
| skotizo                          | 83    | 59                             |
| sol_heredit                      | 84    | 60                             |
| spindel                          | 85    | 61                             |
| tempoross                        | 86    | 62                             |
| the_gauntlet                     | 87    | 63                             |
| the_corrupted_gauntlet           | 88    | 64                             |
| the_hueycoatl                    | 89    | 65                             |
| the_leviathan                    | 90    | 66                             |
| the_whisperer                    | 91    | 67                             |
| theatre_of_blood                 | 92    | 68                             |
| theatre_of_blood_hard_mode       | 93    | 69                             |
| thermonuclear_smoke_devil        | 94    | 70                             |
| tombs_of_amascut                 | 95    | 71                             |
| tombs_of_amascut_expert_mode     | 96    | 72                             |
| tzkal_zuk                        | 97    | 73                             |
| tztok_jad                        | 98    | 74                             |
| vardorvis                        | 99    | 75                             |
| venenatis                        | 100   | 76                             |
| vet_ion                          | 101   | 77                             |
| vorkath                          | 102   | 78                             |
| wintertodt                       | 103   | 79                             |
| zalcano                          | 104   | 80                             |
| zulrah                           | 105   | 81                             |
