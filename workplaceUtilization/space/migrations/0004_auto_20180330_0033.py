# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-30 04:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0003_auto_20180323_1854'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spacerecord',
            old_name='dateTime',
            new_name='datetime',
        ),
        migrations.RenameField(
            model_name='spacerecord',
            old_name='pctMoment',
            new_name='pctmoment',
        ),
        migrations.RenameField(
            model_name='spacerecord',
            old_name='pctSpace',
            new_name='pctspace',
        ),
    ]
