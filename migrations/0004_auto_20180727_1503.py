# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-27 09:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0003_auto_20180727_1459'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='student_feedback',
            unique_together=set([]),
        ),
    ]