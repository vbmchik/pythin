# Generated by Django 4.1.5 on 2023-02-15 21:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Cats", "0042_rename_price_pric"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Pric",
            new_name="Price",
        ),
    ]
