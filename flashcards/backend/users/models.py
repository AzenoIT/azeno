import uuid

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator

from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager["CustomUser"]):

    """Custom manager for CustomUser"""

    use_in_migrations = True

    def create_user(self, email, password, username="", **kwargs):
        """
        Create and save a CustomUser with given email and password.

        :param str email: user email
        :param str username: user username
        :param str password: user password
        :return users.models.CustomUser user: user
        :raise ValueError: if email is not set
        """
        if not email:
            raise ValueError(_("Email field is required"))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.is_active = False
        user.password = make_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password=None):
        """Create and save CustomUser with staff, admin and superuser permissions.

        :param str email: user email
        :param str username: user email
        :param str password: user password
        :return users.models.CustomUser user: user
        """
        user = self.create_user(email=email, username=username, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser):
    """Overrides default User model in Django

    CustomUser uses email field as the USERNAME_FIELD for authentication. It is still possible to set username,
    but it is not required field.

    Inherits only from AbstractUser.

    Following attributes are inherited from baseclasses:
        * username
        * first_name
        * last_name
        * email
        * is_staff
        * is_superuser
        * is_active
        * date_joined
        * last_login
        * password
        * groups

    :param str email: user email
    :param str, optional username: username
    :param str password: user password
    """

    id: models.UUIDField = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, db_index=True)
    email = models.EmailField(_("email address"), unique=True)
    username = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        unique=False,
        validators=[UnicodeUsernameValidator()],
        help_text="Optional",
    )

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: list[str] = [
        "email address",
    ]

    # TODO: Due to unresolved issues in django-stubs project, type checking for CustomUserManager had to be silenced
    # Link to the issue with this solution recommended as fix https://github.com/typeddjango/django-stubs/issues/174

    objects = CustomUserManager()  # type: ignore[assignment]

    def __str__(self) -> str:
        return self.email
