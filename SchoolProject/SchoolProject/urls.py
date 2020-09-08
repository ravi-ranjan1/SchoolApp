"""School URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url,include
from SchoolApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',views.Home),
    url('^Class2/',views.Docs),
    url('^upload/',views.Upload),
    url('^img/',views.showvideo),
    url('^signup/',views.Signup_view),
    url('^accounts/',include('django.contrib.auth.urls')),
    url('^logout/',views.Logout),
    url('^contact/',views.Contact),
    url('^Admission/',views.AdmissionView),
    url('^AdmissionConfirmation/',views.AdmissionCongrates)

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
