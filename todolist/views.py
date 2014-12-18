from django.shortcuts import render

from todolist.models import ToDo

import datetime
from django.contrib.auth.decorators import login_required
from todolist.forms.AddToDoForm import AddToDoForm
from django.http.response import HttpResponseRedirect

@login_required()
def index(request):
    dateToday = datetime.date.today()
    todos = ToDo.objects.filter(dateAdded=dateToday)
    
    if request.method == 'GET':
        form = AddToDoForm()


    context = {'dateToday' : dateToday.strftime('%b %d, %Y'),
               'todos' : todos, 'form' : form}
            
    return render(request, 'index.html', context)

@login_required()
def add(request):
    
    if request.method == 'POST':
        form = AddToDoForm(request.POST)
        if form.is_valid():
            form.save();
    
    return HttpResponseRedirect('index')