# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-15 13:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finding_aids', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='findingaidsentitydate',
            table='finding_aids_dates',
        ),
    ]
