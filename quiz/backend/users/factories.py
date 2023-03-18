from datetime import datetime

import factory

from .models import CustomUser


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser

    last_login = factory.fuzzy.FuzzyDateTime(datetime.now())
    date_joined = factory.fuzzy.FuzzyDateTime(datetime.now())

    username = factory.Faker('username')
    email = factory.LazyAttribute(
        lambda a: f"{a.username}@test.com"
    )
    is_active = True
