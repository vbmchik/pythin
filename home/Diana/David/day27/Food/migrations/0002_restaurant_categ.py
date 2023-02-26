# Generated by Django 4.1.5 on 2023-02-26 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Food", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="categ",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="Food.category",
            ),
            preserve_default=False,
        ),
    ]
