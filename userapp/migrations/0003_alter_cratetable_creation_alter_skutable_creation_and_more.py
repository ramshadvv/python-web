# Generated by Django 4.1.5 on 2023-01-26 06:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_cratetable_creation_alter_skutable_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cratetable',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 12, 22, 5, 239472)),
        ),
        migrations.AlterField(
            model_name='skutable',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 12, 22, 5, 239472)),
        ),
        migrations.AlterField(
            model_name='skutable',
            name='owner',
            field=models.EmailField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]