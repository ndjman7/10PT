# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_task_progress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='progress',
        ),
        migrations.AddField(
            model_name='todolist',
            name='progress',
            field=models.CharField(choices=[('A', '#1e6823'), ('B', '#44a340'), ('C', '#8cc665'), ('D', '#d6e685'), ('F', '#eeeeee')], default='A', max_length=7),
        ),
    ]
