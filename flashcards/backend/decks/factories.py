from factory import Faker, Sequence, SubFactory
from factory.django import DjangoModelFactory, ImageField
from .models import Category, Deck, Flashcard, Tag
from users.factories import UserFactory


class CategoryFactory(DjangoModelFactory):
    """Factory for generating flashcard/deck categories

    """
    class Meta:
        model = Category
        django_get_or_create = ("name",)

    name: Sequence = Sequence(lambda n: f"Category {n:0>4}")
    description: Faker = Faker("sentence", nb_words=5)


class DeckFactory(DjangoModelFactory):
    """Factory for generating decks

    """
    class Meta:
        model = Deck

    image: ImageField = ImageField(color="blue")
    name: Faker = Faker("language_name")
    category: SubFactory = SubFactory(CategoryFactory)
    is_public: bool = True
    price: Faker = Faker("pydecimal", right_digits=2, min_value=1, max_value=99)
    author: SubFactory = SubFactory(UserFactory)
    popularity: int = 0
    is_active: bool = True
    description: Faker = Faker("sentence", nb_words=8)


class FlashcardFactory(DjangoModelFactory):
    """Factory for generating flashcards

    """

    class Meta:
        model = Flashcard


class TagFactory(DjangoModelFactory):
    """Factory for generating tags

    """
    class Meta:
        model = Tag

    name: Faker = Faker("word")
    deck: SubFactory = SubFactory(DeckFactory)
    flashcard: SubFactory = SubFactory(FlashcardFactory)
