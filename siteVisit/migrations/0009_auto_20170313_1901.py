# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-13 17:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0008_commentarticle_article'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='sitename',
            table='article',
        ),
    ]