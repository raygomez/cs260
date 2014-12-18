from django.shortcuts import render

from todolist.models import ToDo

import datetime
from django.contrib.auth.decorators import login_required
from todolist.forms.AddToDoForm import AddToDoForm

@login_required()
def index(request):
    dateToday = datetime.date.today()
    todos = ToDo.objects.filter(dateAdded=dateToday)
    
    if request.method == 'GET':
        form = AddToDoForm()


    context = {'dateToday' : dateToday.strftime('%b %d, %Y'),
               'todos' : todos, 'form' : form}
            
    return render(request, 'index.html', context)

