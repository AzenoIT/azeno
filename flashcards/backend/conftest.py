import io
import json
import os
import shutil
import tempfile
from datetime import datetime
from pathlib import Path

import pytest
from PIL import Image
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile

from django.core.management import call_command
from django.test import override_settings
from factory import faker
from faker import factory

from decks.models import Category, Deck, Flashcard, Tag, DifficultyLevel
from decks.factories import DeckFactory
from config import settings


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
def user(db):
    """Fixture for creating user.
    :return: Object of class User representing a row in table.
    :rtype: User
    """
    User = get_user_model()
    user = User.objects.create_user(email="test_email@com.pl", username="test_username", password="test_password")
    return user


@pytest.fixture
@override_settings(MEDIA_ROOT=os.path.join(settings.BASE_DIR, "test_dir", "media"))
def deck(db, user, category, image):
    """Fixture for creating deck with image.
    :return: Object of class Deck representing a row in table.
    :rtype: Deck
    """
    deck = Deck.objects.create(
        image=image,
        name="test",
        category=category,
        author_id=user.id,
        description="test",
        price=42.00,
        updated_at=datetime.now(),
    )
    return deck


@pytest.fixture
def image(name="test.png", suffix="PNG", size=(50, 50), color="red"):
    """Fixture for creating image file.
    :param name: name of image file
    :type name: str
    :param suffix: suffix of image file
    :type suffix: str
    :param size: size of image file
    :type size: tuple
    :param color: color of image file
    :type color: str
    :return: Object of class SimpleUploadedFile representing a file.
    :rtype: SimpleUploadedFile
    """

    image = Image.new("RGB", size=size, color=color)
    file = io.BytesIO()
    image.save(file, format=suffix)
    file.seek(0)

    return SimpleUploadedFile(name, file.read(), content_type="image/png")


@pytest.fixture
def remove_test_data():
    """Fixture for removing test data.
    :return: None
    :rtype: None
    """
    yield
    shutil.rmtree(os.path.join(settings.BASE_DIR, "test_dir"), ignore_errors=True)


@pytest.fixture
def tag_db(db, deck, flashcard):
    name = "tag_2"
    deck = deck
    flashcard = flashcard

    return Tag.objects.create(name=name, deck=deck, flashcard=flashcard)


@pytest.fixture
def flashcard(db):
    return Flashcard.objects.create()


@pytest.fixture
def difficulty_level(db):
    """Fixture that will create databased saved difficulty object.
    :return: Object of class DifficultyLevel representing a row in table.
    :rtype: DifficultyLevel
    """
    return DifficultyLevel.objects.create(name="Hard", value=1)


@pytest.fixture(scope="session")
def flashcard_decks():
    """Factory for generating decks

    after usage this fixture creates 50 decks and dumps them into fixtures folder to decks.json file`.
    """

    decks = DeckFactory.create_batch(50)
    decks_data = []
    for deck in decks:
        decks_data.append(
            {
                "model": "decks.Deck",
                "pk": deck.pk,
                "fields": {
                    "image": str(deck.image),
                    "name": deck.name,
                    "category": deck.category.pk,
                    "is_public": deck.is_public,
                    "price": str(deck.price),
                    "author": deck.author.pk,
                    "popularity": deck.popularity,
                    "is_active": deck.is_active,
                    "description": deck.description,
                },
            }
        )

    fixture_dir = Path(__file__).parent / "fixtures"
    fixture_dir.mkdir(exist_ok=True)

    with open(fixture_dir / "decks.json", "w") as f:
        json.dump(decks_data, f)

    return decks
