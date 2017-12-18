from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from perlscripts.models import Scripts

urlpatterns = [
    url(r'^perlscripts/$', ListView.as_view(queryset=Scripts.objects.all,template_name="perlscripts/perlscripts.html"))]

