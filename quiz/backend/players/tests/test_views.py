import json

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
    assert response.data["username"] == "test_nick"
    assert all(prop in response.data for prop in ["uuid", "username"])


def test_player_view_create_player_save_in_db(player_api):
    response = player_api()

    assert PlayerCreateAPIView.queryset.get(uuid=response.data["uuid"])


def test_retrieve_player_view_returns_data(player_api, api_rf):
    player = player_api()
    request = api_rf.get(f"/api/v1/players/{player.data['uuid']}/")
    response = PlayerRetrieveAPIView.as_view()(request, uuid=player.data["uuid"])

    assert response.status_code == 200
    assert response.data["username"] == player.data["username"]
    assert response.data["uuid"] == str(player.data["uuid"])


def test_retrieve_player_view_with_wrong_uuid_returns_404(player_api, api_rf):
    player = player_api()
    request = api_rf.get(f"/api/v1/players/{player.data['uuid']}/")
    response = PlayerRetrieveAPIView.as_view()(
        request, uuid=f'{player.data["uuid"] + "1"}'
    )

    assert response.status_code == 404


def test_put_player_view_returns_200_status_code(player_api, api_rf):
    player = player_api()
    request = api_rf.put(
        f"/api/v1/players/{player.data['uuid']}/",
        json.dumps({"username": "new_username", "rank": 1}),
        content_type="application/json",
    )
    response = PlayerRetrieveAPIView.as_view()(request, uuid=player.data["uuid"])

    assert response.status_code == 200
    assert response.data["username"] == "new_username"
