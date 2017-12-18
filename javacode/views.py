# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .scripts import javacode,perlscripts
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_deny

@xframe_options_deny
@login_required(login_url='/juniper/login')
def index(request):
    return render(request, 'javacode/javacode.html')

@xframe_options_deny
@login_required(login_url='/juniper/login')
def java(request):
    perl_data = perlscripts.pred()
    source_data = javacode.pred()
    print(perl_data)
    context={
        "perl_data": perl_data,
        "source_data" : source_data
        }
    return render(request, 'javacode/result.html', context)
