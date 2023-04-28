from django.conf import settings
from django.core.management import BaseCommand
from django.db import transaction

from decks.models import Category, Deck, DifficultyLevel, Tag
from users.models import CustomUser


class Command(BaseCommand):
    """Custom command for deleting generated test data objects.

    Usage:

    ``python manage.py delete_test_data``

    """

    help = "Deletes test data for app"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        """Command handler.
        Deletes all test data objects except users with superuser flag set to True. If DEBUG is set to false
        method will not delete any objects, and display a warning that the project is probably
        in production environment.

        :param tuple args: args
        :param dict kwargs: kwargs
        :return: None
        """
        if not settings.DEBUG:
            self.stdout.write(
                self.style.WARNING(
                    "!!!Deleting data is not possible, because DEBUG is set to False,"
                    " which may indicate production environment!!!"
                )
            )
        else:
            self.stdout.write(self.style.SUCCESS("Deleting test data"))
            tag_models = [Tag]
            for item in tag_models:
                item.objects.all().delete()
            deck_models = [Deck]
            for item in deck_models:
                item.objects.all().delete()
            category_models = [Category]
            for item in category_models:
                item.objects.all().delete()
            difficulty_models = [DifficultyLevel]
            for item in difficulty_models:
                item.objects.all().delete()
            user_models = [CustomUser]
            for item in user_models:
                item.objects.filter(is_superuser=False).delete()
