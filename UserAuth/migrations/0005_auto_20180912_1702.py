# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-09-12 17:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuth', '0004_auto_20180912_1518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='professorauthprofile',
            old_name='email_verfied',
            new_name='email_verified',
        ),
        migrations.RenameField(
            model_name='studentauthprofile',
            old_name='email_verfied',
            new_name='email_verified',
        ),
    ]
