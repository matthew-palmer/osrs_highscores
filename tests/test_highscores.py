import pytest
from osrs_highscores.highscores import Highscores


def test_lookup():
    user = Highscores('Zezima')
    assert user.skill['overall']['level'] != 0


def test_update():
    user = Highscores('Zezima')
    original_query = user.time
    user.update()
    new_query = user.time
    assert original_query != new_query


def test_target_not_exist():
    with pytest.raises(ValueError):
        user = Highscores('Zezima', target='ironman')


def test_target_exists():
    user = Highscores('dids', target='ironman')
    assert user.skill['overall']['level'] != 0
