from django.urls import path
from . import views

urlpatterns = [
    path('Land', views.showLandAds, name='showLandAds'),
    path('Villa', views.showVillaAds, name='showVillaAds'),
    path('Apartment', views.showApartmentAds, name='showApartmentAds'),
]
