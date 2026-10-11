import json
import pathlib
from unittest import mock

import pytest
import requests

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


def make_response(status_code=200, payload=None, content=b""):
    response = mock.Mock()
    response.status_code = status_code
    response.content = content
    response.json.return_value = payload
    if status_code >= 400:
        response.raise_for_status.side_effect = requests.HTTPError(str(status_code))
    else:
        response.raise_for_status.return_value = None
    return response


@pytest.fixture
def lynx_titan():
    return json.loads((FIXTURES / "lynx_titan.json").read_text())


@pytest.fixture
def no_sleep(monkeypatch):
    monkeypatch.setattr("osrs_highscores.base.time.sleep", lambda _: None)
    monkeypatch.setattr("osrs_highscores.rankings.time.sleep", lambda _: None)
