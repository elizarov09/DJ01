# Generated by Django 5.0.6 on 2024-06-21 13:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=255, verbose_name="Заголовок")),
                (
                    "short_description",
                    models.CharField(max_length=255, verbose_name="Краткое описание"),
                ),
                ("text", models.TextField(verbose_name="Новость")),
                ("pub_date", models.DateTimeField(verbose_name="Дата публикации")),
            ],
        ),
    ]
