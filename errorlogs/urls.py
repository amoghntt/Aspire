from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from errorlogs.models import Errorlogs

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Errorlogs.objects.all,template_name="errorlogs/errorlogs.html"))]

