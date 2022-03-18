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


def about(request):
     return render(request, 
            'listings/about.html')

def contact(request):
    return render(request, 
            'listings/contact.html')


def listing(request):
    titles = Title.objects.all()
    return render(request, 
            'listings/listing.html',
            {'titles': titles})

def band_detail(request, id):  # notez le paramètre id supplémentaire
   band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
   return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit