# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-11 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20170511_0900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buscompany',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='buscompany',
            name='longitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
