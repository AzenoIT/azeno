import uuid

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

class QuizCustomUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False, db_index=True)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=100, validators=[UnicodeUsernameValidator()])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email address']

    def __str__(self):
        return self.email
