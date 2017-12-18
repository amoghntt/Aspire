from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from scriptsOptimization.models import ScriptsOptimization
from . import views
from .views import FileFieldView

urlpatterns = [
    url(r'^result/$', views.result, name='optimize'),
    url(r'^$',  FileFieldView.as_view(), name='simple_upload'),]

