# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddMusic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('description', models.TextField(max_length=300)),
                ('code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('description', models.TextField(max_length=300)),
                ('key', models.CharField(max_length=250)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='PlaylistVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_up', models.IntegerField()),
                ('vote_down', models.IntegerField()),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Playlist')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.AddMusic')),
            ],
        ),
        migrations.AddField(
            model_name='addmusic',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Genre'),
        ),
    ]
