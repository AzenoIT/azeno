import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class QuizCustomUserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError(_('Email field is required'))

        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.is_active = False
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class QuizCustomUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True, editable=False, db_index=True)
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=100, validators=[UnicodeUsernameValidator()])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = QuizCustomUserManager()

    def __str__(self):
        return self.email
