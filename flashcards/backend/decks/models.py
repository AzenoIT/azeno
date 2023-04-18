from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from django.db import models
from decimal import Decimal

from django.db.models.functions import Lower

from . import validators

User = get_user_model()


class TimeStampModel(models.Model):
    """Abstract model for tracking creation and modification dates of inheritance models.

    Inherits only from Model class.

    :param created_at: date and time of model
    :type created_at: DataTime
    :param updated_at: date and time of model modification
    :type updated_at: DataTime
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(models.Model):
    """Model for representing Category for deck

    :param name: Category name
    :type name: str
    :param description: Description for category
    :type description: str

    """

    name: models.CharField = models.CharField(max_length=24, unique=True)
    description: models.TextField = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class Deck(TimeStampModel):
    """Model for representing deck data

    :param image: deck image
    :type image: file, optional
    :param name: deck name
    :type name: str
    :param is_public: indicates if deck is public
    :type is_public: bool, optional
    :param price: deck price
    :type price: Decimal, min_value=0.00
    :param author: deck author
    :type author: User
    :param popularity: deck popularity
    :type popularity: int, optional
    :param rating: deck rating
    :type rating: int, optional
    :param is_active: indicates if deck is active
    :type is_active: bool, optional
    :param description: deck description
    :type description: str
    """

    image = models.FileField(
        upload_to="decks/",
        blank=True,
        null=True,
        validators=[validators.validate_file_type, validators.validate_file_size],
    )
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING)
    is_public = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))])
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    popularity = models.PositiveIntegerField(default=0)
    rating = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "deck"
        verbose_name_plural = "decks"


class Tag(models.Model):
    """Model for representing tags for decks
    :param name: Tag name
    :type name: str
    :param deck: Foreign Key for Deck model
    :type deck: int
    :param flashcard: Foreign Key for Flashcard model
    :type flashcard: int
    """

    name = models.CharField(max_length=24)
    deck = models.ForeignKey("Deck", on_delete=models.DO_NOTHING)
    flashcard = models.ForeignKey("Flashcard", on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [models.UniqueConstraint(Lower("name"), name="unique_lower_name_tag")]
        verbose_name = "tag"
        verbose_name_plural = "tags"


class Flashcard(models.Model):
    """Model for representing flashcards in decks
    :param deck: Foreign Key for Deck model
    :type deck: int
    :param category: Foreign Key for Category model
    :type category: int
    :param rating_flashcard: Flashcard rating
    :type rating_flashcard: int
    :param is_active: indicates if flashcard is active
    :type is_active: bool, optional
    :param question: Flashcard question text
    :type question: str
    :param answer: Flashcard answer text
    :type answer: str
    :param date_added: Flashcard added date
    :type date_added: date
    :param date_modification: Flashcard modification date
    :type date_modification: date
    :param author: Foreign Key for User model
    :type author: int
    :param difficulty: Foreign Key for DifficultyLevel model
    :type difficulty: int
    """

    deck = models.ForeignKey("Deck", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    rating_flashcard = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': (
        'text', 'image', 'code'
    )})
    object_id = models.PositiveIntegerField()
    question = GenericForeignKey('content_type', 'object_id')
    answer = GenericForeignKey('content_type', 'object_id')
    date_added = models.DateField(auto_now_add=True)
    date_modification = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty = models.ForeignKey("DifficultyLevel", on_delete=models.CASCADE)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = "flashcard"
        verbose_name_plural = "flashcards"


class Text(models.Model):
    content = models.TextField()


class Image(models.Model):
    content = models.FileField(
        upload_to="decks/",
        blank=True,
        null=True,
        validators=[validators.validate_file_type, validators.validate_file_size],
    )


class Code(models.Model):
    pass

class DifficultyLevel(models.Model):
    pass
