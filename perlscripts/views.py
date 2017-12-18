# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .scripts import perlscripts
from django.shortcuts import render
from django.http import HttpResponse
from .models import Scripts
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_deny

@xframe_options_deny
@login_required(login_url='/juniper/login')
def index(request):
    return render(request, 'perlscripts/perlscripts.html')


@xframe_options_deny
@login_required(login_url='/juniper/login')
def perl(request):
    data = perlscripts.pred()
    context={
        "data": data
        }
    if request.method == "POST":
        pathname = request.POST.get("path", None)
        pathname1 = request.POST.get("path1", None)
        result={
            "pathname": pathname
            }
    #return render(request, 'perlscripts/result.html', result)
    return render(request, 'perlscripts/result.html', context)


