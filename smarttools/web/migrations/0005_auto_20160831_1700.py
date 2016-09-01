# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 22:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20160831_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='converted_video',
            field=models.FileField(blank=True, null=True, upload_to='videos'),
        ),
        migrations.AlterField(
            model_name='video',
            name='original_video',
            field=models.FileField(null=True, upload_to='videos'),
        ),
    ]