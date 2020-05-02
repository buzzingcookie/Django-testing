#Main URLS

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about/', views.about),

    path('lineup/', include('lineup.urls')),
    path('artists/', include('artists.urls')),
    path('memorabilia/', include('memorabilia.urls')),
]
