# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-03 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('guid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('page_data', models.TextField()),
                ('unpublished_page_data', models.TextField(blank=True, null=True)),
                ('meta_data', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
