import pytest
from django.core.exceptions import ValidationError

from helpers.validators.validators import validate_profanity


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
