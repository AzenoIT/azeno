import pytest
from rest_framework import status

from stats.models import Badge
from stats.views import BadgeListView, BadgeRetrieveView


def test_badge_retrieve_view(badge, api_rf):
    url = f"/api/v1/badges/{badge.pk}/"
    view = BadgeRetrieveView.as_view()
    request = api_rf.get(url, format="json")
    response = view(request, pk=badge.pk)
    response.render()

    assert response.status_code == status.HTTP_200_OK
    assert b'"name":"Test badge"' in response.content


def test_badge_retrieve_view_404_status(badge, api_rf):
    url = "/api/v1/badges/5/"
    view = BadgeRetrieveView.as_view()
    request = api_rf.get(url, format="json")
    response = view(request, pk=5)
    response.render()

    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_badge_list_view(badge, api_rf):
    url = "/api/v1/badges/"
    view = BadgeListView.as_view()
    request = api_rf.get(url, format="json")
    response = view(request)
    response.render()

    assert response.status_code == status.HTTP_200_OK
    assert b'"name":"Test badge"' in response.content
