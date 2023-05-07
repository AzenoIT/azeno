from datetime import datetime

from decks.models import Deck


def test_filter_deck_name_exact(db, user, category, difficulty_level, image):
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
    pass
