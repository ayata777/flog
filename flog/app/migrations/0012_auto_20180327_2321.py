# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-27 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20180327_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specify',
            name='image',
            field=models.ImageField(default='image/None/no-img.jpg', upload_to='image'),
        ),
    ]