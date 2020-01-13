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
>>> user.skill['overall']
{'rank': '5238', 'level': '1889', 'experience': '175809308'}

# Target A specific game mode
# Avilable targets are based on the runescape URI (ironman, ultamite, hardcore_ironman, seasonal, deadman, tournament)
>>> user = Highscores("dids", target="ironman")
>>> user.skill['attack']['level']
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
>>> print(attack_top.__dict__)
{'username': 'Heur', 'type': 'skill', 'rank': 1, 'xp': '200,000,000', 'level': '99', 'skill': 'attack'}

```
