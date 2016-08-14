# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-14 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcs', '0002_shelter'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='Destination',
            field=models.CharField(default='temp', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='files',
            name='Source',
            field=models.CharField(default='tempSrc', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='files',
            name='Name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
