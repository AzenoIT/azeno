from django.core.management import BaseCommand
from django.db import transaction

from config.settings import DEBUG
from users.models import CustomUser


class Command(BaseCommand):
    help = "Deletes test data for app"
    @transaction.atomic
    def handle(self, *args, **kwargs):
        if DEBUG:
            self.stdout.write("Deleting test data")
            models = [CustomUser]
            for item in models:
                item.objects.filter(is_superuser=False).delete()
        else:
            self.stdout.write("""
            !!!Deleting data is not possible, because DEBUG is set to False,
            which may indicate production environment!!!
            """)
