from django.contrib.auth import get_user_model
from django.utils import timezone
from factory import Faker, LazyAttribute
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDateTime


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    last_login = FuzzyDateTime(timezone.now())
    date_joined = FuzzyDateTime(timezone.now())

    email = Faker("email")
    username = LazyAttribute(lambda a: a.email.split("@")[0])
    password = "testPass123"
    is_active = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        return manager.create_user(*args, **kwargs)
