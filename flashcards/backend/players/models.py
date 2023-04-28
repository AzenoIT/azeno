from datetime import datetime

import pytz
import uuid
from django.contrib.auth import get_user_model
from django.db import models

from config import settings


class AccountType(models.Model):
    """Model for representing account types (tiers).

    :param name: account type name
    :type name: str
    :param duration: duration of a particular account type
    :type duration: timedelta
    :param cost: monthly cost of a particular account type
    :type cost: Decimal
    """

    name = models.CharField(max_length=150)
    duration = models.DurationField()
    cost = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Player(models.Model):
    """Model for representing player data for logged and not logged users

    :param nick: player name
    :type nick: str
    :param user: related user object
    :type user: CustomUser
    :param account_type: player's account type
    :type account_type: AccountType
    :param start_time: player's account start time
    :type start_time: datetime
    :param expiration_time: player's account expiration time, depends on account type
    :type expiration_time: datetime
    :param is_active: indicates if player is able to play
    :type is_active: bool, optional
    """

    uuid = models.UUIDField(editable=False, db_index=True, default=uuid.uuid4, primary_key=True)
    nick = models.CharField(max_length=30)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, blank=True, null=True)
    account_type = models.ForeignKey("AccountType", on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    expiration_time = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True, help_text="Indicates if player is active.")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nick

    class Meta:
        verbose_name = "player"
        verbose_name_plural = "players"

    def save(self, *args, **kwargs):
        if self.is_active:
            self.start_time = datetime.now(pytz.timezone(settings.TIME_ZONE))
            self.expiration_time = self.start_time + self.account_type.duration

        super().save(*args, **kwargs)
