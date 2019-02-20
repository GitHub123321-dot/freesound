# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-05 11:53
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sounds', '0030_auto_20180618_1305'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoundAnalysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('extractor', models.CharField(db_index=True, max_length=255)),
                ('analysis_filename', models.CharField(max_length=255, null=True)),
                ('analysis_data', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('sound', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='analyses', to='sounds.Sound')),
            ],
        ),
    ]