# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 22:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_auto_20161027_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team_result',
            field=models.CharField(default='', max_length=25),
        ),
    ]
