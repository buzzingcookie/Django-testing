from django.db import models
from datetime import datetime, date

# Lineup MODELS.

#----------------------ARTISTS----------------------------#

class Instrument(models.Model):
    instrument = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.instrument

class Gender(models.Model):
    Gender = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Gender

class Agency(models.Model):
    Agency = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Agency

class Artist(models.Model):
    Name = models.CharField(max_length=100, null=True)
    Surname = models.CharField(max_length=100, null=True)
    Nickname = models.CharField(max_length=100, null=True)
    Gender = models.ForeignKey(Gender, null=True, on_delete= models.SET_NULL)
    Instruments = models.ManyToManyField(Instrument)

    NIE = models.CharField(max_length=100, null=True, blank=True)
    N_Price = models.DecimalField(null=True,max_digits=8, decimal_places=2, blank=True)
    B_Price = models.DecimalField(null=True,max_digits=8, decimal_places=2, blank=True)
    IRPF = models.FloatField(null=True)
    Agency = models.ForeignKey(Agency, null=True, on_delete= models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Nickname


#----------------------PLACES----------------------------#

class Place(models.Model):
    Place = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Place

#----------------------EVENTS----------------------------#

class EventName(models.Model):
    EventName = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.EventName


class Event(models.Model):
    EventName = models.ForeignKey(EventName, null=True, on_delete= models.SET_NULL)
    Artist = models.ForeignKey(Artist, null=True, on_delete= models.SET_NULL)
    Place = models.ForeignKey(Place, null=True, on_delete= models.SET_NULL)


#----------------------SHOWS----------------------------#

class Show(models.Model):
    Artist = models.ForeignKey(Artist, null=True, on_delete= models.SET_NULL)
    Place = models.ForeignKey(Place, null=True, on_delete= models.SET_NULL)
    Start = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    End = models.TimeField(auto_now=False, auto_now_add=False, null=True)
    Date = models.DateField(auto_now=False, auto_now_add=False, null=True)
