# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-18 05:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papp', '0002_auto_20170912_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='post',
            field=models.FileField(null=True, upload_to='pic'),
        ),
    ]
