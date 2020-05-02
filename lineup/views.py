from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import calendar

def lineup(request):
    i = 2

    month = calendar.monthcalendar(2020, i)
    months = calendar.month_name[i]
    days = calendar.day_name


    context = { 'month':month, 'months':months, 'days':days }
    return render(request, 'lineup/lineup-index.html', context)
