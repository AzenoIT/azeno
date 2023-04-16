import os

import magic
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from config import settings


def validate_file_type(upload):
    """function for validating uploaded file type
    :param upload: uploaded file
    :type upload: file
    :raises ValidationError: if file type is not supported
    :return: None
    """
    temp_path = f"tmp/{upload.name}"
    default_storage.save(temp_path, ContentFile(upload.file.read()))
    full_temp_path = os.path.join(settings.MEDIA_ROOT, temp_path)

    file_type = magic.from_file(full_temp_path, mime=True)

    default_storage.delete(temp_path)
    images_types = [f"image/{image_type}" for image_type in settings.IMAGES_TYPES]

    if file_type not in images_types:
        raise ValidationError(f'Unsupported file type. Use: {", *.".join(settings.IMAGES_TYPES)}.')


def validate_file_size(upload):
    """function for validating uploaded file size, which is set in settings under MAX_UPLOAD_SIZE variable
    :param upload: uploaded file
    :type upload: file
    :raises ValidationError: if file size is bigger than allowed
    :return: None
    """
    if upload.size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError(f"File size is too big. Max size is {settings.MAX_UPLOAD_SIZE} bytes.")
