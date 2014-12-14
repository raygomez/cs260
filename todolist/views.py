from django.shortcuts import render

from todolist.models import ToDo

import datetime

def index(request):
    dateToday = datetime.date.today()
    todos = ToDo.objects.filter(dateAdded=dateToday)

    context = {'dateToday' : dateToday.strftime('%b %d, %Y'),
               'todos' : todos}
    return render(request, 'index.html', context)
