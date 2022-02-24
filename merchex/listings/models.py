from django.db import models


class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(max_length=1000) 
   
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)

class Title(models.Model):
    title = models.fields.CharField(max_length=100)

