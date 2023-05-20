from django.contrib.auth import get_user_model
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

    :param image: Category image
    :type image: file
    :param name: Category name
    :type name: str
    :param description: Description for category
    :type description: str

    """

    image = models.FileField(
        upload_to="decks/", validators=[validators.validate_file_type, validators.validate_file_size]
    )
    name = models.CharField(max_length=24, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"


class DifficultyLevel(models.Model):
    """Model for representing how hard flashcard/deck is to learn.

    :param name: level name
    :type name: str
    :param value: value
    :type value: int

    """

    name = models.CharField(max_length=20, unique=True)
    value = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "difficulty level"
        verbose_name_plural = "difficulty level`s"

    def save(self, *args, **kwargs):
        name = DifficultyLevel.objects.filter(name__iexact=self.name).first()
        if not name:
            super().save(*args, **kwargs)
            return self
        if name and self.id:
            super().save(*args, **kwargs)
            return self
        return name


class Deck(TimeStampModel):
    """Model for representing deck data

    :param image: deck image
    :type image: file, None
    :param name: deck name
    :type name: str
    :param category: foreign key for Category model
    :type category: int
    :param difficulty_level: foreign key for DifficultyLevel model
    :type difficulty_level: int
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
        default=None,
        validators=[validators.validate_file_type, validators.validate_file_size],
    )
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.DO_NOTHING)
    difficulty_level = models.ForeignKey("DifficultyLevel", on_delete=models.DO_NOTHING)
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
    :param decks:
    :param decks: Foreign Key for Deck model
    :type decks: int
    :param flashcards: Foreign Key for Flashcard model
    :type flashcards: int
    """

    name = models.CharField(max_length=24)
    decks = models.ManyToManyField("Deck", related_name="tags", blank=True)
    flashcards = models.ManyToManyField("Flashcard", related_name="tags", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [models.UniqueConstraint(Lower("name"), name="unique_lower_name_tag")]
        verbose_name = "tag"
        verbose_name_plural = "tags"


class Flashcard(models.Model):
    pass
