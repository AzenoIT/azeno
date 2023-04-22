from decks import factories
from decks.pagination import DecksPagination
from decks.viewsets import DeckViewSet


def test_deck_list_pagination(api_request_factory, db):
    factories.DeckFactory.create_batch(DecksPagination.max_limit + 1)

    url = f"/api/v1/decks/?limit={DecksPagination.max_limit + 1}&offset=0"
    view = DeckViewSet.as_view({"get": "list"})

    request = api_request_factory.get(url)
    response = view(request)

    assert len(response.data["results"]) == DecksPagination.max_limit
