# Generated by Django 4.1.5 on 2023-02-11 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0012_remove_book_book"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="book",
            field=models.FileField(default="1", upload_to="books/"),
            preserve_default=False,
        ),
    ]