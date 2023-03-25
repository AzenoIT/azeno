from django.core.management import BaseCommand
from django.core.management.base import CommandParser

from django.db import transaction

from django.conf import settings
from users.factories import UserFactory


class Command(BaseCommand):
    """Custom command for generating user objects.
    It takes one positional argument, and it is the count of objects wanted to be generated.

    Usage:

    ``python manage.py create_test_data 5``

    """

    help = "Creates test data for app"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        """Command handler.
        Generates indicated number of objects. If DEBUG is set to false method will not generate any objects,
        and display a warning that the project is probably in production environment.

        :param tuple args: args
        :param dict kwargs: kwargs
        :return: None
        """
        objects_count = kwargs["objects_count"]
        if not settings.DEBUG:
            self.stdout.write(
                self.style.WARNING(
                    "!!! Generating test data is not possible, "
                    "because DEBUG is set to False which may indicate production environment!!!"
                )
            )
        else:
            self.stdout.write(self.style.SUCCESS("Creating test data"))
            for item in range(objects_count):
                UserFactory()

    def add_arguments(self, parser: CommandParser) -> None:
        """Overrides base method for taking in arguments.
        This method is parsing the count of objects the user want to generate.

        :param CommandParser parser: parser
        :return: None
        """
        parser.add_argument(
            "objects_count",
            type=int,
            help="Indicates the number of objects to be created",
        )
