import pytest

from players.models import Player


@pytest.fixture
def player(db):
    return Player.objects.create(nick="John Doe")


@pytest.fixture
def player_bot(db):
    return Player.objects.create(nick="Sophia", is_bot=True)
