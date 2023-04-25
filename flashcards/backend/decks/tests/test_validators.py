import pytest

from django.core.exceptions import ValidationError
from decks.models import Deck
from decks.validators import validate_file_type

from django.core.files.base import ContentFile
from django.conf import settings
from unittest.mock import MagicMock, patch
from PIL import Image
from contextlib import contextmanager

from decks.validators import validate_image_file_type, validate_image_file_size


def test_negative_price_raises_value_error(user, db):
    deck = Deck(
        name="test",
        author_id=user.id,
        description="test",
        price=-1,
    )
    with pytest.raises(ValidationError) as excinfo:
        deck.full_clean()
    assert "Ensure this value is greater than or equal to 0.00" in str(excinfo.value)


def test_valid_image(image):
    assert not validate_file_type(image)


def test_not_valid_image_with_correct_extension(image):
    image.write(b"test not valid type")

    with pytest.raises(ValidationError) as excinfo:
        validate_file_type(image)

    assert excinfo.value.args[0] == f'Unsupported file type. Use: {", *.".join(settings.IMAGES_TYPES)}.'


def test_not_valid_image_with_incorrect_extension(image):
    image.write(b"test not valid type")
    image.name = "test.txt"

    with pytest.raises(ValidationError) as excinfo:
        validate_file_type(image)

    assert excinfo.value.args[0] == f'Unsupported file type. Use: {", *.".join(settings.IMAGES_TYPES)}.'


def test_image_with_invalid_size(image, user, category):
    image.size = settings.MAX_UPLOAD_SIZE + 1
    deck = Deck(
        image=image,
        category=category,
        name="test",
        author_id=user.id,
        description="test",
        price=1,
    )
    with pytest.raises(ValidationError) as excinfo:
        deck.full_clean()
    assert f"File size is too big. Max size is {settings.MAX_UPLOAD_SIZE} bytes." in str(excinfo.value)


def create_image_mock(width, height, file_type):
    image_mock = MagicMock(spec=Image)
    image_mock.size = (width, height)
    image_mock.format = file_type.upper()
    return image_mock


@contextmanager
def image_open_context_manager(image_mock):
    yield image_mock


@pytest.mark.parametrize("file_type,width,height", [("jpeg", 800, 600)])
def test_validate_file_type_valid_resolution(file_type, width, height):
    upload = MagicMock()
    upload.file = ContentFile(b"dummy_content")
    upload.name = f"test.{file_type}"
    image_mock = create_image_mock(width, height, file_type)

    with patch("magic.from_file", return_value=f"image/{file_type}"):
        with patch("PIL.Image.open", return_value=image_open_context_manager(image_mock)):
            validate_image_file_type(upload)


@pytest.mark.parametrize("size", [settings.MAX_UPLOAD_SIZE - 1024, settings.MAX_UPLOAD_SIZE // 2, 1024])
def test_validate_file_size_valid(size):
    file = MagicMock()
    file.size = size

    validate_image_file_size(file)
