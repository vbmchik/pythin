# Generated by Django 4.1.5 on 2023-04-17 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Shope", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="product",
            options={
                "ordering": ("name",),
                "verbose_name": "Продукты",
                "verbose_name_plural": "Продукты",
            },
        ),
    ]