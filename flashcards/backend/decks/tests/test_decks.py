from django.test import TestCase

from backend.decks.factories import CategoryFactory, DeckFactory, FlashcardFactory, TagFactory, DifficultyLevelFactory


class TestFactories(TestCase):
    def test_category_factory(self):
        """Test CategoryFactory."""
        category = CategoryFactory()
        self.assertIsNotNone(category)
        self.assertIsNotNone(category.name)
        self.assertIsNotNone(category.description)

    def test_deck_factory(self):
        """Test DeckFactory."""
        deck = DeckFactory()
        self.assertIsNotNone(deck)
        self.assertIsNotNone(deck.image)
        self.assertIsNotNone(deck.name)
        self.assertIsNotNone(deck.category)
        self.assertTrue(deck.is_public)
        self.assertIsNotNone(deck.price)
        self.assertIsNotNone(deck.author)
        self.assertEqual(deck.popularity, 0)
        self.assertTrue(deck.is_active)
        self.assertIsNotNone(deck.description)

    def test_flashcard_factory(self):
        """Test FlashcardFactory."""
        flashcard = FlashcardFactory()
        self.assertIsNotNone(flashcard)

    def test_tag_factory(self):
        """Test TagFactory."""
        tag = TagFactory()
        self.assertIsNotNone(tag)
        self.assertIsNotNone(tag.name)
        self.assertIsNotNone(tag.deck)
        self.assertIsNotNone(tag.flashcard)

    def test_difficulty_level_factory(self):
        """Test DifficultyLevelFactory."""
        difficulty_level = DifficultyLevelFactory()
        self.assertIsNotNone(difficulty_level)
        self.assertIsNotNone(difficulty_level.name)
        self.assertIsNotNone(difficulty_level.value)
