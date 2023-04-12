import pytest
from PIL import Image
from django.core.exceptions import ValidationError

from players.models import Player, Profile


def test_player_object_representation_in_gui():
    player = Player(nick="testPlayer")

    assert str(player) == "testPlayer"


def test_bot_creation(player_bot):
    players = Player.objects.all()
    assert player_bot in players


@pytest.mark.parametrize(
    "nick",
    [
        "prettyNick",
        "nicePerson",
        "testNick",
    ],
)
def test_player_nick_validates_non_profane_nick(nick, db):
    Player.objects.create(
        nick=nick,
    )
    saved_player = Player.objects.get(nick=nick)
    assert saved_player.nick == nick


@pytest.mark.parametrize(
    "nick",
    [
        "fuckinMonkey",
        "cuntFace",
        "boobs_rock",
        "JP2-kocha-dzieci",
    ],
)
def test_player_nick_raises_validation_error_for_profane_nick(nick, db):
    with pytest.raises(ValidationError) as excinfo:
        Player.objects.create(
            nick=nick,
        )
    assert "This name contains profane word:" in str(excinfo.value)


@pytest.mark.parametrize("avatar_valid_type", [110, 120])
def test_profile_object_representation_in_gui(player, avatar_valid_type):
    profile = Profile(player=player, avatar=avatar_valid_type)

    assert str(profile) == f"Profile of {player.nick}"


@pytest.mark.parametrize("avatar_valid_type", [110, 120, 140], indirect=True)
def test_profile_creation_validates_right_file_size(
    temp_media_root, player, avatar_valid_type, db
):
    Profile.objects.create(player=player, avatar=avatar_valid_type)

    with Image.open(avatar_valid_type) as img_upload:
        img_upload_width, img_upload_height = img_upload.size

    profile = Profile.objects.get(player__nick=player.nick)
    profile.full_clean()

    with Image.open(profile.avatar.path) as img_profile:
        img_profile_width, img_profile_height = img_profile.size

    assert img_profile_width == img_upload_width
    assert img_profile_height == img_upload_height


@pytest.mark.parametrize("avatar_valid_type", [141, 150, 200], indirect=True)
def test_profile_creation_raises_validation_error_with_invalid_file_size(
    temp_media_root, player, avatar_valid_type, db
):
    with pytest.raises(ValidationError) as exc_info:
        profile = Profile.objects.create(player=player, avatar=avatar_valid_type)
        profile.full_clean()

    assert (
        "Image exceeds maximum dimensions. Maximum width: 140px, "
        in exc_info.value.messages[0]
    )


def test_profile_creation_validates_valid_image_type(
    temp_media_root, player, test_image, db
):
    profile = Profile.objects.create(player=player, avatar=test_image)
    profile.full_clean()

    saved_profile = Profile.objects.get(player__nick=player.nick)

    assert test_image.name in saved_profile.avatar.name


def test_profile_creation_raises_validation_error_with_invalid_image_type(
    temp_media_root, player, uploaded_svg, db
):
    with pytest.raises(ValidationError) as exc_info:
        profile = Profile.objects.create(player=player, avatar=uploaded_svg)
        profile.full_clean()

    assert "File type not supported. Use one of:" in str(exc_info.value.message_dict)
