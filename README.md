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
```
>>> from osrs_highsores import highscores

# Instantiates a new user object from username=zezima
>>> user = highscores('Zezima')
>>> user.skill['overall']
{'rank': '5238', 'level': '1889', 'experience': '175809308'}

# Target A specific game mode
>>> user = Highscores("dids", target="ironman")
>>> user.skill['attack']['level']
99

# Update existing data of object
user.update()

```
