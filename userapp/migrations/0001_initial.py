# Generated by Django 4.1.5 on 2023-01-26 06:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrateTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crate', models.CharField(blank=True, max_length=255, null=True)),
                ('crate_weight', models.BigIntegerField(blank=True, null=True)),
                ('docstatus', models.BooleanField(blank=True, default=True, null=True)),
                ('doctype', models.CharField(blank=True, max_length=255, null=True)),
                ('idx', models.IntegerField(blank=True, null=True)),
                ('is_final_crate', models.BooleanField(blank=True, default=False, null=True)),
                ('modified_by', models.EmailField(blank=True, max_length=254, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('owner', models.EmailField(blank=True, max_length=254, null=True)),
                ('packed_quantity', models.IntegerField(blank=True, null=True)),
                ('parent', models.CharField(blank=True, max_length=100, null=True)),
                ('parentfield', models.CharField(blank=True, max_length=100, null=True)),
                ('parenttype', models.CharField(blank=True, max_length=100, null=True)),
                ('creation', models.DateTimeField(default=datetime.datetime(2023, 1, 26, 12, 12, 6, 825102))),
                ('modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkuTable',
            fields=[
                ('docstatus', models.BooleanField(blank=True, default=False, null=True)),
                ('doctype', models.CharField(blank=True, max_length=255, null=True)),
                ('idx', models.IntegerField(blank=True, null=True)),
                ('modified_by', models.EmailField(blank=True, max_length=254, null=True)),
                ('owner', models.EmailField(max_length=255, unique=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('parent', models.CharField(blank=True, max_length=100, null=True)),
                ('parentfield', models.CharField(blank=True, max_length=100, null=True)),
                ('parenttype', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.BigIntegerField(blank=True, null=True)),
                ('sku', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('sku_description', models.CharField(blank=True, max_length=255, null=True)),
                ('standard_crate_quantity', models.CharField(blank=True, max_length=255, null=True)),
                ('creation', models.DateTimeField(default=datetime.datetime(2023, 1, 26, 12, 12, 6, 825102))),
                ('modified', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
