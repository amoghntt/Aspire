from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from scriptsOptimization.models import ScriptsOptimization
from . import views

urlpatterns = [
    url(r'^result/$', views.result, name='testcoverage'),
    url(r'^$', views.simple_upload, name='simple_upload'),]

