# Generated by Django 4.1.5 on 2023-01-25 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapps', '0002_entry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
    ]