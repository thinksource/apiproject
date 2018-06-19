from django.urls import path,re_path
from django.conf.urls import url
from . import views
from .models import Pulse
from rest_framework import serializers, viewsets, routers

     
urlpatterns = [
    re_path(r'^pulses$', views.PulseList.as_view(), name='pulse_list'),
    re_path(r'^pulse/(?P<pk>[0-9]*)$', views.PulseDetail.as_view(), name='pulse_detail'),
    re_path(r'create_pulse/$', views.PulseCreate.as_view(), name='pulse_create'),
    path(r'^uploadfiles/$', views.FileUploadView.as_view(), mame="pulse_upload"),

]