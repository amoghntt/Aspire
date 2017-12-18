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
from .scripts import uc2_test_case_optimization, testcaseread_post,post
import os
from django.conf import settings
import pandas as pd
import xlsxwriter
import os, sys
import glob
import ntpath
from .forms import FileFieldForm
from django.views.generic.edit import FormView

def index(request):
    return render(request, 'scriptsOptimization/scriptsOptimization.html')

def result(request):
    corpora = request.POST.get('corpora',False)
    print corpora
    corpora_lan=corpora
    
   # print test_ref
    #test_result=uc2_test_case_optimization.optimize(corpora)
    #print test_ref
    tc=[]
    i=1
    path= "/home/aspire/client/juniper/juniper/media/testcases"
    test=[]
    
    print 'hiiiii'
    pathresults='/home/aspire/client/juniper/juniper1/static/juniper/documents/results/'
    for filename in glob.glob(os.path.join(pathresults, '*.csv')):
        #filename=str(ntpath.basename(filename)
        print '- ' + filename
        if os.path.isfile(filename):
            print 'deleting'
            os.unlink(filename)
    for filename in glob.glob(os.path.join(path, '*.xlsx')):
        filename=str(ntpath.basename(filename))
        print filename
        test_ref=testcaseread_post.readTestCasesFromExcelFile(filename)
        test_result=uc2_test_case_optimization.optimize(corpora,filename)
        test.append(test_result)
        print test_result
        test_case=[]
        test_results=[]
        actual=[]*len(test_result)
        for x in test_result:
            tc.append("TC"+str(i))
            actual.append("TC"+str(i))
            for y in x:
                actual.append(y)
            i=i+1
            test_results.append(actual)
            actual=[]
        print(tc)
        print test_results
        print test_result
        with open('/home/aspire/client/juniper/juniper1/static/juniper/documents/results/'+filename+'_result.csv', 'w') as csv:
            csv.write('')
            csv.write(',')
            for tc1 in tc:
                csv.write(str(tc1))
                csv.write(',')
            csv.write('\n')
            i=1
            for col in test_result:
                csv.write('TC'+str(i))
                csv.write(',')
                for row in col:
                    csv.write(str(row))
                    csv.write(',')
                csv.write('\n')
                i=i+1
        csv.close()
        with open('/home/aspire/client/juniper/juniper1/static/juniper/documents/opt/textrequirementprocessed.txt','r') as p:
            lines=p.readlines()
            for line in lines:
                #print line
                test_case.append(str(line))
        with open('/home/aspire/client/juniper/juniper1/static/juniper/documents/results/'+filename+'_result_Duplicate.csv', 'w') as csv:
            csv.write('Duplicate TC Pair')
            csv.write(',')
            csv.write('\n')
            i=1
            j=1
            for row in test_result:
                j=1
                for col in row:
                    if(col>=90 and j>1 and col<=100):
                        if(i!=j):
                            #tc_pair= str(i)+','+str(j)
                            csv.write(str(test_ref[i-1]))
                            csv.write(',')
                            csv.write(str(i))
                            csv.write(',')
                            csv.write(str(j))
                            csv.write(',')
                            csv.write(str(test_ref[j-1]))
                            csv.write('\n')
                            csv.write(str(test_case[i-1]))
                            #csv.write('\n')
                            csv.write(str(test_case[j-1]))
                        
                            csv.write('\n')
                    j=j+1
                i=i+1
        csv.close()
        with open('/home/aspire/client/juniper/juniper1/static/juniper/documents/results/'+filename+'_result_Redun.csv', 'w') as csv:
            csv.write('Redundant TC Pair')
            csv.write(',')
            csv.write('\n')
            i=1
            j=1
            #k=0
            for row in test_result:
                j=1
                for col in row:
                    if(col>75 and col<90 and j>1):
                        #tc_pair= str(i)+','+str(j)
                        #csv.write(tc_pair)
                        #csv.write(str(i),str(j))
                        csv.write(str(test_ref[i-1]))
                        csv.write(',')
                        csv.write(str(i))
                        csv.write(',')
                        csv.write(str(j))
                        csv.write(',')
                        csv.write(str(test_ref[j-1]))
                        csv.write('\n')
                        csv.write(str(test_case[i-1]))
                        csv.write(str(test_case[j-1]))
                        csv.write('\n')
                    j=j+1
                i=i+1
        csv.close()

    context={
        #"data":test_result,
        "data": test_results,
        "TC":tc
        }
    return render(request,'scriptsOptimization/result.html' ,context)

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
    return render(request, 'scriptsOptimization/scriptsOptimization.html', {
        'uploaded_file_url': uploaded_file_url
        })


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'scriptsOptimization/scriptsOptimization.html'
    success_url = '#'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        path= "/home/aspire/client/juniper/juniper/media/testcases"
        for filename in glob.glob(os.path.join(path, '*.xlsx')):
            #filename=str(ntpath.basename(filename))
            print '- ' + filename
            if os.path.isfile(filename):
                print 'deleting'
                os.unlink(filename)
        #os.remove(filename)
        files = request.FILES.getlist('file_field')
        fs=FileSystemStorage()
        if form.is_valid():
            for f in files:
                #pprint("Name of file is " + f._get_name() + ' ' + f.field_name, sys.stderr)
                #new_file = FileModel(file=f)
                #new_file.save()
                #f.save(str(i)+'test.xlsx',f)
                filename=fs.save('testcases/'+f.name,f)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
