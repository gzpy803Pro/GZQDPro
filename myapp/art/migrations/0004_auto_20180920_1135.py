# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-20 03:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0003_volumesetmodel_free_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='add_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 9, 20, 11, 35, 47, 122848), null=True, verbose_name='发布时间'),
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='art/images', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='chaptermodel',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='发布时间'),
        ),
        migrations.AlterField(
            model_name='chaptermodel',
            name='char_size',
            field=models.IntegerField(blank=True, verbose_name='字数'),
        ),
    ]
