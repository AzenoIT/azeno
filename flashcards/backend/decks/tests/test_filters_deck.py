from datetime import datetime
from django.test import Client

from decks.models import Deck


def test_filter_deck_name_exact(db, user, category, difficulty_level, image):
    client = Client()
    deck = Deck.objects.create(
        image=image,
        name="test",
        category=category,
        difficulty_level=difficulty_level,
        author_id=user.id,
        description="test",
        price=42.00,
        updated_at=datetime.now(),
    )
    queryset = deck.filter_queryset(deck.get_queryset().order_by("-rating")).filter(name__exact=deck.name)
    response = client.get("decks/?name__exact=test")
    assert deck == queryset
