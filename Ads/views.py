from django.shortcuts import render
from django.views.generic import ListView
from .models import Land, Villa, Apartment


def showLandAds(request):

    lands = Land.objects.all()

    context = {
        'lands': lands,
    }

    return render(request, 'Ads/LandAds.html', context)


def showVillaAds(request):

    villas = Villa.objects.all()

    context = {
        'villas': villas,
    }

    return render(request, 'Ads/VillaAds.html', context)


def showApartmentAds(request):

    apartments = Apartment.objects.all()

    context = {
        'apartments': apartments,
    }

    return render(request, 'Ads/ApartmentAds.html', context)
