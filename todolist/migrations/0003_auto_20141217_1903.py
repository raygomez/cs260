# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_auto_20141214_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='dateAdded',
            field=models.DateField(default=datetime.date(2014, 12, 17)),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(max_length=200, default=''),
        ),
    ]
