# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('description', models.CharField(default='', max_length=200)),
                ('isDone', models.BooleanField(default=False)),
                ('dateAdded', models.DateField(default=datetime.date(2014, 12, 18))),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
