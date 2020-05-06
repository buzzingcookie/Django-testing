from django.shortcuts import render
from django.http import HttpResponse
from lineup.models import *

import calendar

def artists(request):

    artists = Artist.objects.all()
    currentYear = datetime.now().year
    currentMonth = datetime.now().month

    context = {
        'currentYear':currentYear,
        'currentMonth':currentMonth,
        'artists': artists,
    }
    return render(request, 'artists/artists-index.html', context)


def artist(request, artist_nickname):

    artist = Artist.objects.get(Nickname=artist_nickname)
    instruments = artist.Instruments.all()

    shows = artist.show_set.all()
    show_count = shows.count()

    context = {
        'shows':shows,
        'show_count':show_count,
        'artist': artist,
        'instruments':instruments,
    }
    return render(request, 'artists/artist-show.html', context)
