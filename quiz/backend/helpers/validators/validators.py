import os
import re
from typing import List

import magic
from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import UploadedFile

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


def validate_badge_file_type(upload: UploadedFile) -> None:
    """Validate type of given file to uploaded by user.

    :param upload: UploadedFile instance containing the file uploaded by the user
    :type upload: UploadedFile
    :return: None
    :raise: ValidationError
    """
    if upload.name is None:
        raise ValidationError("No file name provided.")

    tmp_path = "tmp/%s" % upload.name[2:]

    if upload.file is None:
        raise ValidationError("No file content provided.")

    default_storage.save(tmp_path, ContentFile(upload.file.read()))
    full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)
    file_type = magic.from_file(full_tmp_path, mime=True)
    default_storage.delete(tmp_path)
    image_types = [f"image/{img}" for img in settings.BADGE_IMAGE_TYPES]

    if file_type not in image_types:
        raise ValidationError(
            f'File type not supported. Use: {", ".join(settings.BADGE_IMAGE_TYPES)}'
        )
