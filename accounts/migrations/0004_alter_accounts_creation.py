# Generated by Django 4.1.5 on 2023-01-26 06:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_accounts_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 12, 24, 41, 763667)),
        ),
    ]
