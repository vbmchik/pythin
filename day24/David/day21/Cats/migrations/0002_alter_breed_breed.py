# Generated by Django 4.1.5 on 2023-02-08 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='breed',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
