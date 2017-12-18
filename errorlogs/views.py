# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .scripts import error_log_gensim_lsi
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_deny

@xframe_options_deny
@login_required(login_url='/juniper/login')
def index(request):
    path="/home/aspire/Juniper_files/Juniper_UC3/Test_Log.txt"
    file = open(path, "r")
    log_data=file.readlines()
    context={
        "log_data": log_data
        }
    return render(request, 'errorlogs/errorlogs.html' , context)



@xframe_options_deny
@login_required(login_url='/juniper/login')
def error_logs(request):
    data= error_log_gensim_lsi.predict_error_log()
    context={
        "data" : data
        }
    return render(request, "errorlogs/result.html", context)
