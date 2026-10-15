[![Tests](https://github.com/matthew-palmer/osrs_highscores/actions/workflows/tests.yml/badge.svg)](https://github.com/matthew-palmer/osrs_highscores/actions/workflows/tests.yml)
[![PyPI](https://img.shields.io/pypi/v/osrs_highscores)](https://pypi.org/project/osrs_highscores/)
![python](https://img.shields.io/pypi/pyversions/osrs_highscores)
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
>>> from osrs_highscores import Highscores

# Instantiates a new user object from username=zezima from default highscores.
>>> user = Highscores('Zezima')
>>> user.overall
{'rank': '5238', 'level': '1889', 'xp': '175809308', 'xp_to_level': 0}

# Target A specific game mode
# Available targets are listed in the Targets table below
>>> user = Highscores('dids', target='ironman')
>>> user.attack.level
'99'

# Update existing data of object
>>> user.update()

# A player that doesn't exist on the target hiscores raises ValueError
>>> Highscores('Lynx Titan', target='ironman')
ValueError: No data loaded! ...
```

Values are returned as strings, exactly as reported by the hiscores. Unranked entries are reported as `'-1'`.

#### Rankings
*The OSRS API does not have a specific endpoint, so queries using ranks is done with bs4 and scraping the UI result.*
*Implementation of this Function may not work on all systems if you have issues with bs4.*
```
>>> from osrs_highscores import Rankings

>>> ranks = Rankings()
>>> attack_top = ranks.get_rank_in_skill('attack', 1)
>>> print(attack_top.username)
Heur

>>> print(attack_top.level)
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
    - xp_to_level (int, 0 for `overall` and maxed skills)
- user.*minigame (e.g. clue_scrolls_easy, lms_rank, bounty_hunter_hunter)
    - rank
    - score
- user.*boss (e.g. chaos_elemental, hespori, the_gauntlet)
    - rank
    - kills

All of the above are also grouped as dicts in `user.skill`, `user.minigame` and `user.boss`.

Entries are matched by name from the hiscores JSON API, so skills, minigames and bosses that Jagex adds are picked up
automatically, even before they are listed below. A display name is converted to an attribute by lowercasing it and
replacing punctuation/spaces with `_` (e.g. `Theatre of Blood: Hard Mode` -> `theatre_of_blood_hard_mode`).

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
**PLEASE NOTE** This table may not be up-to-date. It was last updated on 11 October 2026. New hiscores entries are
still available on `Highscores` objects; `Rankings` reads the current table numbers from the hiscores at runtime.

*Ref # is the associated osrs_highscores index number*

*Table # is the associated OSRS highscores URL reference lookup query param*

- Category=0 assumed for skill refs.
- Category=1 for all nonskills.

| Attribute Name                    | Ref # | Table # (relative to category) |
|-----------------------------------|-------|--------------------------------|
| overall                           | 0     | 0                              |
| attack                            | 1     | 1                              |
| defence                           | 2     | 2                              |
| strength                          | 3     | 3                              |
| hitpoints                         | 4     | 4                              |
| ranged                            | 5     | 5                              |
| prayer                            | 6     | 6                              |
| magic                             | 7     | 7                              |
| cooking                           | 8     | 8                              |
| woodcutting                       | 9     | 9                              |
| fletching                         | 10    | 10                             |
| fishing                           | 11    | 11                             |
| firemaking                        | 12    | 12                             |
| crafting                          | 13    | 13                             |
| smithing                          | 14    | 14                             |
| mining                            | 15    | 15                             |
| herblore                          | 16    | 16                             |
| agility                           | 17    | 17                             |
| thieving                          | 18    | 18                             |
| slayer                            | 19    | 19                             |
| farming                           | 20    | 20                             |
| runecraft                         | 21    | 21                             |
| hunter                            | 22    | 22                             |
| construction                      | 23    | 23                             |
| sailing                           | 24    | 24                             |
| league_points                     | 25    | 0                              |
| deadman_points                    | 26    | 1                              |
| bounty_hunter_hunter              | 27    | 2                              |
| bounty_hunter_rogue               | 28    | 3                              |
| bounty_hunter_legacy_hunter       | 29    | 4                              |
| bounty_hunter_legacy_rogue        | 30    | 5                              |
| clue_scrolls_all                  | 31    | 6                              |
| clue_scrolls_beginner             | 32    | 7                              |
| clue_scrolls_easy                 | 33    | 8                              |
| clue_scrolls_medium               | 34    | 9                              |
| clue_scrolls_hard                 | 35    | 10                             |
| clue_scrolls_elite                | 36    | 11                             |
| clue_scrolls_master               | 37    | 12                             |
| lms_rank                          | 38    | 13                             |
| pvp_arena_rank                    | 39    | 14                             |
| soul_wars_zeal                    | 40    | 15                             |
| rifts_closed                      | 41    | 16                             |
| colosseum_glory                   | 42    | 17                             |
| collections_logged                | 43    | 18                             |
| abyssal_sire                      | 44    | 19                             |
| alchemical_hydra                  | 45    | 20                             |
| amoxliatl                         | 46    | 21                             |
| araxxor                           | 47    | 22                             |
| artio                             | 48    | 23                             |
| barrows_chests                    | 49    | 24                             |
| brutus                            | 50    | 25                             |
| bryophyta                         | 51    | 26                             |
| callisto                          | 52    | 27                             |
| calvar_ion                        | 53    | 28                             |
| cerberus                          | 54    | 29                             |
| chambers_of_xeric                 | 55    | 30                             |
| chambers_of_xeric_challenge_mode  | 56    | 31                             |
| chaos_elemental                   | 57    | 32                             |
| chaos_fanatic                     | 58    | 33                             |
| commander_zilyana                 | 59    | 34                             |
| corporeal_beast                   | 60    | 35                             |
| crazy_archaeologist               | 61    | 36                             |
| dagannoth_prime                   | 62    | 37                             |
| dagannoth_rex                     | 63    | 38                             |
| dagannoth_supreme                 | 64    | 39                             |
| deranged_archaeologist            | 65    | 40                             |
| doom_of_mokhaiotl                 | 66    | 41                             |
| duke_sucellus                     | 67    | 42                             |
| general_graardor                  | 68    | 43                             |
| giant_mole                        | 69    | 44                             |
| grotesque_guardians               | 70    | 45                             |
| hespori                           | 71    | 46                             |
| kalphite_queen                    | 72    | 47                             |
| king_black_dragon                 | 73    | 48                             |
| kraken                            | 74    | 49                             |
| kree_arra                         | 75    | 50                             |
| kril_tsutsaroth                   | 76    | 51                             |
| lunar_chests                      | 77    | 52                             |
| mimic                             | 78    | 53                             |
| nex                               | 79    | 54                             |
| nightmare                         | 80    | 55                             |
| phosanis_nightmare                | 81    | 56                             |
| obor                              | 82    | 57                             |
| phantom_muspah                    | 83    | 58                             |
| sarachnis                         | 84    | 59                             |
| scorpia                           | 85    | 60                             |
| scurrius                          | 86    | 61                             |
| shellbane_gryphon                 | 87    | 62                             |
| skotizo                           | 88    | 63                             |
| sol_heredit                       | 89    | 64                             |
| spindel                           | 90    | 65                             |
| tempoross                         | 91    | 66                             |
| the_gauntlet                      | 92    | 67                             |
| the_corrupted_gauntlet            | 93    | 68                             |
| the_hueycoatl                     | 94    | 69                             |
| the_leviathan                     | 95    | 70                             |
| the_royal_titans                  | 96    | 71                             |
| the_whisperer                     | 97    | 72                             |
| theatre_of_blood                  | 98    | 73                             |
| theatre_of_blood_hard_mode        | 99    | 74                             |
| thermonuclear_smoke_devil         | 100   | 75                             |
| tombs_of_amascut                  | 101   | 76                             |
| tombs_of_amascut_expert_mode      | 102   | 77                             |
| tzkal_zuk                         | 103   | 78                             |
| tztok_jad                         | 104   | 79                             |
| vardorvis                         | 105   | 80                             |
| venenatis                         | 106   | 81                             |
| vet_ion                           | 107   | 82                             |
| vorkath                           | 108   | 83                             |
| wintertodt                        | 109   | 84                             |
| yama                              | 110   | 85                             |
| zalcano                           | 111   | 86                             |
| zulrah                            | 112   | 87                             |

## Development

```
python -m pip install -e '.[test]'
pytest            # offline tests (mocked hiscores responses)
pytest -m live    # tests against the real OSRS hiscores
```

## Releasing

Releases are published to PyPI automatically by the
[Upload Python Package](.github/workflows/python-publish.yml) workflow when a GitHub Release is published.

1. Bump `__version__` in `osrs_highscores/__version__.py` and merge to `master`.
2. Create a GitHub Release with a tag matching that version (e.g. `v0.10.0`) and publish it.
3. The workflow runs the tests, checks the tag matches the version, builds the sdist/wheel and uploads them to PyPI.

Publishing uses [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/), so no API token secret is
needed. One-time setup:

- On PyPI, open the `osrs_highscores` project -> *Manage* -> *Publishing* and add a GitHub trusted publisher with
  owner `matthew-palmer`, repository `osrs_highscores`, workflow `python-publish.yml` and environment `pypi`.
- In this GitHub repository, create an environment named `pypi` (*Settings* -> *Environments*). Optionally add
  required reviewers to approve each release.
