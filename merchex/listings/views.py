from os import mkdir
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Title

def hello(request):
    bands = Band.objects.all()
    return render(request, 
            'listings/hello.html',
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

