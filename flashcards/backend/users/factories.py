from django.contrib.auth import get_user_model
from django.utils import timezone
from factory import Faker, LazyAttribute
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    """Factory for generating user objects.

    It uses AUTH_USER_MODEL for building objects. Usage is automated with custom command,
    described in :doc:`users.management.commands`.
    """

    class Meta:
        model = get_user_model()

    last_login: Faker = Faker("date_time", tzinfo=timezone.get_current_timezone())
    date_joined: Faker = Faker("date_time", tzinfo=timezone.get_current_timezone())

    email: Faker = Faker("email")
    username: LazyAttribute = LazyAttribute(lambda a: a.email.split("@")[0])
    password: str = "testPass123"
    is_active: bool = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """

        :param .models.CustomUSer model_class: CustomUser
        :return .models.CustomUser user: user
        """
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)
