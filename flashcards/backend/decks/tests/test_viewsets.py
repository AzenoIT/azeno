from decks.viewsets import DeckViewSet


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
