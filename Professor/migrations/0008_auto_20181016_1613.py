# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-16 16:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Professor', '0007_auto_20181016_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizquestion',
            old_name='is_multiples_correct',
            new_name='is_multiple_correct',
        ),
    ]
