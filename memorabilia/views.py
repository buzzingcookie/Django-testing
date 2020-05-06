from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date
from .models import *
import calendar

def memorabilia(request):
    currentYear = datetime.now().year
    currentMonth = datetime.now().month

    i = 2

    month = calendar.monthcalendar(2020, i)
    months = calendar.month_name[i]
    days = calendar.day_name


    context = {
        'currentMonth': currentMonth,
        'currentYear':currentYear, 
        'month':month,
        'months':months,
        'days':days 
    }
    return render(request, 'memorabilia/memorabilia-index.html', context)
