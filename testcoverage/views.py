# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.files.storage import FileSystemStorage
from .scripts import lsa_trial
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'testcoverage/testcoverage.html')

def result(request):
    content =request.POST.get('content')
    print content
    test_result=lsa_trial.coverage()
    print ('************')
    print (test_result)
    status=[]
    for k,v in test_result:
        if v>50:
            status.append('O')
        elif v<20:
            status.append('X')
        else:
            status.append('Intermediate')
    print status
    
    context={
        
        "test_result":test_result,
        "status":status,
        
        }
    return render(request, 'testcoverage/matrics.html',context)

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        name='test-case.xlsm'
        file_name=fs.get_valid_name('test-case.xlsm')
        if(file_name==name):
            fs.delete(file_name)
        filename = fs.save('test-case.xlsm', myfile)
        uploaded_file_url = fs.url(filename)
    return render(request, 'testcoverage/testcoverage.html', {
        'uploaded_file_url': uploaded_file_url
        })
