from django.contrib import admin
from .models import *

# Register your models here.
#Artist
admin.site.register(Instrument)
admin.site.register(Gender)
admin.site.register(Agency)
admin.site.register(Artist)
#Place
admin.site.register(EventName)
admin.site.register(Event)
admin.site.register(Place)
#Show
admin.site.register(Show)
