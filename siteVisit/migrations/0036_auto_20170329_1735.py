# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-29 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0035_auto_20170329_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageinarticle',
            name='image',
            field=models.FileField(upload_to='i'),
        ),
    ]
