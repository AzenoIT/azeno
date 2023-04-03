from datetime import timedelta

from rest_framework import status

from players.models import AccountType
from players.views import AccountTypeListAPIView, PlayerListAPIView


def test_account_types_list(account_type, api_rf):
    account_type = AccountType(name="Plus", duration=timedelta(days=60), cost=10)
    url = "/api/v1/accounts/"
    view = AccountTypeListAPIView.as_view()

    request = api_rf.get(url)
    response = view(request)

    assert response.status_code == status.HTTP_200_OK


def test_players_list(db, api_rf):
    url = "/api/v1/players/"
    view = PlayerListAPIView.as_view()

    request = api_rf.get(url)
    response = view(request)

    assert response.status_code == status.HTTP_200_OK
