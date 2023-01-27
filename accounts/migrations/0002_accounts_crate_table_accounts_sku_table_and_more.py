# Generated by Django 4.1.5 on 2023-01-26 06:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_cratetable_creation_alter_skutable_creation'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='crate_table',
            field=models.ManyToManyField(blank=True, to='userapp.cratetable'),
        ),
        migrations.AddField(
            model_name='accounts',
            name='sku_table',
            field=models.ManyToManyField(blank=True, to='userapp.skutable'),
        ),
        migrations.AlterField(
            model_name='accounts',
            name='creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 26, 12, 17, 15, 829990)),
        ),
    ]