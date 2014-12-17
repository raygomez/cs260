from django.shortcuts import render

from todolist.models import ToDo

import datetime
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    dateToday = datetime.date.today()
    todos = ToDo.objects.filter(dateAdded=dateToday)

    context = {'dateToday' : dateToday.strftime('%b %d, %Y'),
               'todos' : todos}
    return render(request, 'index.html', context)

