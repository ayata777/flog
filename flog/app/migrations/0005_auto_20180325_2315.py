# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-25 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20180325_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='bigcategory_name',
        ),
        migrations.AddField(
            model_name='bigcategory',
            name='title',
            field=models.CharField(default='bigcategory', max_length=20),
        ),
        migrations.AddField(
            model_name='category',
            name='title',
            field=models.CharField(default='category', max_length=20),
        ),
    ]