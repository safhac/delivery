"""getPackage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls
from django.urls import path, include

from . import views
from getPackage.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('add_delivery', AddDelivery.as_view(), name='add_delivery'),
    path('set_courier/<int:pk>/<int:id>', SetCourierDelivery, name='set_courier'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
