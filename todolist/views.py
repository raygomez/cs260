from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    dateToday = datetime.date.today()
    context = {'dateToday': dateToday}
    return render(request, 'index.html', context)
