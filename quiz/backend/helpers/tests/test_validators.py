from io import BytesIO

import pytest
from django.core.exceptions import ValidationError

from helpers.validators.validators import (
    validate_profanity,
    validate_badge_file_type,
    validate_avatar_file_type_and_dimensions,
)


@pytest.mark.parametrize(
    "username",
    [
        "analyticalMonkey",
        "assertivePesto",
        "vibrantArrow",
    ],
)
def test_validate_profanity_not_profane_usernames(
    username, monkeypatch, profane_words_temp_file
):
    monkeypatch.setattr(
        "helpers.validators.validators.PROFANE_WORDS_FILE", str(profane_words_temp_file)
    )

    assert validate_profanity(username) is None


@pytest.mark.parametrize(
    "username",
    ["fuckinMonkey", "cuntFace", "boobs_rock", "JP2-kocha-dzieci"],
)
def test_validate_profanity_profane_usernames(
    username, monkeypatch, profane_words_temp_file
):
    monkeypatch.setattr(
        "helpers.validators.validators.PROFANE_WORDS_FILE", str(profane_words_temp_file)
    )

    with pytest.raises(ValidationError) as excinfo:
        validate_profanity(username)

    assert "This name contains profane word:" in str(excinfo.value)


def test_valid_badge_file_type_valid_image(uploaded_svg):
    assert validate_badge_file_type(uploaded_svg) is None


def test_valid_badge_file_type_invalid_file_type(test_image):
    with pytest.raises(ValidationError) as exc_info:
        validate_badge_file_type(test_image)

    assert "File type not supported. Use: svg+xml" in exc_info.value.message


def test_valid_avatar_type_valid_image(test_image):
    assert validate_avatar_file_type_and_dimensions(test_image) is None


def test_valid_avatar_type_invalid_image_type(uploaded_svg):
    with pytest.raises(ValidationError) as exc_info:
        validate_avatar_file_type_and_dimensions(uploaded_svg)

    assert "File type not supported. Use one of: jpeg, png." in exc_info.value.message


@pytest.mark.parametrize("avatar_valid_type", [141, 150, 200], indirect=True)
def test_valid_avatar_invalid_image_dimensions(avatar_valid_type):
    with pytest.raises(ValidationError) as exc_info:
        validate_avatar_file_type_and_dimensions(avatar_valid_type)

    assert "Image exceeds maximum dimensions. Maximum width:" in str(
        exc_info.value.messages
    )
