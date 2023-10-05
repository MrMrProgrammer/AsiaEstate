from django.shortcuts import render
from django.views.generic import ListView

from .models import Land, Villa, Apartment


class showAdsView(ListView):

    model = None
    template_name = 'Ads/ShowAds.html'
    context_object_name = 'Ads'

    def get_queryset(self):
        lands = Land.objects.all()
        villas = Villa.objects.all()
        apartments = Apartment.objects.all()

        allAds = lands.union(villas, apartments, all=True)

        return allAds


class showLandView(ListView):
    model = Land
    template_name = 'Ads/ShowAds.html'
    queryset = Land.objects.all()
    context_object_name = 'lands'
    paginate_by = 10


class showVillaView(ListView):
    model = Villa
    template_name = 'Ads/ShowAds.html'
    queryset = Villa.objects.all()
    context_object_name = 'villas'
    paginate_by = 10


class showApartmentView(ListView):
    model = Apartment
    template_name = 'Ads/ShowAds.html'
    queryset = Apartment.objects.all()
    context_object_name = 'apartments'
    paginate_by = 10
