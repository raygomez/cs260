from django.shortcuts import render
from todolist.models import ToDo
from django.contrib.auth.decorators import user_passes_test

import datetime
from django.contrib.auth.decorators import login_required
from todolist.forms.AddToDoForm import AddToDoForm
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse


@login_required()
def index(request):
    dateToday = datetime.date.today()
    todos = ToDo.objects.filter(dateAdded=dateToday, user=request.user)
    form = AddToDoForm()

    context = {'dateToday' : dateToday.strftime('%b %d, %Y'),
               'todos' : todos, 'form' : form}
            
    return render(request, 'index.html', context)

@login_required()
def update(request):
    
    if request.method == 'GET':
        if 'pk' in request.GET and 'isOn' in request.GET:
            id = int(request.GET.get('pk'))
            state = request.GET.get('isOn') == 'True'
            todo = ToDo.objects.get(pk=id, user=request.user)
            todo.isDone = state
            todo.save()
        else: return HttpResponseRedirect('index')
    else: return HttpResponseRedirect('index')
    

@login_required()
def add(request):
    
    if request.method == 'POST':
        form = AddToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False);
            todo.user = request.user
            todo.save()
    return HttpResponseRedirect('index')


def isAdmin(user):
    return user.is_staff

@user_passes_test(isAdmin)
def addUser(request):
    return HttpResponse()
