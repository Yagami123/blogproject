# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-10 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_merge_20170706_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
