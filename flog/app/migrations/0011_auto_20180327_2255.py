# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-27 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20180327_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specify',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
