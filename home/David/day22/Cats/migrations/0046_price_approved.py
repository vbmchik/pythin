# Generated by Django 4.1.5 on 2023-02-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0045_remove_image_owner_price_image_price_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="price",
            name="approved",
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
    ]
