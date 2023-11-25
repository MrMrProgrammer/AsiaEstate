from django.shortcuts import render
from .models import AboutUs
from BaseConfig.models import FooterData


def about_us(request):

    about_us = AboutUs.objects.filter(is_active=True).last()
    
    footer_data = FooterData.objects.filter(is_active=True).last()

    context = {
        'about_us': about_us,
        'FooterData': footer_data,
    }

    return render(request, 'AboutUs/about_us.html', context)
