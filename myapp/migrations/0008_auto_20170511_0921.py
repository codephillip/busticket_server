# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-11 09:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20170511_0920'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bus',
            old_name='numberPlate',
            new_name='number_plate',
        ),
    ]
