from io import BytesIO

import pytest
from django.core.exceptions import ValidationError

from helpers.validators.validators import validate_profanity, validate_badge_file_type


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
