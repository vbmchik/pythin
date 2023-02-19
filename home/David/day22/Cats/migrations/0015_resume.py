# Generated by Django 4.1.5 on 2023-02-11 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0014_delete_book_delete_foo"),
    ]

    operations = [
        migrations.CreateModel(
            name="Resume",
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
                ("email", models.EmailField(max_length=254)),
                ("name", models.CharField(max_length=255)),
                ("file", models.FileField(null=True, upload_to="Cats")),
            ],
        ),
    ]