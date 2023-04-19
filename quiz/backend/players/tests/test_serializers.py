import pytest
from rest_framework.exceptions import ValidationError

from players.serializers import PlayerSerializer


def test_player_serializer_serialization(player):
    data = PlayerSerializer(player).data

    assert data["username"] == player.nick
    assert data["uuid"] == f"{player.uuid}"


def test_player_serializer_deserialization(player):
    serializer = PlayerSerializer(data={"username": "test_nick"})
    serializer.is_valid(raise_exception=True)

    instance = serializer.save()

    assert instance.nick == "test_nick"


def test_player_serializer_passing_wrong_data(player):
    serializer = PlayerSerializer(data={"wrong_field": "test_nick"})

    with pytest.raises(ValidationError) as excinfo:
        serializer.is_valid(raise_exception=True)

        assert excinfo.value.detail == {"nick": ["This field is required."]}


def test_player_serializer_long_nick(player):
    serializer = PlayerSerializer(data={"nick": "test_nick" * 10})

    with pytest.raises(ValidationError) as excinfo:
        serializer.is_valid(raise_exception=True)

        assert excinfo.value.detail == {
            "nick": ["Ensure this field has no more than 30 characters."]
        }
