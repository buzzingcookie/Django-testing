#Main URLS

from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),

    path('lineup/', include('lineup.urls')),

    path('artists/', include('artists.urls')),

    path('memorabilia/', include('memorabilia.urls')),
]
