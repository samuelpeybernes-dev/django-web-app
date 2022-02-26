from django.contrib import admin

from listings.models import Band
from listings.models import Title

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
 list_display = ('name', 'year_formed', 'genre', 'biography', 'active') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin)

class TitleAdmin(admin.ModelAdmin):
 list_display = ('title', 'description', 'sold', 'year', 'types')

admin.site.register(Title, TitleAdmin)

