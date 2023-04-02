import pytest

from django.core.management import call_command
from django.test import override_settings

from decks.models import Category, DifficultyLevel


@pytest.fixture
@override_settings(DEBUG=True)
def generated_data_with_custom_command(settings, db):
    """Fixture for calling create_test_data command
    :return func call_command: call_command
    """
    return call_command(
        "create_test_data",
        "5",
    )


@pytest.fixture
def category(db):
    """Fixture for create category with saving to database.
    :return: Object of class Category representing a row in table.
    :rtype: Category
    """
    name = "test category"
    description = "test category description"

    return Category.objects.create(name=name, description=description)


@pytest.fixture
def difficulty_level(db):
    """Fixture that will create databased saved difficulty object.
    :return: Object of class DifficultyLevel representing a row in table.
    :rtype: DifficultyLevel
    """
    return DifficultyLevel.objects.create(name="Hard", value=1)
