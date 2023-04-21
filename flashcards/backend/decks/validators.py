import os

import magic
from PIL import Image

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


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


def validate_image_file_type(upload):
    """The function of checking the correctness of the loaded file type which is saved in settings IMAGE_TYPES
    and the file resolution saved in settings MAX_IMAGE_WIDTH, MAX_IMAGE_HEIGHT

      :param upload: Uploaded file
      :type upload: file
      :raises ValidationError: if the file type is not supported
      :return: None
    """
    tmp_path = "tmp/%s" % upload.name[2:]
    default_storage.save(tmp_path, ContentFile(upload.file.read()))
    full_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)
    file_type = magic.from_file(full_tmp_path, mime=True)
    default_storage.delete(tmp_path)
    image_types = [f"image/{img}" for img in settings.IMAGES_TYPES]
    if file_type not in image_types:
        raise ValidationError(f'File type not supported. Use: {", ".join(settings.IMAGES_TYPES)}')

    with Image.open(upload) as img:
        width, height = img.size
        if width > settings.MAX_IMAGE_WIDTH or height > settings.MAX_IMAGE_HEIGHT:
            raise ValidationError(
                f"The uploaded image is too large. The maximum dimensions are {settings.MAX_IMAGE_WIDTH}"
                f"x{settings.MAX_IMAGE_HEIGHT} pixels."
            )


def validate_image_file_size(upload):
    """Function for validating uploaded file size, which is set in settings under MAX_UPLOAD_SIZE variable
    :param upload: uploaded file
    :type upload: file
    :raises ValidationError: if file size is bigger than allowed
    :return: None
    """
    if upload.size > settings.MAX_UPLOAD_SIZE:
        raise ValidationError(
            f"The uploaded file is too large. The maximum allowed size is {settings.MAX_UPLOAD_SIZE / (1024 * 1024)} MB."
        )
