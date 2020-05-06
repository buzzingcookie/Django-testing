from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date
from lineup.models import *

import calendar

def navBar():
    currentYear = datetime.now().year

    return render(request, 'layouts/navbar.html')

def home(request):

    currentYear = datetime.now().year
    currentMonth = datetime.now().month

    artists = Artist.objects.all()
    total_artists =  artists.count()

    today = date.today()
    shows = Show.objects.all()
    today_shows = Show.objects.filter(Date=today)
    scheduledShows = today_shows.order_by("Start")



    lineupVars = {
        'currentYear': currentYear,
        'currentMonth':currentMonth,
        'today':today,
        'scheduledShows':scheduledShows,
        'artists': artists,
        'total_artists': total_artists,
        'shows': shows,
    }
    return render(request, 'index.html', lineupVars)





def about(request):
    currentYear = datetime.now().year
    currentMonth = datetime.now().month

    context = {
        'currentYear':currentYear,
        'currentMonth': currentMonth, 
    }
    return render(request, 'about.html', context)
