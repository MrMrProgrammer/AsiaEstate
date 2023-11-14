from itertools import chain
from operator import attrgetter
from django.shortcuts import render
from django.views.generic import ListView
from .models import Land, Villa, Apartment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from BaseConfig.models import FooterData


def all_ads(request):
    lands = Land.objects.all()
    villas = Villa.objects.all()
    apartments = Apartment.objects.all()

    all_ads = []

    for i in lands:
        all_ads.append(i)

    for i in villas:
        all_ads.append(i)

    for i in apartments:
        all_ads.append(i)

    all_ads = sorted(all_ads, key=lambda ad: ad.dateTimeCreated, reverse=True)

    footer_data = FooterData.objects.filter(is_active=True).last()

    context = {
        'lands': lands,
        'villas': villas,
        'apartments': apartments,
        'all_ads': all_ads,
        'FooterData': footer_data
    }
    return render(request, 'Ads/AllAds.html', context)


class ShowLandAds(ListView):
    # model = Land
    # queryset = Land.objects.all().order_by('id')
    template_name = 'Ads/LandAds.html'
    context_object_name = 'lands'
    paginate_by = 1

    def get_queryset(self):
        queryset1 = Land.objects.all().order_by('id')
        queryset2 = FooterData.objects.filter(is_active=True)

        combined_queryset = queryset1.union(queryset2)

        return combined_queryset


class ShowVillaAds(ListView):
    # model = Villa
    # queryset = Villa.objects.all().order_by('id')
    template_name = 'Ads/VillaAds.html'
    # context_object_name = 'villas'
    paginate_by = 1

    def get_queryset(self):
        qs1 = Villa.objects.all()
        qs2 = FooterData.objects.filter(is_active=True)
        queryset = sorted(chain(qs1, qs2), key=attrgetter('timestamp'), )
        return queryset


class ShowApartmentAds(ListView):
    model = Apartment
    queryset = Apartment.objects.all().order_by('id')
    template_name = 'Ads/ApartmentAds.html'
    context_object_name = 'apartments'
    paginate_by = 1
