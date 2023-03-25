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

