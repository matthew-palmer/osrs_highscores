import pytest
from osrs_highscores.highscores import Highscores


def test_lookup():
    user = Highscores('RSB PerpDoom')
    print("Hello")
    print(user.skill.Attack)
    assert int(user.skill.Attack.level) == 90


def test_update():
    user = Highscores('Lynx Titan')
    original_query = user.time
    user.update()
    new_query = user.time
    assert original_query != new_query


def test_target_not_exist():
    with pytest.raises(ValueError):
        Highscores('Lynx Titan', target='ironman')


def test_target_exists():
    user = Highscores('dids', target='ironman')
    assert int(user.overall.level) != 0
