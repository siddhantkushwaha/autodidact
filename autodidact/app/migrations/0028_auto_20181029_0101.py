# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-28 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0027_auto_20181026_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
