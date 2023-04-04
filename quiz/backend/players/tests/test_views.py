from rest_framework import status
from players.views import NicknameGeneratorAPIView, PlayerCreateAPIView


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
