import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, username, password, **kwargs):
        if not email:
            raise ValueError(_("Email field is required"))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.is_active = False
        user.password = make_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email=email, username=username, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    id = models.UUIDField(
        default=uuid.uuid4, primary_key=True, editable=False, db_index=True
    )
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(max_length=100, validators=[UnicodeUsernameValidator()])

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "email address",
    ]

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
