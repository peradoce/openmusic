# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='icon',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
