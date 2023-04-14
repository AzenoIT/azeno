from django.db import models


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
        return name
