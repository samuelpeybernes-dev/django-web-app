from email import message
from os import mkdir
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Title
from listings.forms import ListingForm, BandForm, ContactUsForm
from django.core.mail import send_mail
from django.shortcuts import redirect

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

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
            'listings/band_create.html',
            {'form': form})

def band_update(request, id):  
    band = Band.objects.get(id=id)  

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)  # on pré-remplir le formulaire avec un groupe existant
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
            
    else:
        form = BandForm(instance=band)

    return render(request,
          'listings/band_update.html',
          {'form': form, 'band': band}) 


def about(request):
     return render(request, 
            'listings/about.html')

def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message de {form.cleaned_data["name"] or "anonyme"} via formulaire de contact',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-envoye')  # ajoutez cette instruction de retour

            # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
            # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).
    else:
        # ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request, 
            'listings/contact.html',
            {'form': form})  # passe ce formulaire au gabarit


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

def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            titles = form.save()
            return redirect('listing-detail', titles.id)

    else:
        form = ListingForm()

    return render(request,
            'listings/listing_create.html',
            {'form': form})

def listing_update(request, id):  
    title = Title.objects.get(id=id)  
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=title)  # on pré-remplir le formulaire avec un groupe existant
        if form.is_valid():
            form.save()
            return redirect('listing-detail', title.id)
            
    else:
        form = ListingForm(instance=title)

    return render(request,
          'listings/listing_update.html',
          {'form': form, 'title': title}) 

