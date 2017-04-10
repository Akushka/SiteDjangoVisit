# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-29 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0033_sitename_trycategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitename',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='sitename',
            name='tryCategory',
            field=models.BooleanField(),
        ),
    ]
