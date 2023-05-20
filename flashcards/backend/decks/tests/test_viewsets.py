from decks.viewsets import DeckViewSet
from rest_framework import status
from rest_framework.test import force_authenticate

from decks.models import Deck
from decks.serializers import DeckSerializer


def test_deck_viewsets_retrieve_deck_found(deck, api_request_factory):
    url = "/api/v1/decks/1/"
    view = DeckViewSet.as_view({"get": "retrieve"})

    request = api_request_factory.get(url)
    response = view(request, pk=deck.id)

    assert response.status_code == 200
    assert response.data["name"] == deck.name
    assert response.data["id"] == deck.id
    assert response.data["category"]["name"] == deck.category.name


def test_deck_viewsets_list_deck_found(deck, api_request_factory):
    url = "/api/v1/decks/"
    view = DeckViewSet.as_view({"get": "list"})

    request = api_request_factory.get(url)
    response = view(request)

    assert response.status_code == 200


def test_viewset_create_deck_with_default_image(category, api_request_factory, db, user, difficulty_level):
    url = "/api/v1/decks/1"
    view = DeckViewSet.as_view({"post": "create"})
    deck_ = {
        "name": "Test Deck",
        "description": "Test description",
        "price": 10,
        "category_id": category.pk,
        "difficulty_level": difficulty_level.pk,
        "author": user.pk,
    }

    request = api_request_factory.post(url, data=deck_, format="multipart")
    force_authenticate(request, user=user)
    response = view(request)

    assert response.status_code == status.HTTP_201_CREATED
    deck = Deck.objects.first()
    serializer = DeckSerializer(deck)
    assert serializer.data == response.data
    assert serializer.data["image"] is not None


def test_create_deck_with_custom_image(category, api_request_factory, db, user, uploaded_image, difficulty_level):
    url = "/api/v1/decks/1"
    view = DeckViewSet.as_view({"post": "create"})
    deck_ = {
        "name": "Test Deck",
        "description": "Test description",
        "price": 10,
        "category_id": category.pk,
        "difficulty_level": difficulty_level.pk,
        "author": user.pk,
        "image": uploaded_image,
    }

    request = api_request_factory.post(url, data=deck_, format="multipart")
    force_authenticate(request, user=user)
    response = view(request)

    assert response.status_code == status.HTTP_201_CREATED
    deck = Deck.objects.first()
    serializer = DeckSerializer(deck)
    assert serializer.data == response.data
    assert serializer.data["image"] != serializer.data["category"]["image"]


def test_viewset_create_deck_with_invalid_data(category, api_request_factory, db, user):
    url = "/api/v1/decks/1"
    view = DeckViewSet.as_view({"post": "create"})
    deck_ = {}

    request = api_request_factory.post(url, data=deck_, format="multipart")
    force_authenticate(request, user=user)
    response = view(request)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert str(response.data["name"][0]) == "This field is required."
    assert str(response.data["category_id"][0]) == "This field is required."
    assert str(response.data["price"][0]) == "This field is required."
    assert str(response.data["description"][0]) == "This field is required."
