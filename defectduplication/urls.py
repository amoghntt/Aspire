from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from defectduplication.models import defectduplication
from . import views

urlpatterns = [
    url(r'^result/$', views.result, name='defectduplication'),
    url(r'^$', views.simple_upload, name='simple_upload'),]

