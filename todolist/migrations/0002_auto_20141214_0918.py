# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='dateAdded',
            field=models.DateField(default=datetime.date(2014, 12, 14)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='isDone',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
