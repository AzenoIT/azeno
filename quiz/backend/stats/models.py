from django.db import models
from django.urls import reverse

from helpers.validators.validators import validate_badge_file_type


class TimestampModel(models.Model):
    """Abstract class for saving timestamps.

    :param created_at: Date and time when given object was created.
    :type created_at: models.DateTimeField(auto_now_add=True)

    :param updated_at: Date and time of when given object was updated.
    :type updated_at: models.DateTimeField(auto_now_add=True)

    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PlayerBadge(models.Model):
    """Model for linking badges :class:`stats.models.Badge` with player :class:`players.models.Player`

    :param badge: ID of badge
    :type badge: models.ForeignKey

    :param player: ID of player
    :type player: models.ForeignKey

    :param obtained_on: Date when player obtained given badge.
    :type obtained_on: models.DateTimeField

    """

    badge = models.ForeignKey("Badge", on_delete=models.DO_NOTHING)
    player = models.ForeignKey("players.Player", on_delete=models.DO_NOTHING)
    obtained_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "badge obtained by player"
        verbose_name_plural = "badges obtained by players"

    def __str__(self):
        return f"{self.badge.name} obtained by {self.player.nick}"


class Badge(TimestampModel):
    """Represents badges that players/users can earn during games.
    Inherits from TimestampModel and :class:`stats.models.TimestampModel`

    Following fields are inherited:
        * created_at
        * updated_at

    :param name: Name of badge
    :type name: models.CharField(max_length=40, unique=True)

    :param description: Description of bade. For e.g. when user/player can obtain it.
    :type description: models.CharField(max_length=300)

    :param owned_by_user_percentage: How many users/players own given badge.
    :type owned_by_user_percentage: models.FloatField(default=0)

    :param points: How many points is given badge worth.
    :type points: models.PositiveSmallIntegerField(default=0)

    :param created_at: Date and
    time when badge was created.
    :type created_at: models.DateTimeField(auto_now_add=True)

    :param updated_at: Date and time when badge was updated, changes every time badge is edited.
    :type updated_at: models.DateTimeField(auto_now=True)

    """

    name = models.CharField(max_length=40, unique=True)
    description = models.CharField(max_length=300)
    owned_by_user_percentage = models.FloatField(
        default=0, help_text="Percentage of all users/players owning given badge."
    )
    points = models.PositiveSmallIntegerField(
        default=0, help_text="How many points is given badge worth."
    )
    image = models.FileField(
        upload_to="badges/",
        validators=[
            validate_badge_file_type,
        ],
    )
    players = models.ManyToManyField(
        "players.Player", related_name="badges", through="PlayerBadge"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Method for building absolute url for Badge object.

        :return: The absolute URL of the badge's detail view.
        :rtype: str
        """
        return reverse("stats:badge_detail", args=[str(self.pk)])
