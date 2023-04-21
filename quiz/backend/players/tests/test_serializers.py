import pytest
from rest_framework.exceptions import ValidationError

from players.serializers import PlayerSerializer, PlayerDetailSerializer


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


def test_player_detail_serializer_serialization(player):
    data = PlayerDetailSerializer(player).data

    assert data["username"] == player.nick
    assert data["uuid"] == f"{player.uuid}"
    assert data["rank"] == player.rank
    assert data["created_at"] == player.created_at.strftime("%Y-%m-%dT%H:%M:%S.%fZ")


def test_player_detial_serializer_deserialization(player):
    serializer = PlayerDetailSerializer(
        data={"username": "test_nick", "rank": 1}, instance=player
    )
    serializer.is_valid(raise_exception=True)

    instance = serializer.save()

    assert instance.nick == "test_nick"
    assert instance.rank == 1
