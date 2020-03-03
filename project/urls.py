"""project URL Configuration

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
from django.apps import apps
from django.urls import include, path  # > Django-2.0
from django.contrib import admin
from payu.nonseamless.dashboard.app import application as payu


urlpatterns = [
     path('i18n/', include('django.conf.urls.i18n')),
     path('admin/', admin.site.urls),
     path('', include(apps.get_app_config('oscar').urls[0])),



    path('checkout/payu/', include('payu.nonseamless.urls')),
    path('dashboard/payu/', include(payu.urls)),
]
