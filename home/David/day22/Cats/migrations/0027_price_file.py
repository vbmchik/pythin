# Generated by Django 4.1.5 on 2023-02-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0026_remove_price_image_remove_price_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="price",
            name="file",
            field=models.FileField(null=True, upload_to="Cats"),
        ),
    ]
