from django.urls import path
from . import views

urlpatterns = [
    path('AllAds', views.all_ads, name='AllAds'),
    path('Land', views.ShowLandAds.as_view(), name='showLandAds'),
    path('Villa', views.ShowVillaAds.as_view(), name='showVillaAds'),
    path('Apartment', views.ShowApartmentAds.as_view(), name='showApartmentAds'),
]
