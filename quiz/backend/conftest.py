from pathlib import Path

import pytest

from players.models import Player
from django.core.management import call_command


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
