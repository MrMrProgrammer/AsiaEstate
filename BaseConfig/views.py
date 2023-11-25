from django.shortcuts import render
from BaseConfig.models import FooterData, HomeData, SliderImage
from Log.loggers import saveLog


# Create your views here.

def home(request):
    # --------------
    saveLog(request)
    # --------------

    footer_data = FooterData.objects.filter(is_active=True).last()
    home_data = HomeData.objects.filter(is_active=True).last()
    slider_images = SliderImage.objects.filter(is_active=True)

    context = {
        'FooterData': footer_data,
        'HomeData': home_data,
        'SliderImages': slider_images,
    }

    return render(request, 'BaseConfig/home.html', context)


# # custom 404 view
def custom_404(request, exception):
    return render(request, 'BaseConfig/404.html', status=404)
