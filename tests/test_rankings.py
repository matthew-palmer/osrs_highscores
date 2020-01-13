import pytest
from osrs_highscores.rankings import Rankings


def test_lookup_skill():
    rank = Rankings().get_rank_in_skill('attack', 1)
    assert rank.rank == 1


def test_lookup_nonskill():
    rank = Rankings().get_rank_in_target('clue_scrolls_all', 1)
    assert rank.score != 0
