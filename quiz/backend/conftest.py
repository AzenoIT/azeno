import io
import json
from pathlib import Path

import pytest
from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile

from players.models import Player
from django.core.management import call_command

from players.views import PlayerCreateAPIView
from stats.models import Badge


@pytest.fixture
def player(db):
    return Player.objects.create(nick="John Doe")


@pytest.fixture
def player_bot(db):
    return Player.objects.create(nick="Sophia", is_bot=True)


@pytest.fixture
def generated_data_with_custom_command():
    """Fixture for calling create_test_data command

    :return func call_command: call_command
    """
    return call_command(
        "create_test_data",
        "5",
    )


@pytest.fixture
def api_rf():
    from rest_framework.test import APIRequestFactory

    return APIRequestFactory()


@pytest.fixture
def player_api(api_rf, db):
    def create_player():
        request = api_rf.post(
            "api/v1/players/",
            json.dumps({"username": "test_nick"}),
            content_type="application/json",
        )
        view = PlayerCreateAPIView.as_view()
        return view(request)

    return create_player


@pytest.fixture
def adjectives_temp_file(tmp_path: Path) -> Path:
    """Fixture for substituting text file with adjectives for username generator.

    :return monkeypatch file: adj_temp_file
    """
    test_adj = [
        "silly",
        "outstanding",
        "talented",
    ]

    adj_temp_file = tmp_path / "temp_adjectives.txt"
    adj_temp_file.write_text("\n".join(test_adj))

    return adj_temp_file


@pytest.fixture
def nouns_temp_file(tmp_path: Path) -> Path:
    """Fixture for substituting text file with nouns for username generator.

    :return monkeypatch file: noun_temp_file
    """
    test_noun = [
        "Sod",
        "Archer",
        "Craftsman",
    ]

    noun_temp_file = tmp_path / "temp_nouns.txt"
    noun_temp_file.write_text("\n".join(test_noun))

    return noun_temp_file


@pytest.fixture
def profane_words_temp_file(tmp_path: Path) -> Path:
    """Creates a temporary path for profane words to test
    the validator function :function:`helpers.validators.validate_profanity`

    :param Path tmp_path: tmp_path fixture provided by pytest
    :return: Path file for test to use as base.
    """
    test_profane_words = ["fuckin", "boobs", "cunt", "kocha dzieci"]

    temp_file = tmp_path / "temp_profane_words.txt"
    temp_file.write_text("\n".join(test_profane_words))

    return temp_file


@pytest.fixture
def svg_content():
    """Content for uploaded_svg file.

    :return: Multiline string containing svg content
    """
    return """
        <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50">
          <rect width="50" height="50" style="fill:rgb(255,0,0);" />
        </svg>
        """


@pytest.fixture
def uploaded_svg(svg_content):
    """Instance of uploaded svg file

    :param svg_content: Content for svg file.
    :type svg_content: str
    :return: SimpleUploadedFile instance
    """
    return SimpleUploadedFile(
        "test_image.svg",
        svg_content.strip().encode("utf-8"),
        content_type="image/svg+xml",
    )


@pytest.fixture(params=["jpeg", "png"])
def test_image(request):
    """Fixture for wrong types of files to validate by :class:`stats.models.Badge`

    :param request: fixture for providing information about executing test function.
    :type request: FixtureRequest
    :returns uploaded_image: Object of class SimpleUploadedFile
    """
    img = Image.new("RGB", (50, 50), color=(255, 0, 0))
    image_data = io.BytesIO()
    img.save(image_data, format=request.param)

    uploaded_image = SimpleUploadedFile(
        f"test_image.{request.param}",
        image_data.getvalue(),
        content_type=f"image/{request.param}",
    )
    yield uploaded_image


@pytest.fixture
def temp_media_root(settings, tmpdir):
    """Temporary django media directory.

    :param settings: Django setting fixture
    :param tmpdir: Temporary directory fixture
    :return: Setting media root variable
    """
    settings.MEDIA_ROOT = tmpdir.strpath
    return settings.MEDIA_ROOT


@pytest.fixture
def avatar_valid_type(request):
    """Fixture that returns avatar with dimensions given in parameter.

    :param request: fixture for providing information about executing test function.
    :type request: FixtureRequest
    :return: uploaded image with parametrized dimensions
    """
    size = request.param
    img = Image.new("RGB", (size, size), color=(255, 0, 0))
    image_data = io.BytesIO()
    img.save(image_data, format="JPEG")

    uploaded_image = SimpleUploadedFile(
        "test_image.jpeg",
        image_data.getvalue(),
        content_type="image/jpeg",
    )
    yield uploaded_image


@pytest.fixture
def badge(db, uploaded_svg, temp_media_root):
    """Badge instance fixture.

    :param db: Database fixtue
    :param uploaded_svg: Uploaded. svg file.
    :return: Badge instance
    """
    yield Badge.objects.create(
        name="Test badge",
        description="Description with maximum length of 300 characters.",
        image=uploaded_svg,
    )
