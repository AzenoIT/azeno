from rest_framework import status

from players.views import NicknameGeneratorAPIView


def test_nickname_generator_view_returns_correct_data(api_rf):
    request = api_rf.get("/api/v1/players/username/")
    response = NicknameGeneratorAPIView.as_view()(request)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 10
