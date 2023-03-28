from django.core.management import BaseCommand
from django.db import transaction

from django.conf import settings
from users.models import CustomUser


class Command(BaseCommand):
    """Custom command for deleting generated user objects.

    Usage:

    ``python manage.py delete_test_data``

    """

    help = "Deletes test data for app"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        """Command handler.
        Deletes all objects except users with superuser flag set to True. If DEBUG is set to false
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
            models = [CustomUser]
            for item in models:
                item.objects.filter(is_superuser=False).delete()
