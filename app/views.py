from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date
import calendar

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
