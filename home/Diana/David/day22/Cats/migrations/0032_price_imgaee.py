# Generated by Django 4.1.5 on 2023-02-13 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0031_price_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="price",
            name="imgaee",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="Cats.image"
            ),
            preserve_default=False,
        ),
    ]