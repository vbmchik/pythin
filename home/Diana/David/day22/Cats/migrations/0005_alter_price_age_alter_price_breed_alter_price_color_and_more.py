# Generated by Django 4.1.5 on 2023-02-10 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cats", "0004_alter_price_age_alter_price_breed_alter_price_color_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="price",
            name="age",
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name="price",
            name="breed",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="price",
            name="color",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="price",
            name="temperament",
            field=models.CharField(max_length=40),
        ),
    ]