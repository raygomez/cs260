from django.shortcuts import render
from django.http import HttpResponse
import datetime

def index(request):
    dateToday = datetime.date.today()
    return HttpResponse(dateToday.strftime('%m-%d-%Y'))
