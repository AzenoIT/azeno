from django.db import models


class Agreements(models.Model):
    """Model for representing user's agreements on newsletters

    :param email: user's email
    :type email: str
    :param checkbox_1: user's selection on agreement
    :type checkbox_1: bool, False by default
    :param checkbox_2: user's selection on agreement
    :type checkbox_2: bool, False by default
    :param checkbox_3: user's selection on agreement
    :type checkbox_3: bool, False by default

    """

    email = models.EmailField()
    checkbox_1 = models.BooleanField(default=False)
    checkbox_2 = models.BooleanField(default=False)
    checkbox_3 = models.BooleanField(default=False)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "agreement"
        verbose_name_plural = "agreements"
