from django.urls import path
from . import views


urlpatterns = [
    path('', views.artists, name="artists"),
    path('artist/<str:artist_nickname>/', views.artist, name="artist"),
]
