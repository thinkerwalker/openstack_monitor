# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-22 12:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_mgr', '0002_auto_20180415_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]
