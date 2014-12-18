from django.db import models
from django.contrib.auth.models import User

import datetime

class ToDo(models.Model):
    description = models.CharField(max_length=200, default="", blank=False)
    isDone = models.BooleanField(default=False)
    dateAdded = models.DateField(default=datetime.date.today())
    user = models.ForeignKey(User, blank=False, default=1)