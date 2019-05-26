"""carrental URL Configuration

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
import re

from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from django.conf import settings
from core.views import BaseView, LoginView, LogoutView, \
    AddUserView, SegmentView, CarView, SuccessView, load_dates, email, WellDoneView
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url('login/', LoginView.as_view()),
    url('logout/', LogoutView.as_view()),
    url('adduser/', AddUserView.as_view()),
    url('segment/(?P<segment>[1-5])/', SegmentView.as_view()),
    url('car/(?P<car>(\d)+)/', CarView.as_view()),
    path('', BaseView.as_view()),
    url('success', SuccessView.as_view()),
    url('summary', load_dates),
    url('email', email),
    url('well_done', WellDoneView.as_view())
    # url('(?P<car>[1-99])/'
    # url('reservation/', ReservationView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)