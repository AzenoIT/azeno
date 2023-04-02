import json
from pathlib import Path

import pytest

from players.models import Player
from django.core.management import call_command

from players.views import PlayerCreateAPIView


@pytest.fixture
def player(db):
    return Player.objects.create(nick="John Doe")


@pytest.fixture
def player_bot(db):
    return Player.objects.create(nick="Sophia", is_bot=True)


@pytest.fixture
def generated_data_with_custom_command():
    """Fixture for calling create_test_data command

    :return func call_command: call_command
    """
    return call_command(
        "create_test_data",
        "5",
    )


@pytest.fixture
def api_rf():
    from rest_framework.test import APIRequestFactory

    return APIRequestFactory()


@pytest.fixture
def player_api(api_rf, db):
    def create_player():
        request = api_rf.post(
            "api/v1/players/",
            json.dumps({"nick": "test_nick"}),
            content_type="application/json",
        )
        view = PlayerCreateAPIView.as_view()
        return view(request)

    return create_player


@pytest.fixture
def adjectives_temp_file(tmp_path: Path) -> Path:
    """Fixture for substituting text file with adjectives for username generator.

    :return monkeypatch file: adj_temp_file
    """
    test_adj = [
        "silly",
        "outstanding",
        "talented",
    ]

    adj_temp_file = tmp_path / "temp_adjectives.txt"
    adj_temp_file.write_text("\n".join(test_adj))

    return adj_temp_file


@pytest.fixture
def nouns_temp_file(tmp_path: Path) -> Path:
    """Fixture for substituting text file with nouns for username generator.

    :return monkeypatch file: noun_temp_file
    """
    test_noun = [
        "Sod",
        "Archer",
        "Craftsman",
    ]

    noun_temp_file = tmp_path / "temp_nouns.txt"
    noun_temp_file.write_text("\n".join(test_noun))

    return noun_temp_file


@pytest.fixture
def profane_words_temp_file(tmp_path: Path) -> Path:
    """Creates a temporary path for profane words to test
    the validator function :function:`helpers.validators.validate_profanity`

    :param Path tmp_path: tmp_path fixture provided by pytest
    :return: Path file for test to use as base.
    """
    test_profane_words = ["fuckin", "boobs", "cunt", "kocha dzieci"]

    temp_file = tmp_path / "temp_profane_words.txt"
    temp_file.write_text("\n".join(test_profane_words))

    return temp_file
