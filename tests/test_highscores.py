from unittest import mock

import pytest
import requests

from osrs_highscores.highscores import Highscores
from .conftest import make_response


@pytest.fixture
def mock_get(lynx_titan, no_sleep):
    with mock.patch("osrs_highscores.base.requests.get", return_value=make_response(payload=lynx_titan)) as get:
        yield get


def test_lookup(mock_get):
    user = Highscores('Lynx Titan')
    assert int(user.strength.level) == 99
    assert user.overall.xp == '4600000000'
    url = mock_get.call_args.args[0]
    assert url == "https://secure.runescape.com/m=hiscore_oldschool/index_lite.json"
    assert mock_get.call_args.kwargs["params"] == {"player": "Lynx Titan"}


def test_categories(mock_get):
    user = Highscores('Lynx Titan')
    assert user.clue_scrolls_all.score == '22'
    assert user.clue_scrolls_all.rank == '433023'
    assert user.dagannoth_rex.kills == '-1'
    assert user.kril_tsutsaroth == user.boss['kril_tsutsaroth']
    assert 'clue_scrolls_all' in user.minigame
    assert 'zulrah' in user.boss
    assert 'sailing' in user.skill


def test_xp_to_level(mock_get):
    user = Highscores('Lynx Titan')
    assert user.hunter.xp_to_level == 2192818 - 2000000  # level 81 is 2,192,818 xp
    assert user.attack.xp_to_level == 0
    assert user.overall.xp_to_level == 0


def test_new_entries_are_picked_up(mock_get, lynx_titan):
    lynx_titan["activities"].insert(3, {"id": 3, "name": "Brand New Boss", "rank": 7, "score": 42})
    user = Highscores('Lynx Titan')
    assert user.brand_new_boss.kills == '42'
    # Entries after the insertion are still matched by name, not position
    assert user.clue_scrolls_all.score == '22'


def test_update(mock_get):
    user = Highscores('Lynx Titan')
    original_query = user.time
    user.update()
    assert user.time >= original_query
    assert mock_get.call_count == 2


def test_target_url(mock_get):
    Highscores('dids', target='ironman')
    assert mock_get.call_args.args[0] == "https://secure.runescape.com/m=hiscore_oldschool_ironman/index_lite.json"


def test_invalid_target():
    with pytest.raises(ValueError):
        Highscores('Lynx Titan', target='not_a_target')


def test_player_not_found(no_sleep):
    with mock.patch("osrs_highscores.base.requests.get", return_value=make_response(404)) as get:
        with pytest.raises(ValueError):
            Highscores('Lynx Titan', target='ironman')
    assert get.call_count == 1


def test_retries_transient_errors(lynx_titan, no_sleep):
    responses = [requests.ConnectionError(), make_response(503), make_response(payload=lynx_titan)]
    with mock.patch("osrs_highscores.base.requests.get", side_effect=responses) as get:
        user = Highscores('Lynx Titan')
    assert int(user.attack.level) == 99
    assert get.call_count == 3


def test_gives_up_after_retries(no_sleep):
    with mock.patch("osrs_highscores.base.requests.get", side_effect=requests.ConnectionError()) as get:
        with pytest.raises(requests.ConnectionError):
            Highscores('Lynx Titan')
    assert get.call_count == 6


@pytest.mark.live
def test_live_lookup():
    user = Highscores('Lynx Titan')
    assert int(user.strength.level) == 99


@pytest.mark.live
def test_live_target_not_exist():
    with pytest.raises(ValueError):
        Highscores('Lynx Titan', target='ironman')
