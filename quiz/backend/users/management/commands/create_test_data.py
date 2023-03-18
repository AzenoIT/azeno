from django.core.management import BaseCommand
from django.db import transaction

from config.settings import DEBUG
from users.factories import UserFactory


class Command(BaseCommand):
    help = "Creates test data for app"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        if DEBUG:
            self.stdout.write("Creating test data")
            for item in range(20):
                UserFactory()
        else:
            self.stdout.write(
                """
                !!! Generating test data is not possible, 
                because DEBUG is set to False which may indicate production environment!!!
                """
            )
