from factory import Faker
from factory.django import DjangoModelFactory
from .models import Category


class CategoryFactory(DjangoModelFactory):
    """Factory for generating flashcard/deck categories

    """
    class Meta:
        model = Category

    name: Faker = Faker("language_name")
    description: Faker = Faker("sentence", nb_words=5)
