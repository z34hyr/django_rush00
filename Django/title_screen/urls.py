from django.urls import path
from .views import TitlePageView

urlpatterns = [
    path('', TitlePageView.page, name='home')
]