
import datetime
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

from todolist.forms.AddUserForm import AddUserForm
from todolist.forms.AddToDoForm import AddToDoForm
from todolist.models import ToDo


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
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.first_name = request.POST.get('first_name')
            new_user.last_name = request.POST.get('last_name')
            new_user.save()
            return HttpResponseRedirect('index')
    else:
        form = AddUserForm() 

    return render(request, 'adduser.html', {'form': form})
