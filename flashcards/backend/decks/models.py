from django.db import models


class Tag(models.Model):
    """Model for representing tags for decks
    :param name: Tag name
    :type name: str
    :param description: Description for tag
    :type description: str
    """

    name = models.CharField(max_length=24)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "tag"
        verbose_name_plural = "tags"
