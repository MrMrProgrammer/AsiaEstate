from itertools import chain
from operator import attrgetter
from django.shortcuts import render
from django.views.generic import ListView
from .models import Land, Villa, Apartment
from BaseConfig.models import FooterData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseNotFound


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

    ads_per_page = footer_data.per_page_item
    paginator = Paginator(all_ads, ads_per_page)

    page = request.GET.get('page')

    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    context = {
        # 'lands': lands,
        # 'villas': villas,
        # 'apartments': apartments,
        'all_ads': ads,
        'FooterData': footer_data,
    }

    return render(request, 'Ads/AllAds.html', context)


def show_land_ads(request):
    lands = Land.objects.all().order_by('-id')

    footer_data = FooterData.objects.filter(is_active=True).last()

    ads_per_page = footer_data.per_page_item
    paginator = Paginator(lands, ads_per_page)

    page = request.GET.get('page')

    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    context = {
        'lands': ads,
        'FooterData': footer_data,
    }

    return render(request, 'Ads/LandAds.html', context)


def show_villa_ads(request):
    villas = Villa.objects.all().order_by('-id')

    footer_data = FooterData.objects.filter(is_active=True).last()

    ads_per_page = footer_data.per_page_item
    paginator = Paginator(villas, ads_per_page)

    page = request.GET.get('page')

    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    context = {
        'villas': ads,
        'FooterData': footer_data,
    }

    return render(request, 'Ads/VillaAds.html', context)


def show_apartment_ads(request):
    apartments = Apartment.objects.all().order_by('-id')

    footer_data = FooterData.objects.filter(is_active=True).last()

    ads_per_page = footer_data.per_page_item
    paginator = Paginator(apartments, ads_per_page)

    page = request.GET.get('page')

    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    context = {
        'apartments': ads,
        'FooterData': footer_data,
    }

    return render(request, 'Ads/ApartmentAds.html', context)


def show_single_ad(requesst, db_name, ad_id):
    if db_name == 'Land':

        single_ad = Land.objects.filter(id=ad_id).first()

    elif db_name == 'Villa':
        single_ad = Villa.objects.filter(id=ad_id).first()

    elif db_name == 'Apartment':
        single_ad = Apartment.objects.filter(id=ad_id).first()

    else:
        return HttpResponseNotFound()

    footer_data = FooterData.objects.filter(is_active=True).last()

    seprator = 10000

    context = {
        'single_ad': single_ad,
        'FooterData': footer_data,
        'seprator' : seprator,
    }

    return render(requesst, 'Ads/ShowPerAd.html', context)