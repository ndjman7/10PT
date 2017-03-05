# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 23:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0007_alter_to_do_list_progress_defalut_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ball',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.Goal')),
            ],
        ),
    ]
