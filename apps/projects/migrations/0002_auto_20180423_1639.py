# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-23 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='dever',
            field=models.CharField(max_length=20, verbose_name='负责人'),
        ),
    ]
