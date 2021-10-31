from django.urls import path
from .views import WorldMapView

urlpatterns = [
    path('', WorldMapView.page, name='worldmap')
]