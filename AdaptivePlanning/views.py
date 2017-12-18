# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, Http404
from .scripts import Updatedb ,randomforestregressionLoad
from .Updatedb import *
from django.shortcuts import render, get_object_or_404
from .models import adaptive ,pk,adaptive1,pk1
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_deny

@xframe_options_deny
@login_required(login_url='/juniper/login')
def adp(request):
    #release = Updatedb.col1()
    #dd=Updatedb.col2()
    #dl=Updatedb.col3()
    #dr=Updatedb.col4()
    #tcc=Updatedb.col5()
    #ac=Updatedb.col6()
    #dk=Updatedb.col7()
    #ts=Updatedb.col8()
    #rqc=Updatedb.col9()
    #crc=Updatedb.col10()
    #drc=Updatedb.col11()
    #nr=Updatedb.col12()
    #bu=Updatedb.col13()
    #eta=Updatedb.col14()
    #cr=Updatedb.col15()
    #eff=Updatedb.col16()
    Re = request.POST.get('Release')
    db=adaptive.objects.all()
    db1 = adaptive1.objects.all()
   # release = SR_ID

    context={
        "db":db,
        "db1": db1,
        #"DD": dd,
        #"Re": Re,
        #"DefectLeakage": dl,
        #"DefectRejection": dr,

        #"TestCaseCount": tcc,
        #"ApplicationComplexity": ac,
        #"DomainKnowledge": dk,
        #"TechnicalSkills": ts,
        #"ReqQueryCount": rqc,
        #"CodeReviewComments": crc,
        #"DesignReviewComments": drc,
        #"NoofResources": nr,
        #"BudgetinUse": bu,
        #"ETA":eta,
        #"CostofResource": cr,
        #"Efficiency": eff,
        #"Project Status": ProjectStatus,
      # "Availability of Budget": AvailabilityofBudget

        }
    return render(request, 'AdaptivePlanning/matrics1.html', context)

@login_required(login_url='/juniper/login')
def clicked(request,Release_id):
    ad= adaptive.objects.all()

   # Adaptive=get_object_or_404(adaptive , pk =Release_id)
 #   try:
  #      clicked_element=pk.Release.get(pk=request.POST['Release'])
  #  except(KeyError,Release_id.DoesNotExist):
  #        return render(request,'AdaptivePlanning/matrics1.html',{
  #        'adptive':adaptive,
   #       'error':"You did not select any Release to Pridict",

   #       })
 #   else:
 #       clicked_element.is_clicked =True
 #       clicked_element.save()
    return render(request, 'AdaptivePlanning/result.html',{'adaptive':ad})

@login_required(login_url='/juniper/login')
def result(request):
    db = adaptive.objects.all()
    Re = request.POST.get('Release')
    context = {
        "db": db,
        "Re": Re,

    }
    return render(request, 'AdaptivePlanning/test.html',context)

@xframe_options_deny
@login_required(login_url='/juniper/login')
def predict(request, Release_id):
    db = adaptive.objects.all()
    P = pk.objects.get(pk=Release_id)
    releaseId = request.POST.get('releaseId', False)
    defectDensity = request.POST.get('defectDensity', False)
    defectLeakage = request.POST.get('defectLeakage', False)
    defectRejection = request.POST.get('defectRejection', False)
    testCaseCount = request.POST.get('testCaseCount', False)
    applicationComplexity = request.POST.get('applicationComplexity', False)
    domainKnowledge = request.POST.get('domainKnowledge', False)
    technicalSkills = request.POST.get('technicalSkills', False)
    requirementQueryCount = request.POST.get('requirementQueryCount', False)
    codeReviewComments = request.POST.get('codeReviewComments', False)
    designReviewComments = request.POST.get('designReviewComments', False)
    numberOfResources = request.POST.get('numberOfResources', False)
    budgetInUse = request.POST.get('budgetInUse', False)
    numberOfDaysToComplete = request.POST.get('numberOfDaysToComplete', False)
    costOfResource = request.POST.get('costOfResource', False)
    efficiency = request.POST.get('efficiency', False)
    projectStatus = request.POST.get('projectStatus', False)
    availabilityOfBudget = request.POST.get('availabilityOfBudget', False)


    res = [defectDensity,defectLeakage,defectRejection,testCaseCount,applicationComplexity,domainKnowledge,technicalSkills,requirementQueryCount,codeReviewComments,designReviewComments,numberOfResources,budgetInUse,numberOfDaysToComplete,costOfResource,efficiency,projectStatus,availabilityOfBudget]


    a1,a2 = randomforestregressionLoad.res(res)
    context = {
        "db": db,
        "P":P,
        "releaseId": releaseId,
        "defectDensity":defectDensity,
        "defectLeakage": defectLeakage,
        "defectRejection": defectRejection,

        "testCaseCount": testCaseCount,
        "applicationComplexity": applicationComplexity,
        "domainKnowledge": domainKnowledge,
        "technicalSkills": technicalSkills,
        "requirementQueryCount": requirementQueryCount,
        "codeReviewComments": codeReviewComments,
        "designReviewComments": designReviewComments,
        "numberOfResources": numberOfResources,
        "budgetInUse": budgetInUse,
        "numberOfDaysToComplete": numberOfDaysToComplete,
        "costOfResource": costOfResource,
        "efficiency": efficiency,
        "projectStatus": projectStatus,
        "availabilityOfBudget": availabilityOfBudget,
        "a1": a1,
        "a2": a2,


    }
    return render(request, 'AdaptivePlanning/result.html',context)

@xframe_options_deny
@login_required(login_url='/juniper/login')
def check(request, Release_id):
    db=pk1.objects.all()
    db1=adaptive1.objects.all()
    db2 = adaptive.objects.all()
    releaseId =request.POST.get('releaseId',False)
    #projectstatus = request.POST.get('projectStatus', False)
    context = {
        "db": db,
        "db1": db1,
        "db2": db2,
        "releaseId":releaseId,

        #"projectstatus": projectstatus
    }
    try :
        P=pk1.objects.get(pk=Release_id)
    except pk1.DoesNotExist:
        raise Http404 ("Does Not exist")

    return render(request , 'AdaptivePlanning/detail.html',{'P':P,'db1': db1 ,'db2': db2,'releaseId':releaseId})

@xframe_options_deny
@login_required(login_url='/juniper/login')
def check1(request):
    db = adaptive.objects.all()
    db1 = adaptive1.objects.all()
    # release = SR_ID

    context = {
        "db": db,
        "db1": db1,
    }
    return render(request, 'AdaptivePlanning/matrics1.html', context)
