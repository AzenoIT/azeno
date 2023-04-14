# Generated by Django 4.1.7 on 2023-04-16 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("players", "0002_profile"),
        ("stats", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PlayerBadge",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("obtained_on", models.DateTimeField(auto_now_add=True)),
                (
                    "badge",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="stats.badge"
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="players.player",
                    ),
                ),
            ],
            options={
                "verbose_name": "badge obtained by player",
                "verbose_name_plural": "badges obtained by players",
            },
        ),
        migrations.AddField(
            model_name="badge",
            name="players",
            field=models.ManyToManyField(
                related_name="badges", through="stats.PlayerBadge", to="players.player"
            ),
        ),
    ]