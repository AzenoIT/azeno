from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from django.db import transaction

from config.settings import DEBUG
from users.factories import UserFactory


class Command(BaseCommand):
    help = "Creates test data for app"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        objects_count = kwargs['objects_count']
        if DEBUG:
            self.stdout.write(self.style.SUCCESS("Creating test data"))
            for item in range(objects_count):
                UserFactory()
        else:
            self.stdout.write(
                self.style.WARNING("""
                !!! Generating test data is not possible, 
                because DEBUG is set to False which may indicate production environment!!!
                """)
            )

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('objects_count', type=int, help='Indicates the number of objects to be created')
