from django.db import models
from datetime import datetime, date

# Lineup MODELS.

#----------------------ARTISTS----------------------------#

class ArtistType(models.Model):
    Type = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Type

class Artist(models.Model):
    Name = models.CharField(max_length=100, null=True)
    Surname = models.CharField(max_length=100, null=True)
    GENDERS = (
        ('Male','Male'),
        ('Female','Female'),
    )
    Gender = models.CharField(max_length=100, null=True, choices=GENDERS)
    Types = models.ManyToManyField(ArtistType)
    NIE = models.CharField(max_length=100, null=True)
    N_Price = models.FloatField(null=True)
    B_Price = models.FloatField(null=True)
    IRPF = models.FloatField(null=True)
    AGENCYS = (
        ('THM','THM'),
        ('AUTONOMO','AUTONOMO'),
    )
    Agency = models.CharField(max_length=50, null=True, choices=AGENCYS)
    date_created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.Name

#----------------------PLACES----------------------------#

class Place(models.Model):
    Place = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Place

#----------------------EVENTS----------------------------#

class Event(models.Model):
    Name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.Name

#----------------------SHOWS----------------------------#

class Show(models.Model):
    Artist = models.ForeignKey(Artist, null=True, on_delete= models.SET_NULL)
    Place = models.ForeignKey(Place, null=True, on_delete= models.SET_NULL)


    def __str__(self):
        return self.Artist
