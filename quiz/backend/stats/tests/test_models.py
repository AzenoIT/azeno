import pytest
from django.core.exceptions import ValidationError

from stats.models import Badge


def test_badge_gui_representation():
    badge = Badge(name="Good Badge Name", points=10)

    assert str(badge) == "Good Badge Name"


def test_badge_model_validates_right_type_of_image(temp_media_root, uploaded_svg, db):
    badge = Badge.objects.create(
        name="Funny Badge",
        description="A maximal length description of 300 characters",
        image=uploaded_svg,
    )
    badge.full_clean()

    image_name = Badge.objects.first().image.name

    assert Badge.objects.first().name == "Funny Badge"
    assert image_name.split("/")[-1] == uploaded_svg.name


def test_badge_model_raises_validation_error_with_wrong_file_types(
    temp_media_root, test_image, db
):
    with pytest.raises(ValidationError) as exc_info:
        badge = Badge.objects.create(
            name="Funny Badge",
            description="A maximal length description of 300 characters",
            image=test_image,
        )
        badge.full_clean()

    assert "File type not supported. Use: svg+xml" in exc_info.value.messages[0]
