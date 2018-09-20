# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-20 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='账号')),
                ('password', models.CharField(max_length=100, verbose_name='口令')),
                ('nick_name', models.CharField(max_length=20, verbose_name='别名')),
                ('phone', models.CharField(max_length=11, verbose_name='手机号')),
                ('photo', models.CharField(blank=True, max_length=100, null=True, verbose_name='头像')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
                'db_table': 't_user',
            },
        ),
    ]
