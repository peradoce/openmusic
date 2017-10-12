# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20171006_1246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('facebook', models.CharField(blank=True, max_length=250, null=True)),
                ('twitter', models.CharField(blank=True, max_length=250, null=True)),
                ('youtube', models.CharField(blank=True, max_length=250, null=True)),
                ('wiki', models.CharField(blank=True, max_length=250, null=True)),
                ('bio', models.TextField(max_length=300)),
                ('image', models.FileField(upload_to='artist_images')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('music_file', models.FileField(upload_to='musics')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Genre')),
            ],
        ),
    ]