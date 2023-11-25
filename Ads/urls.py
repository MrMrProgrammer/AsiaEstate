from django.urls import path
from . import views

urlpatterns = [
    path('AllAds', views.all_ads, name='AllAds'),
    path('Land', views.show_land_ads, name='showLandAds'),
    path('Villa', views.show_villa_ads, name='showVillaAds'),
    path('Apartment', views.show_apartment_ads, name='showApartmentAds'),
]