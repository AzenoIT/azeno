import json

from players.views import PlayerCreateAPIView


def test_player_view_return_201_status_code_and_correct_data(player_api):
    response = player_api()

    assert response.status_code == 201
    assert response.data["nick"] == "test_nick"
    assert all(prop in response.data for prop in ["uuid", "rank", "created_at"])


def test_player_view_create_player_save_in_db(player_api):
    response = player_api()

    assert PlayerCreateAPIView.queryset.get(uuid=response.data["uuid"])
