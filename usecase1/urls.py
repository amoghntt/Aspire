from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from perlscripts.models import Scripts
from . import views
urlpatterns = [
    url(r'^result/$', views.use,name="usecase_result"),
    url(r'^details/$', views.details,name="details"),
    url(r'^update_predictioncount/$', views.update_predictioncount,name="update_predictioncount")]

