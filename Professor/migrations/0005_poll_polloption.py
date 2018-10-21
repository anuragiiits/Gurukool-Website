# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-10-11 16:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Professor', '0004_course_courseprofessor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('question', models.CharField(max_length=100)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Professor.Course')),
                ('professor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Professor.ProfessorProfile')),
            ],
        ),
        migrations.CreateModel(
            name='PollOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=100)),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Professor.Poll')),
            ],
        ),
    ]
