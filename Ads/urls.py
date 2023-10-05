from django.urls import path
from . import views

urlpatterns = [
    path('Ads', views.showApartmentView.as_view(), name='showAds'),
]
