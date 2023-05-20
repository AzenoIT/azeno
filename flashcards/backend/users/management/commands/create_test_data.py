from django.conf import settings
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from django.db import transaction

from decks.factories import CategoryFactory, DeckFactory, DifficultyLevelFactory, TagFactory, FlashcardFactory
from users.factories import UserFactory


class Command(BaseCommand):
    """Custom command for generating deck, user, tag, category and difficulty level objects.
    It takes five named (optional) arguments which are the counts of objects that need to be generated.

    Usage:

    ``python manage.py create_test_data --decks=5 --users=3 --tags=2 --categories=4 --difficulties=2``

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
        deck_objects_count = kwargs["decks"]
        user_objects_count = kwargs["users"]
        tag_objects_count = kwargs["tags"]
        category_objects_count = kwargs["categories"]
        difficulties_objects_count = kwargs["difficulties"]
        if not settings.DEBUG:
            self.stdout.write(
                self.style.WARNING(
                    "!!! Generating test data is not possible, "
                    "because DEBUG is set to False which may indicate production environment!!!"
                )
            )
        else:
            self.stdout.write(self.style.SUCCESS("Creating test data"))
            for item in range(deck_objects_count):
                DeckFactory()
            for item in range(user_objects_count):
                UserFactory()
            for item in range(tag_objects_count):
                TagFactory.create(decks=(DeckFactory(),), flashcards=(FlashcardFactory(),))
            for item in range(category_objects_count):
                CategoryFactory()
            for item in range(difficulties_objects_count):
                DifficultyLevelFactory()

    def add_arguments(self, parser: CommandParser) -> None:
        """Overrides base method for taking in arguments.
        This method is parsing the count of objects the user wants to generate. If the count for the particular object
        is not specified the default value 0 is taken and the object is not created.

        :param CommandParser parser: parser
        :return: None
        """
        parser.add_argument(
            "--decks",
            default=0,
            type=int,
            help="Indicates the number of deck objects to be created",
        )

        parser.add_argument(
            "--users",
            default=0,
            type=int,
            help="Indicates the number of user objects to be created",
        )

        parser.add_argument(
            "--tags",
            default=0,
            type=int,
            help="Indicates the number of tag objects to be created",
        )

        parser.add_argument(
            "--categories",
            default=0,
            type=int,
            help="Indicates the number of category objects to be created",
        )

        parser.add_argument(
            "--difficulties",
            default=0,
            type=int,
            help="Indicates the number of difficulty level objects to be created",
        )
