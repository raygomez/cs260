from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    dateToday = datetime.date.today()
    context = {'dateToday': dateToday.strftime('%m-%d-%Y')}
    return render(request, 'index.html', context)
