# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-23 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20181023_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='thread',
            name='creation_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
