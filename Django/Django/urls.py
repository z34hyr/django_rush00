"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('title_screen/', include('title_screen.urls')),
    # path('save/', include('save.urls')),
    # path('load/', include('load.urls')),
    # path('option/', include('option.urls')),
    # path('battle/', include('battle.urls')),
    # path('detail/', include('detail.urls')),
    path('worldmap/', include('worldmap.urls')),
    # path('moviedex/', include('moviedex.urls')),
]
