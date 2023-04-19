import uuid

import pytest

from .. import models
from rest_framework import status
from players.views import (
    NicknameGeneratorAPIView,
    PlayerCreateAPIView,
    PlayerRetrieveAPIView,
)


def test_nickname_generator_view_returns_correct_data(api_rf):
    request = api_rf.get("/api/v1/players/username/")
    response = NicknameGeneratorAPIView.as_view()(request)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 10


def test_player_view_return_201_status_code_and_correct_data(player_api):
    response = player_api()

    assert response.status_code == 201
    assert response.data["nick"] == "test_nick"
    assert all(prop in response.data for prop in ["uuid", "rank", "created_at"])


def test_player_view_create_player_save_in_db(player_api):
    response = player_api()

    assert PlayerCreateAPIView.queryset.get(uuid=response.data["uuid"])


def test_retrieve_player_view_returns_data(profile_data, api_rf):
    url = f"/api/v1/players/{profile_data.player.uuid}/"
    request = api_rf.get(url, content_type="application/json")
    response = PlayerRetrieveAPIView.as_view()(request, uuid=profile_data.player.uuid)

    assert response.status_code == 200
    assert response.data["nick"] == profile_data.player.nick
    assert response.data["uuid"] == str(profile_data.player.uuid)


def test_retrieve_player_view_with_wrong_uuid_returns_404(profile_data, api_rf):
    random_uuid = str(uuid.uuid4())
    request = api_rf.get(f"/api/v1/players/{random_uuid}/")
    response = PlayerRetrieveAPIView.as_view()(
        request, uuid=f'{random_uuid}'
    )

    assert response.status_code == 404
