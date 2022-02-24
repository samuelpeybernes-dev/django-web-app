from tkinter import SOLID
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(max_length=1000) 
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)]
    )
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        HARD_ROCK = 'HR'
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

class Title(models.Model):
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=1000)
    sold = models.fields.BooleanField(default=True)
    year = models.fields.IntegerField(null=True )
    class Type(models.TextChoices):
        RECORDS = 'RE'
        CLOTHING = 'CL'
        POSTERS = 'PO'
        DIVERS = 'DI'
    types = models.fields.CharField(choices=Type.choices, max_length=5)
