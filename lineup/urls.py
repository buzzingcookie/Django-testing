from django.urls import path
from . import views
import calendar
from datetime import datetime, date

currentYear = datetime.now().year
currentMonth = datetime.now().month

urlpatterns = [
    #path('', views.lineupCurrent, name="lineup"),
    #path('<int:yearNum>/', views.lineupCurrent, name="currentLineup"),
    path('<int:yearNum>/<int:monthNum>/', views.lineupMonths, name="currentLineup"),
    path('create_show/', views.createShow, name="create_show")
]
