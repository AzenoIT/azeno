import pytest
from django.core.exceptions import ValidationError
from config import settings
from decks.models import Deck
from decks.validators import validate_file_type


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
