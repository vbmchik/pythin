# Generated by Django 4.1.5 on 2023-02-12 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0025_remove_price_resume_price_image_price_title"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="price",
            name="image",
        ),
        migrations.RemoveField(
            model_name="price",
            name="title",
        ),
    ]