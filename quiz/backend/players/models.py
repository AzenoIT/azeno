import uuid
from django.db import models

from helpers.validators.validators import validate_profanity


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
