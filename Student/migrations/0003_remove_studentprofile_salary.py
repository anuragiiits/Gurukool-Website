# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-06 18:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_auto_20180905_2125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofile',
            name='salary',
        ),
    ]
