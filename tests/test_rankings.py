from unittest import mock

import pytest

from osrs_highscores.rankings import Rankings
from .conftest import make_response

PAGE = b"""<html><body><table><tbody>
<tr><td>1</td><td>Lynx Titan</td><td>99</td><td>200,000,000</td></tr>
<tr><td>2</td><td>Someone\xc2\xa0Else</td><td>99</td><td>199,999,999</td></tr>
</tbody></table></body></html>"""

ACTIVITY_PAGE = b"""<html><body><table><tbody>
<tr><td>26</td><td>Clue Hunter</td><td>12,345</td></tr>
</tbody></table></body></html>"""


def test_lookup_skill(lynx_titan, no_sleep):
    responses = [make_response(payload=lynx_titan), make_response(content=PAGE)]
    with mock.patch("osrs_highscores.base.requests.get", side_effect=responses) as get:
        rank = Rankings().get_rank_in_skill('attack', 1)
    assert rank.rank == 1
    assert rank.username == 'Lynx Titan'
    assert rank.xp == '200000000'
    assert get.call_args.args[0] == "https://secure.runescape.com/m=hiscore_oldschool/overall.ws"
    assert get.call_args.kwargs["params"] == {"table": 1, "page": 1}


def test_lookup_nonskill_uses_live_table_ids(lynx_titan, no_sleep):
    responses = [make_response(payload=lynx_titan), make_response(content=ACTIVITY_PAGE)]
    with mock.patch("osrs_highscores.base.requests.get", side_effect=responses) as get:
        rank = Rankings(target='ironman').get_rank_in_target('the_royal_titans', 26)
    assert rank.score == '12345'
    assert get.call_args.args[0] == "https://secure.runescape.com/m=hiscore_oldschool_ironman/overall.ws"
    assert get.call_args.kwargs["params"] == {"category_type": 1, "table": 71, "page": 2}


def test_table_ids_fall_back_when_offline(no_sleep):
    responses = [make_response(404), make_response(content=PAGE)]
    with mock.patch("osrs_highscores.base.requests.get", side_effect=responses) as get:
        rank = Rankings().get_rank_in_skill('attack', 1)
    assert rank.level == '99'
    assert get.call_args.kwargs["params"] == {"table": 1, "page": 1}


@pytest.mark.live
def test_live_lookup_skill():
    rank = Rankings().get_rank_in_skill('attack', 1)
    assert rank.rank == 1
