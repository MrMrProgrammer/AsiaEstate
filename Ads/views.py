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
    apartment = Apartment.objects.all()

    context = {
        'lands': lands,
        'villas': villas,
        'apartment': apartment,
        'all': zip(lands, villas, apartment)
    }
    return render(request, 'Ads/AllAds.html', context)


# class ShowLandAds(ListView):
#     model = Land
#     queryset = Land.objects.all().order_by('id')
#     template_name = 'Ads/LandAds.html'
#     context_object_name = 'lands'
#     paginate_by = 1


def ShowLandAds(request):
    lands = Land.objects.all().order_by('id')
    page = request.GET.get('page', 1)

    paginator = Paginator(lands, 1)

    context = {
        'lands': lands,
    }

    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'Ads/LandAds.html', context)


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
