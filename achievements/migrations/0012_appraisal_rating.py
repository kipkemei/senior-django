# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-13 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0011_auto_20170713_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='appraisal',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default='1', max_length=10),
        ),
    ]