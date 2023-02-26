# Generated by Django 4.1.5 on 2023-02-26 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("categ", models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name="Restaurant",
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
                ("restaurant", models.CharField(max_length=40)),
                ("characteristic", models.TextField()),
                ("city", models.CharField(max_length=30)),
                ("street", models.CharField(max_length=50)),
                (
                    "image",
                    models.ImageField(max_length=255, null=True, upload_to="images/"),
                ),
                (
                    "approved",
                    models.DecimalField(
                        decimal_places=2, default=0, max_digits=10, null=True
                    ),
                ),
                ("date_added", models.DateTimeField(auto_now_add=True)),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
