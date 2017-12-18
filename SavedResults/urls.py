from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from perlscripts.models import Scripts
from . import views
urlpatterns = [
    url(r'^$', views.report,name="usecase_result"),
    #url(r'^details/$', views.details,name="details")
    ]

