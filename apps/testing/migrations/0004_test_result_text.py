# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-21 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testing', '0003_auto_20170305_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='result_text',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
