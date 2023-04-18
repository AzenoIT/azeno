import pytest

from decks.factories import CategoryFactory, DeckFactory, FlashcardFactory, TagFactory, DifficultyLevelFactory
from decks.models import Category, Tag, User


@pytest.mark.django_db
def test_category_factory():
    """Test CategoryFactory."""
    category = CategoryFactory()
    assert category.pk is not None
    assert str(category) == category.name
    assert Category(name="test category", description="test category description")
    assert isinstance(category.description, str)


@pytest.mark.django_db
def test_deck_factory():
    """Test DeckFactory."""
    deck = DeckFactory()
    assert deck is not None
    assert isinstance(deck.image.url, str)
    assert str(deck) == deck.name
    assert isinstance(deck.category, Category)
    assert deck.is_public is True
    assert deck.price > 0
    assert isinstance(deck.author, User)
    assert deck.popularity == 0
    assert deck.is_active is True
    assert isinstance(deck.description, str)


@pytest.mark.django_db
def test_flashcard_factory():
    """Test FlashcardFactory."""
    flashcard = FlashcardFactory()
    assert flashcard is not None


@pytest.mark.django_db
def test_tag_factory():
    """Test TagFactory."""
    tag = TagFactory()
    assert tag.name is not None
    assert str(tag) == tag.name


@pytest.mark.django_db
def test_difficulty_level_factory():
    """Test DifficultyLevelFactory."""
    difficulty_level = DifficultyLevelFactory()
    assert difficulty_level.pk is not None
    assert str(difficulty_level) == difficulty_level.name
    assert difficulty_level.value > 0
