import pytest
from django.core.exceptions import ValidationError

from players.models import Player


def test_object_representation_in_gui():
    player = Player(nick="testPlayer")

    assert str(player) == "testPlayer"


def test_bot_creation(player_bot):
    players = Player.objects.all()
    assert player_bot in players


@pytest.mark.parametrize(
    "nick",
    [
        "prettyNick",
        "nicePerson",
        "testNick",
    ],
)
def test_player_nick_validates_non_profane_nick(nick, db):
    Player.objects.create(
        nick=nick,
    )
    saved_player = Player.objects.get(nick=nick)
    assert saved_player.nick == nick


@pytest.mark.parametrize(
    "nick",
    [
        "fuckinMonkey",
        "cuntFace",
        "boobs_rock",
        "JP2-kocha-dzieci",
    ],
)
def test_player_nick_raises_validation_error_for_profane_nick(nick, db):
    with pytest.raises(ValidationError) as excinfo:
        Player.objects.create(
            nick=nick,
        )
    assert "This name contains profane word:" in str(excinfo.value)
