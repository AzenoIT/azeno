from django.contrib.auth.hashers import make_password
from django.utils import timezone
from factory import Faker, LazyAttribute
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDateTime

from .models import CustomUser


class UserFactory(DjangoModelFactory):
    class Meta:
        model = CustomUser

    last_login = FuzzyDateTime(timezone.now())
    date_joined = FuzzyDateTime(timezone.now())

    email = Faker("email")
    username = LazyAttribute(lambda a: a.email.split("@")[0])
    password = make_password("testPass123")
    is_active = True
