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
ValueError: No data loaded! Player not found on the target hiscores.
```

Values are returned as strings, exactly as reported by the hiscores. Unranked entries are reported as `'-1'`.

#### Rankings
*The OSRS API does not have a specific endpoint, so queries using ranks is done with bs4 and scraping the UI result.*
*Implementation of this Function may not work on all systems if you have issues with bs4.*

> **Note:** as of November 2026 the OSRS hiscores bot protection blocks automated requests for the ranking pages, so
> `Rankings` lookups typically fail with `requests.HTTPError` (403 Forbidden). `Highscores` lookups are not affected.
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
automatically, even before they are listed below. An activity this library doesn't know yet is grouped as a minigame
if the hiscores list it before the bosses, and as a boss otherwise. A display name is converted to an attribute by lowercasing it and
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
**PLEASE NOTE** This table may not be up-to-date. It was last updated on 20 November 2026. New hiscores entries are
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
| grid_points                       | 25    | 0                              |
| league_points                     | 26    | 1                              |
| deadman_points                    | 27    | 2                              |
| bounty_hunter_hunter              | 28    | 3                              |
| bounty_hunter_rogue               | 29    | 4                              |
| bounty_hunter_legacy_hunter       | 30    | 5                              |
| bounty_hunter_legacy_rogue        | 31    | 6                              |
| clue_scrolls_all                  | 32    | 7                              |
| clue_scrolls_beginner             | 33    | 8                              |
| clue_scrolls_easy                 | 34    | 9                              |
| clue_scrolls_medium               | 35    | 10                             |
| clue_scrolls_hard                 | 36    | 11                             |
| clue_scrolls_elite                | 37    | 12                             |
| clue_scrolls_master               | 38    | 13                             |
| lms_rank                          | 39    | 14                             |
| pvp_arena_rank                    | 40    | 15                             |
| soul_wars_zeal                    | 41    | 16                             |
| rifts_closed                      | 42    | 17                             |
| colosseum_glory                   | 43    | 18                             |
| collections_logged                | 44    | 19                             |
| abyssal_sire                      | 45    | 20                             |
| alchemical_hydra                  | 46    | 21                             |
| amoxliatl                         | 47    | 22                             |
| araxxor                           | 48    | 23                             |
| artio                             | 49    | 24                             |
| barrows_chests                    | 50    | 25                             |
| brutus                            | 51    | 26                             |
| bryophyta                         | 52    | 27                             |
| callisto                          | 53    | 28                             |
| calvar_ion                        | 54    | 29                             |
| cerberus                          | 55    | 30                             |
| chambers_of_xeric                 | 56    | 31                             |
| chambers_of_xeric_challenge_mode  | 57    | 32                             |
| chaos_elemental                   | 58    | 33                             |
| chaos_fanatic                     | 59    | 34                             |
| commander_zilyana                 | 60    | 35                             |
| corporeal_beast                   | 61    | 36                             |
| crazy_archaeologist               | 62    | 37                             |
| dagannoth_prime                   | 63    | 38                             |
| dagannoth_rex                     | 64    | 39                             |
| dagannoth_supreme                 | 65    | 40                             |
| deranged_archaeologist            | 66    | 41                             |
| doom_of_mokhaiotl                 | 67    | 42                             |
| duke_sucellus                     | 68    | 43                             |
| general_graardor                  | 69    | 44                             |
| giant_mole                        | 70    | 45                             |
| grotesque_guardians               | 71    | 46                             |
| hespori                           | 72    | 47                             |
| kalphite_queen                    | 73    | 48                             |
| king_black_dragon                 | 74    | 49                             |
| kraken                            | 75    | 50                             |
| kree_arra                         | 76    | 51                             |
| kril_tsutsaroth                   | 77    | 52                             |
| lunar_chests                      | 78    | 53                             |
| mad_angel                         | 79    | 54                             |
| maggot_king                       | 80    | 55                             |
| mimic                             | 81    | 56                             |
| nex                               | 82    | 57                             |
| nightmare                         | 83    | 58                             |
| phosanis_nightmare                | 84    | 59                             |
| obor                              | 85    | 60                             |
| phantom_muspah                    | 86    | 61                             |
| sarachnis                         | 87    | 62                             |
| scorpia                           | 88    | 63                             |
| scurrius                          | 89    | 64                             |
| shellbane_gryphon                 | 90    | 65                             |
| skotizo                           | 91    | 66                             |
| sol_heredit                       | 92    | 67                             |
| spindel                           | 93    | 68                             |
| tempoross                         | 94    | 69                             |
| the_gauntlet                      | 95    | 70                             |
| the_corrupted_gauntlet            | 96    | 71                             |
| the_hueycoatl                     | 97    | 72                             |
| the_leviathan                     | 98    | 73                             |
| the_royal_titans                  | 99    | 74                             |
| the_whisperer                     | 100   | 75                             |
| theatre_of_blood                  | 101   | 76                             |
| theatre_of_blood_hard_mode        | 102   | 77                             |
| the_fractured_archive             | 103   | 78                             |
| thermonuclear_smoke_devil         | 104   | 79                             |
| tombs_of_amascut                  | 105   | 80                             |
| tombs_of_amascut_expert_mode      | 106   | 81                             |
| tzkal_zuk                         | 107   | 82                             |
| tztok_jad                         | 108   | 83                             |
| vardorvis                         | 109   | 84                             |
| venenatis                         | 110   | 85                             |
| vet_ion                           | 111   | 86                             |
| vorkath                           | 112   | 87                             |
| wintertodt                        | 113   | 88                             |
| yama                              | 114   | 89                             |
| zalcano                           | 115   | 90                             |
| zulrah                            | 116   | 91                             |

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
