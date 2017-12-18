from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from javacode.models import Javacode

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Javacode.objects.all,template_name="javacode/javacode.html"))]

