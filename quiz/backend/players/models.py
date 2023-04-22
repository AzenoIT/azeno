import uuid
from django.db import models

from helpers.validators.validators import (
    validate_profanity,
    validate_avatar_file_type_and_dimensions,
)


class Player(models.Model):
    """Model for representing player data for logged and not logged users

    :param nick: player name
    :type nick: str
    :param rank: player ranking calculated with Elo system
    :type rank: int, optional
    :param is_bot: indicates if player is artificial
    :type is_bot: bool, optional
    :param is_active: indicates if player is able to play
    :type is_active: bool, optional

    """

    uuid = models.UUIDField(
        editable=False, db_index=True, default=uuid.uuid4, primary_key=True
    )
    nick = models.CharField(
        max_length=30,
        validators=[
            validate_profanity,
        ],
    )
    rank = models.PositiveIntegerField(
        default=0, help_text="Calculated with Elo system."
    )
    is_bot = models.BooleanField(
        default=False,
        help_text="True if player is not real.",
        verbose_name="Player type.",
    )
    is_active = models.BooleanField(
        default=True, help_text="Indicates if player is an active player."
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nick

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "players"

    def save(self, *args, **kwargs):
        self.clean_fields()
        super().save(*args, **kwargs)


def upload_avatar_to(instance, filename):
    """This function iis used for generating a dynamic path for players avatars, so they
    are stored in dedicated directories identified by uuid.

    :param instance: Object of given class.
    :type instance: Profile
    :param filename: File uploaded by player.
    :type: SimpleUploadedFile
    :return: String containing a path to dedicated directory.
    :rtype: str
    """
    return f"players/{instance.player.uuid}/avatars/{filename}"


class Profile(models.Model):
    """Model for representing player settings and basic information. Related to :class:`players.models.Player`

    :param player: Player related to profile.
    :type player: models.ForeignKey
    :param avatar: Image representing given player.
    :type avatar: Path
    :param score: How many points given player has. The maximum value of points
            a player should be able to earn is 2800.
    :type score: models.PositiveSmallIntegerField
    :param status: Flag indicating whether player is online
    :type status: bool
    :param is_push_notification: Flag indicating whether player wants to receive push notifications.
    :type is_push_notification: bool, optional
    :param is_findable: Flag indicating whether player wants to be found by other players.
    :type is_findable: bool, optional
    :param is_invitable: Flag indicating whether player wants to be invited by other players.
    :type is_findable: bool, optional

    """

    player = models.ForeignKey(
        "Player", on_delete=models.DO_NOTHING, related_name="profile"
    )
    avatar = models.FileField(
        upload_to=upload_avatar_to,
        validators=[validate_avatar_file_type_and_dimensions],
    )
    score = models.PositiveIntegerField(default=0, help_text="Points earned by player.")
    status = models.BooleanField(
        default=False, help_text="Information whether player is online or not."
    )
    is_push_notification = models.BooleanField(
        default=False,
        help_text="Information about whether player wants to receive push notifications.",
    )
    is_findable = models.BooleanField(
        default=False,
        help_text="Information about whether player wants to be visible in searches.",
    )
    is_invitable = models.BooleanField(
        default=False,
        help_text="Information whether player wants to be invited by other players.",
    )

    def __str__(self):
        return f"Profile of {self.player.nick}"
