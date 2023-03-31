from players.views import NicknameGeneratorAPIView


def test_nickname_generator_view_returns_correct_data(api_rf):
    request = api_rf.get("/players/nickname-generator/")
    response = NicknameGeneratorAPIView.as_view()(request)

    assert response.status_code == 200
    assert len(response.data) == 1


def test_nickname_generator_view_returns_correct_data_with_count_query_param(api_rf):
    request = api_rf.get("/players/nickname-generator/", {"count": 5})
    response = NicknameGeneratorAPIView.as_view()(request)

    assert response.status_code == 200
    assert len(response.data) == 5
