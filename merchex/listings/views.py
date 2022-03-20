from os import mkdir
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Title

def band_list(request):
    bands = Band.objects.all()
    return render(request, 
            'listings/band_list.html',
            {'bands': bands})

def band_detail(request, id):  # notez le paramètre id supplémentaire
   band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
   return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def about(request):
     return render(request, 
            'listings/about.html')

def contact(request):
    return render(request, 
            'listings/contact.html')


def listing_list(request):
    titles = Title.objects.all()
    return render(request, 
            'listings/listing_list.html',
            {'titles': titles})

def listing_detail(request, id):  # notez le paramètre id supplémentaire
   titles = Title.objects.get(id=id)  # nous insérons cette ligne pour obtenir l'annonce avec cet id
   return render(request,
          'listings/listing_detail.html',
          {'titles': titles}) # nous mettons à jour cette ligne pour passer le groupe au gabarit
