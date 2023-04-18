from factory.django import DjangoModelFactory, ImageField
from factory import Faker, Sequence, SubFactory

from backend.decks.models import Category, Flashcard, Deck, DifficultyLevel, Tag
from backend.users.factories import UserFactory


class CategoryFactory(DjangoModelFactory):
    """Factory for generating category of categories

    Usage is automated and it creates the instances of Category`.
    """

    name = Sequence(lambda n: f"Category {n:0>4}")
    description = Faker("sentence", nb_words=5)

    class Meta:
        model = Category
        django_get_or_create = ("name",)


class DeckFactory(DjangoModelFactory):
    """Factory for generating decks

    Usage is automated and it creates the instances of Decks`.
    """

    image = ImageField(color="blue")
    name = Faker("language_name")
    category = SubFactory(CategoryFactory)
    is_public = True
    price = Faker("pydecimal", right_digits=2, min_value=1, max_value=99)
    author = SubFactory(UserFactory)
    popularity = 0
    is_active = True
    description = Faker("sentence", nb_words=8)

    class Meta:
        model = Deck


class FlashcardFactory(DjangoModelFactory):
    """Factory for generating flashcards

    Usage is automated and it creates the instances of Flashcards`.
    """

    class Meta:
        model = Flashcard


class TagFactory(DjangoModelFactory):
    """Factory for generating TagFactory

    Usage is automated and it creates the instances of Tags`.
    """

    name = Faker("word")
    deck = SubFactory(DeckFactory)
    flashcard = SubFactory(FlashcardFactory)

    class Meta:
        model = Tag


class DifficultyLevelFactory(DjangoModelFactory):
    """Factory for generating difficulty level

    Usage is automated and it creates the instances of DifficultyLevel`.
    """

    name = Sequence(lambda n: f"Difficulty {n:0>2}")
    value = Faker("pyint", min_value=1, max_value=5)

    class Meta:
        model = DifficultyLevel
