from django.shortcuts import render
from .models import Gallery
from BaseConfig.models import FooterData


# Create your views here.

def show_gallery(request):
    images = Gallery.objects.filter(is_active=True)

    footer_data = FooterData.objects.filter(is_active=True).last()

    context = {
        'images': images,
        'FooterData': footer_data
    }

    return render(request, 'Gallery/gallery.html', context)