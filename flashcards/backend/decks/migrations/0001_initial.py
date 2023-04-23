from decimal import Decimal
import decks.validators
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.text


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=24, unique=True)),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name": "category",
                "verbose_name_plural": "categories",
            },
        ),
        migrations.CreateModel(
            name="Deck",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "image",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="decks/",
                        validators=[decks.validators.validate_file_type, decks.validators.validate_file_size],
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("is_public", models.BooleanField(default=True)),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=4,
                        validators=[django.core.validators.MinValueValidator(Decimal("0.00"))],
                    ),
                ),
                ("popularity", models.PositiveIntegerField(default=0)),
                ("rating", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                ("description", models.TextField()),
                (
                    "author",
                    models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
                ),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="decks.category")),
            ],
            options={
                "verbose_name": "deck",
                "verbose_name_plural": "decks",
            },
        ),
        migrations.CreateModel(
            name="Flashcard",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=24)),
                ("deck", models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="decks.deck")),
                ("flashcard", models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="decks.flashcard")),
            ],
            options={
                "verbose_name": "tag",
                "verbose_name_plural": "tags",
            },
        ),
        migrations.AddConstraint(
            model_name="tag",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("name"), name="unique_lower_name_tag"
            ),
        ),
        migrations.CreateModel(
            name="DifficultyLevel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=20, unique=True)),
                ("value", models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                "verbose_name": "difficulty level",
                "verbose_name_plural": "difficulty level`s",
            },
        ),
        migrations.AddConstraint(
            model_name="difficultylevel",
            constraint=models.UniqueConstraint(
                django.db.models.functions.text.Lower("name"), name="unique difficulty level"
            ),
        ),
        migrations.RemoveConstraint(
            model_name="difficultylevel",
            name="unique difficulty level",
        ),
    ]
