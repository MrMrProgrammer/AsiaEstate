from django.shortcuts import render
from django.views.generic import ListView
from .models import Land, Villa, Apartment


class ShowLandAds(ListView):
    model = Land
    queryset = Land.objects.all().order_by('id')
    template_name = 'Ads/LandAds.html'
    context_object_name = 'lands'
    paginate_by = 1


class ShowVillaAds(ListView):
    model = Villa
    queryset = Villa.objects.all().order_by('id')
    template_name = 'Ads/VillaAds.html'
    context_object_name = 'villas'
    paginate_by = 1


class ShowApartmentAds(ListView):
    model = Apartment
    queryset = Apartment.objects.all().order_by('id')
    template_name = 'Ads/ApartmentAds.html'
    context_object_name = 'apartments'
    paginate_by = 1
