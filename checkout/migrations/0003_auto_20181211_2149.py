# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-11 21:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20181211_2146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address_line1',
            new_name='address_line_1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_line2',
            new_name='address_line_2',
        ),
    ]
