# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-26 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_auto_20181026_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
