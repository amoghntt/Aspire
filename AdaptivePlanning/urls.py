# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView

from . import views
app_name ='AdaptivePlanning'
urlpatterns = [
url(r'^$', views.check1,name='AdaptivePlanning'),
    url(r'^(?P<Release_id>[0-9]+)/$', views.check ,name='Adaptive'),
    url(r'^(?P<Release_id>[0-9]+)/result/$', views.predict ,name='predict'),
    url(r'^(?P<Release_id>[0-9]+)/predict/$', views.predict,name='clicked'),
]

