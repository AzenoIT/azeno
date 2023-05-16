import os
from datetime import datetime


def test_correct_gui_representation(deck, remove_test_data):
    assert str(deck) == "test"


def test_deck_creation(deck, remove_test_data, user):
    assert os.path.basename(deck.image.name) == "test.png"
    assert deck.image.url == "/media/decks/test.png"
    assert deck.name == "test"
    assert deck.author.id == user.id
    assert deck.description == "test"
    assert deck.price == 42.00
    assert isinstance(deck.updated_at, datetime)


def test_deck_fields(deck, remove_test_data):
    assert [*vars(deck)] == [
        "_state",
        "id",
        "created_at",
        "updated_at",
        "image",
        "name",
        "category_id",
        "difficulty_level_id",
        "is_public",
        "price",
        "author_id",
        "popularity",
        "rating",
        "is_active",
        "description",
    ]
