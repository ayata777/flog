# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-27 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20180327_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specify',
            name='text',
        ),
        migrations.AlterField(
            model_name='specify',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]