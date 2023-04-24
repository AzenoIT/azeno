# Generated by Django 4.1.7 on 2023-04-24 16:39

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
        ("contenttypes", "0002_remove_content_type_name"),
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
            name="DifficultyLevel",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ],
        ),
        migrations.CreateModel(
            name="Flashcard",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("rating_flashcard", models.PositiveIntegerField(default=0)),
                ("is_active", models.BooleanField(default=True)),
                ("object_id_question", models.PositiveIntegerField()),
                ("object_id_answer", models.PositiveIntegerField()),
                ("date_added", models.DateField(auto_now_add=True)),
                ("date_modification", models.DateField(auto_now=True)),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ("category", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="decks.category")),
                (
                    "content_type_answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="flashcard_answer",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "content_type_question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="flashcard_question",
                        to="contenttypes.contenttype",
                    ),
                ),
                ("deck", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="decks.deck")),
                (
                    "difficulty",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="decks.difficultylevel"),
                ),
            ],
            options={
                "verbose_name": "flashcard",
                "verbose_name_plural": "flashcards",
            },
        ),
        migrations.CreateModel(
            name="ItemBase",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name="Code",
            fields=[
                (
                    "itembase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="decks.itembase",
                    ),
                ),
                ("content", models.TextField()),
            ],
            bases=("decks.itembase",),
        ),
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "itembase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="decks.itembase",
                    ),
                ),
                (
                    "content",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="decks/",
                        validators=[decks.validators.validate_file_type, decks.validators.validate_file_size],
                    ),
                ),
            ],
            bases=("decks.itembase",),
        ),
        migrations.CreateModel(
            name="Text",
            fields=[
                (
                    "itembase_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="decks.itembase",
                    ),
                ),
                ("content", models.CharField(max_length=255)),
            ],
            bases=("decks.itembase",),
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
    ]
