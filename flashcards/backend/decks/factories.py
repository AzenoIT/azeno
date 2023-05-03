from factory import Faker, Sequence, SubFactory, LazyAttribute
from factory.django import DjangoModelFactory, ImageField

from decks.models import Category, Deck, Flashcard, Tag, DifficultyLevel
from users.factories import UserFactory


class CategoryFactory(DjangoModelFactory):
    """Factory for generating flashcard/deck categories

    Usage is automated with custom command and combined with test user data generation,
    described in :doc:`users.management.commands`.
    """

    class Meta:
        model = Category
        django_get_or_create = ("name",)

    name = Sequence(lambda n: f"Category {n:0>4}")
    description: Faker = Faker("sentence", nb_words=5)


class DifficultyLevelFactory(DjangoModelFactory):
    """Factory for generating difficulty level

    Usage is automated with custom command and combined with test user data generation,
    described in :doc:`users.management.commands`.
    """

    class Meta:
        model = DifficultyLevel
        django_get_or_create = ("value",)

    value: Faker = Faker("pyint", min_value=1, max_value=10)
    name: LazyAttribute = LazyAttribute(lambda a: "Difficulty " + str(a.value))


class DeckFactory(DjangoModelFactory):
    """Factory for generating decks

    Usage is automated with custom command and combined with test user data generation,
    described in :doc:`users.management.commands`.
    """

    class Meta:
        model = Deck

    image = ImageField(color="blue")
    name: Faker = Faker("language_name")
    category: SubFactory = SubFactory(CategoryFactory)
    difficulty_level: SubFactory = SubFactory(DifficultyLevelFactory)
    is_public = True
    price: Faker = Faker("pydecimal", right_digits=2, min_value=1, max_value=99)
    author: SubFactory = SubFactory(UserFactory)
    popularity = 0
    is_active = True
    description: Faker = Faker("sentence", nb_words=8)


class FlashcardFactory(DjangoModelFactory):
    """Factory for generating flashcards"""

    class Meta:
        model = Flashcard


class TagFactory(DjangoModelFactory):
    """Factory for generating tags

    Usage is automated with custom command and combined with test user data generation,
    described in :doc:`users.management.commands`.
    """

    class Meta:
        model = Tag

    name: Faker = Faker("bothify", text="Tag_???-###")
    deck: SubFactory = SubFactory(DeckFactory)
    flashcard: SubFactory = SubFactory(FlashcardFactory)
