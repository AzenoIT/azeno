import io
import os
import shutil
from datetime import datetime, timedelta
from _decimal import Decimal

import pytest
from PIL import Image
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import call_command
from django.test import override_settings

from config import settings
from comments.models import Comment
from decks.models import Category, Deck, Flashcard, Tag, DifficultyLevel
from players.models import AccountType
from stats.models import FlashcardStudy, DeckStudy


@pytest.fixture
@override_settings(DEBUG=True)
def generated_data_with_custom_command(settings, db):
    """Fixture for calling create_test_data command
    :return func call_command: call_command
    """
    return call_command(
        "create_test_data",
        "--decks=3",
        "--users=5",
        "--categories=3",
        "--tags=2",
        "--difficulties=1",
    )


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
def category(db, image):
    """Fixture for create category with saving to database.
    :return: Object of class Category representing a row in table.
    :rtype: Category
    """
    name = "test category"
    description = "test category description"

    return Category.objects.create(name=name, description=description, image=image)


@pytest.fixture
def difficulty_level(db):
    """Fixture that will create databased saved difficulty object.
    :return: Object of class DifficultyLevel representing a row in table.
    :rtype: DifficultyLevel
    """
    name = "Hard"
    value = 1
    return DifficultyLevel.objects.create(name=name, value=value)


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
def deck(db, user, category, difficulty_level, image):
    """Fixture for creating deck with image.
    :return: Object of class Deck representing a row in table.
    :rtype: Deck
    """
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
    return deck


@pytest.fixture
def remove_test_data():
    """Fixture for removing test data.
    :return: None
    :rtype: None
    """
    yield
    shutil.rmtree(os.path.join(settings.BASE_DIR, "test_dir"), ignore_errors=True)


@pytest.fixture
def flashcard(db):
    return Flashcard.objects.create()


@pytest.fixture
def tag_db(db, deck, flashcard):
    """Fixture for creating a tag  with saving to database.
    :return: Object of class Tag representing a row in table.
    :rtype: Tag
    """

    tag = Tag.objects.create(name="tag_2")
    tag.flashcards.add(flashcard)
    tag.decks.add(deck)
    return tag


@pytest.fixture
def account_type(db):
    """Fixture for creating account type with saving to database.
    :return: Object of class AccountType representing a row in table.
    :rtype: AccountType
    """
    return AccountType.objects.create(name="Basic", duration=timedelta(days=60), cost=Decimal(10))


@pytest.fixture
def flashcard_study(db, user, flashcard):
    """Fixture for creating a flashcard study instance with saving to database.
    :return: Object of class FlashcardStudy representing a row in table.
    :rtype: FlashcardStudy
    """
    return FlashcardStudy.objects.create(user=user, study_date=datetime.now(), correct_answers=2, flashcard=flashcard)


@pytest.fixture
def deck_study(db, user, deck):
    """Fixture for creating a deck study instance with saving to database.
    :return: Object of class DeckStudy representing a row in table.
    :rtype: DeckStudy
    """
    return DeckStudy.objects.create(
        user=user,
        study_date=datetime.now(),
        correct_answers=3,
        deck=deck,
        study_duration=timedelta(hours=1),
        realization=Decimal(42),
    )


@pytest.fixture
def comment(db, user, flashcard, deck):
    """Fixture for creating a comment with saving to database.
    :return: Object of class Comment representing a row in table.
    :rtype: Comment
    """
    return Comment.objects.create(user=user, flashcard=flashcard, deck=deck, comment="This is a test comment.")


@pytest.fixture
def api_request_factory():
    """Fixture for creating request instance.
    :return: APIRequestFactory instance.
    :rtype: APIRequestFactory
    """
    from rest_framework.test import APIRequestFactory

    return APIRequestFactory()


@pytest.fixture
def uploaded_image():
    """Fixture for creating and saving image file in JPEG format.
    :return: Object of class SimpleUploadedFile representing a file.
    :rtype: SimpleUploadedFile
    """
    img = Image.new("RGB", (50, 50), color=(255, 0, 0))
    image_data = io.BytesIO()
    img.save(image_data, format="jpeg")

    uploaded_image = SimpleUploadedFile(
        "test_image.jpeg",
        image_data.getvalue(),
        content_type="image/jpeg",
    )

    return uploaded_image
