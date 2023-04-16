# Generated by Django 4.1.7 on 2023-04-16 12:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("decks", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FlashcardStudy",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("study_date", models.DateTimeField(auto_now_add=True)),
                ("correct_answers", models.PositiveIntegerField(verbose_name="Correct answers count")),
                (
                    "flashcard",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="study_logs", to="decks.flashcard"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)ss",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DeckStudy",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("study_date", models.DateTimeField(auto_now_add=True)),
                ("correct_answers", models.PositiveIntegerField(verbose_name="Correct answers count")),
                ("study_duration", models.DurationField()),
                ("realization", models.DecimalField(decimal_places=1, max_digits=4)),
                (
                    "deck",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="study_logs", to="decks.deck"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="%(class)ss",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
