from django.shortcuts import render
from .models import Gallery, GallerySetting
from BaseConfig.models import FooterData
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def show_gallery(request):
    images = Gallery.objects.filter(is_active=True).order_by('-id')
    gallery_conf = GallerySetting.objects.filter(is_active=True).last()

    footer_data = FooterData.objects.filter(is_active=True).last()

    per_page = gallery_conf.pagination
    paginator = Paginator(images, per_page)

    page = request.GET.get('page')

    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)

    context = {
        'images': ads,
        'FooterData': footer_data,
    }

    return render(request, 'Gallery/gallery.html', context)