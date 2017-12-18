# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import Document
from .forms import DocumentForm
from .scripts import defectduplication
import os
from django.conf import settings

def index(request):
    return render(request, 'defectduplication/defectduplication.html')

def result(request):
    corpora = request.POST.get('corpora',False)
    print corpora
    test_result=defectduplication.optimize(corpora)
    tc=[]
    i=1
    test_results=[]
    actual=[]*len(test_result)
    for x in test_result:
        tc.append("D-ID"+str(i))
        actual.append("D-ID"+str(i))
        for y in x:
            actual.append(y)
        i=i+1
        test_results.append(actual)
        actual=[]
    print(tc)
    print test_results
    print test_result
    context={
        #"data":test_result,
        "data":test_results,
        "TC":tc
        }
    return render(request,'defectduplication/result.html' ,context)

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        name='Book2.xlsm'
        file_name=fs.get_valid_name('Book2.xlsm')
        if(file_name==name):
            fs.delete(file_name)
        filename = fs.save('Book2.xlsm', myfile)
        uploaded_file_url = fs.url(filename)
    return render(request, 'defectduplication/defectduplication.html', {
        'uploaded_file_url': uploaded_file_url
        })
