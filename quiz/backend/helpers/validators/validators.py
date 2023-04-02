import os
import re
from typing import List

from django.core.exceptions import ValidationError

from config.settings import BASE_DIR

PROFANE_WORDS_FILE = os.path.join(
    BASE_DIR, "helpers", "validators/data", "profane_words.txt"
)


def load_profane_words(file_path: str) -> List[str]:
    """Load profane words from given file and remove all non-alphanumerical characters and spaces.

    :param str file_path: Path to file containing profane words.
    :return: Processed profane word, cleaned from all non-alphanumerical characters and spaces.
    :rtype: List[str]
    """
    with open(file_path, "r") as file:
        profane_words = [line.strip() for line in file.readlines() if line.strip()]

    processed_profane_words = [
        re.sub(r"\W", "", word.replace(" ", "")) for word in profane_words
    ]
    return processed_profane_words


def validate_profanity(value: str) -> None:
    """Validate given string to ensure it does not contain profane words listed in PROFANE_WORDS_FILE.

    If input contains profane words it raises :class:`django.core.exceptions.ValidationError`

    :param str value: The input string to validate
    :return: None
    :raises ValidationError: If value contains profane words.
    """
    text = re.sub(r"[^a-zA-Z]", "", value.lower())
    profane_words = load_profane_words(PROFANE_WORDS_FILE)

    for word in profane_words:
        if word in text:
            raise ValidationError(
                f"This name contains profane word: {word}. Please choose another one."
            )
