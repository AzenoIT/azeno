import json

import pytest

from players.models import Player
from django.core.management import call_command

from players.views import PlayerCreateAPIView


@pytest.fixture
def player(db):
    return Player.objects.create(nick="John Doe")


@pytest.fixture
def player_bot(db):
    return Player.objects.create(nick="Sophia", is_bot=True)


@pytest.fixture
def generated_data_with_custom_command():
    """Fixture for calling create_test_data command

    :return func call_command: call_command
    """
    return call_command(
        "create_test_data",
        "5",
    )


@pytest.fixture
def api_rf():
    from rest_framework.test import APIRequestFactory

    return APIRequestFactory()


@pytest.fixture
def player_api(api_rf, db):
    def create_player():
        request = api_rf.post(
            "api/v1/players/",
            json.dumps({"nick": "test_nick"}),
            content_type="application/json",
        )
        view = PlayerCreateAPIView.as_view()
        return view(request)

    return create_player
