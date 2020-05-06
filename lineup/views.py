from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import calendar
from datetime import datetime, date
from .forms import *


def createShow(request):
    currentYear = datetime.now().year
    currentMonth = datetime.now().month

    form = ShowForm

    if request.method == 'POST':
        print('POST METHOD NOW:', request.POST)
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'currentMonth': currentMonth,
        'currentYear':currentYear,
        'form':form,
    }


    return render(request, 'lineup/create_show.html', context)


def lineupCurrent(request, yearNum):

    nextYear = 2021
    currentYear = datetime.now().year
    currentMonth = datetime.now().month

    monthSelector = calendar.month_name

    monthHeader = calendar.month_name[currentMonth]

    weekDaysMonth = calendar.monthcalendar(yearNum, currentMonth)

    days = calendar.day_name


    context = {
        'nextYear': nextYear,
        'currentYear':currentYear,
        'currentMonth':currentMonth,
        'monthHeader':monthHeader,
        'weekDaysMonth':weekDaysMonth,
        'monthSelector':monthSelector,
        'days':days
    }

    return render(request, 'lineup/lineup-index.html', context)



def lineupMonths(request, yearNum, monthNum):

    month = calendar.monthcalendar(yearNum, monthNum)
    numMonths = [1,2,3,4,5,6,7,8,9,10,11,12]
    monthNames = ['January','February','March','April','May','June','July','August','September','October','November','December']

    c = calendar.TextCalendar(calendar.MONDAY)

    currentYear = datetime.now().year
    currentMonth = datetime.now().month


    months = calendar.month_name[monthNum]

    monthHeader = calendar.month_name[monthNum]
    monthSelector = calendar.month_name

    monthV = calendar.monthcalendar(yearNum, monthNum)
    for weeks in monthV:
        for days in weeks:
            k = days

    days = calendar.day_name

    showsMonthly = Show.objects.filter(Date__year=yearNum,Date__month=monthNum)
    showsDaily = Show.objects.filter(Date__day=k)

    orderedMonthlyShows = showsMonthly.order_by("Start")

    


    context = {
        'yearNum':yearNum,
        'currentYear':currentYear,
        'currentMonth':currentMonth,
        'showsMonthly':showsMonthly,
        'showsDaily':showsDaily,
        'orderedMonthlyShows':orderedMonthlyShows,
        'numMonths': numMonths,
        'monthNames':monthNames,
        'monthSelector':monthSelector,
        'monthHeader':monthHeader,
        'monthV':monthV,
        'months':months,
        'days':days
    }

    return render(request, 'lineup/lineup-monthly.html', context)
