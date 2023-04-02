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
