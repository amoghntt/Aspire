# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from django.shortcuts import render
import mysql.connector
from .scripts import save1

from .scripts import uc1_scikit_linear_regression_dd,uc1_scikit_linear_regression_da,uc1_scikit_linear_regression_ddr,uc1_scikit_linear_regression_alld,uc1c_scikit_svr_linear_telephonica_dd,uc1c_scikit_svr_linear_telephonica_da,uc1c_scikit_svr_linear_telephonica_ddr,uc1c_scikit_svr_linear_telephonica_alld
from .scripts import uc1c_scikit_svr_rbf_telephonica_dd,uc1c_scikit_svr_rbf_telephonica_da,uc1c_scikit_svr_rbf_telephonica_ddr,uc1c_scikit_svr_rbf_telephonica_alld
from .scripts import uc1c_scikit_svr_rbf_telephonica_fund,uc1_scikit_linear_regression_fund,uc1c_scikit_svr_linear_telephonica_fund
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_deny



@xframe_options_deny
@login_required(login_url='/juniper/login')
def metrics(request):

    return render(request,'usecase1/matrics.html')
@xframe_options_deny
@login_required(login_url='/juniper/login')
def details(request):
    global graph_data, predicted_data, Relid, ucl, lcl
    Last_Pred=[]
    lastP_Data=[]
    project_in = request.POST.get('project',False)
    Algorithm_in = request.POST.get('Algorithm',False)
    global Module_in
    Module_in = request.POST.get('Module',False)
    
    Trend_in = request.POST.get('Trend',False)
    ucl_in = request.POST.get('UCL',False)
    lcl_in = request.POST.get('LCL',False)


    
    if(Module_in =='Defect Density'):
         print ("no")
         module='Defect Density'
         predicted_data=uc1c_scikit_svr_rbf_telephonica_dd.predict_dc()
         Relid,graph_data,ucl,lcl=uc1c_scikit_svr_rbf_telephonica_dd.graph_data()
         #Last_Pred,lastP_Data=uc1c_scikit_svr_rbf_telephonica_dd.last_prediction()
    elif(Module_in=='Defect Acceptance Rate') :
             print ("no12")
             module='Defect acceptance'
             predicted_data=uc1c_scikit_svr_rbf_telephonica_da.predict_dc()
             Relid,graph_data,ucl,lcl=uc1c_scikit_svr_rbf_telephonica_da.graph_data()
             #Last_Pred,lastP_Data=uc1c_scikit_svr_rbf_telephonica_da.last_prediction()
    elif(Module_in=='Defect Defferal Rate'):
             module='Defect Defferal Rate'
             predicted_data=uc1c_scikit_svr_rbf_telephonica_ddr.predict_dc()
             Relid,graph_data,ucl,lcl=uc1c_scikit_svr_rbf_telephonica_ddr.graph_data()
             #Last_Pred,lastP_Data=uc1c_scikit_svr_rbf_telephonica_ddr.last_prediction()
    elif(Module_in=='All Defect'):
             module='Defect Count'
             predicted_data=uc1c_scikit_svr_rbf_telephonica_alld.predict_dc()
             Relid,graph_data,ucl,lcl=uc1c_scikit_svr_rbf_telephonica_alld.graph_data()
             #Last_Pred,lastP_Data=uc1c_scikit_svr_rbf_telephonica_alld.last_prediction()
    else :
            module='Functional Defect'
            print '3'
            predicted_data=uc1c_scikit_svr_rbf_telephonica_fund.predict_dc()
            Relid,graph_data,ucl,lcl=uc1c_scikit_svr_rbf_telephonica_fund.graph_data()
            #Last_Pred,lastP_Data=uc1c_scikit_svr_rbf_telephonica_fund.last_prediction()


    print 1
    rel_id=len(Relid)
    print("*******************")
    print ucl_in


    context={
        
        "Algorithm_in":Algorithm_in,
        "Prediction_in":Module_in,
        "Trend_in":Trend_in,
        "project_in":project_in,
        "ucl" : ucl[0],
        "lcl" : lcl[0],
       


        }

    return render(request,'usecase1/details.html',context)

@xframe_options_deny
@login_required(login_url='/juniper/login')
def use(request):

    global graph_data, predicted_data, Relid, ucl, lcl
    Last_Pred=[]
    lastP_Data=[]
    module=''
    

    Algorithm_in = request.POST.get('Algorithm',False)
    #Module_in = request.POST.get('Module',False)
    Trend_in = request.POST.get('Trend',False)
    ucl_in = request.POST.get('UCL',False)
    lcl_in = request.POST.get('LCL',False)


    
    if(Algorithm_in == '1' ):
        
        if(Module_in =='Defect Density'):
         print ("yes12")
         module='Defect Density'
         predicted_data=uc1_scikit_linear_regression_dd.predict_dd()
         Relid,graph_data,ucl,lcl=uc1_scikit_linear_regression_dd.graph_data()
         Last_Pred,lastP_Data,Actual,Accuracy=uc1_scikit_linear_regression_dd.last_prediction()
        elif(Module_in=='Defect Acceptance Rate') :
             module='Defect acceptance'
             predicted_data=uc1_scikit_linear_regression_da.predict_dc()
             Relid,graph_data,ucl,lcl=uc1_scikit_linear_regression_da.graph_data()
             Last_Pred,lastP_Data,Actual,Accuracy=uc1_scikit_linear_regression_da.last_prediction()
        elif(Module_in=='Defect Defferal Rate'):
             module='Defect Defferal Rate'
             predicted_data=uc1_scikit_linear_regression_ddr.predict_dc()
             Relid,graph_data,ucl,lcl=uc1_scikit_linear_regression_ddr.graph_data()
             Last_Pred,lastP_Data,Actual,Accuracy=uc1_scikit_linear_regression_ddr.last_prediction()
        elif (Module_in=='All Defect'):
             module='Defect Count'
            
             predicted_data=uc1_scikit_linear_regression_alld.predict_dc()
             Relid,graph_data,ucl,lcl=uc1_scikit_linear_regression_alld.graph_data()
             Last_Pred,lastP_Data,Actual,Accuracy=uc1_scikit_linear_regression_alld.last_prediction()
        else :
            module='Functional Defect'
            print Module_in
            print '123'
            predicted_data=uc1_scikit_linear_regression_fund.predict_dc()
            Relid,graph_data,ucl,lcl=uc1_scikit_linear_regression_fund.graph_data()
            Last_Pred,lastP_Data,Actual,Accuracy=uc1_scikit_linear_regression_fund.last_prediction()
            


    elif(Algorithm_in == '2') :
        if(Module_in =='Defect Density'):
         print ("no")
         module='Defect Density'
         predicted_data=uc1c_scikit_svr_linear_telephonica_dd.predict_dc()
         Relid,graph_data,ucl,lcl=uc1c_scikit_svr_linear_telephonica_dd.graph_data()
         Last_Pred,lastP_Data,Actual,Accuracy=uc1c_scikit_svr_linear_telephonica_dd.last_prediction()
        elif(Module_in=='Defect Acceptance Rate') :
             print ("no12")
             module='Defect acceptance'
             predicted_data=uc1c_scikit_svr_linear_telephonica_da.predict_dc()
             Relid,graph_data,ucl,lcl=uc1c_scikit_svr_linear_telephonica_da.graph_data()
             Last_Pred,lastP_Data,Actual,Accuracy=uc1c_scikit_svr_linear_telephonica_da.last_prediction()
        elif(Module_in=='Defect Defferal Rate'):
             module='Defect Defferal Rate'
             predicted_data=uc1c_scikit_svr_linear_telephonica_ddr.predict_dc()
             Relid,graph_data,ucl,lcl=uc1c_scikit_svr_linear_telephonica_ddr.graph_data()
             Last_Pred,lastP_Data,Actual,Accuracy=uc1c_scikit_svr_linear_telephonica_ddr.last_prediction()
        elif(Module_in=='All Defect'):
             module='Defect Count'
             predicted_data=uc1c_scikit_svr_linear_telephonica_alld.predict_dc()
             Relid,graph_data,ucl,lcl=uc1c_scikit_svr_linear_telephonica_alld.graph_data()
             Last_Pred,lastP_Data,Actual,Accuracy=uc1c_scikit_svr_linear_telephonica_alld.last_prediction()
        else :
            module='Functional Defect'
            print '23'
            predicted_data=uc1c_scikit_svr_linear_telephonica_fund.predict_dc()
            Relid,graph_data,ucl,lcl=uc1c_scikit_svr_linear_telephonica_fund.graph_data()
            Last_Pred,lastP_Data,Actual,Accuracy=uc1c_scikit_svr_linear_telephonica_fund.last_prediction()
    elif(Algorithm_in == '3'):
        if(Module_in =='Defect Density'):
         print ("no")
         module='Defect Density'
         predicted_data=uc1c_scikit_svr_rbf_telephonica_dd.predict_dc()
         Relid,graph_data,ucl,lcl=uc1c_scikit_svr_rbf_telephonica_dd.graph_data()
         Last_Pred,lastP_Data,Actual,Accuracy=uc1c_scikit_svr_rbf_telephonica_dd.last_prediction()
        elif(Module_in=='Defect Acceptance Rate') :
             print ("no12")
             module='Defect acceptance'
             predicted_data=uc1c_scikit_svr_rbf_telephonica_da.predict_dc()
             Relid,graph_data,ucl,lcl=uc1c_scikit_svr_rbf_telephonica_da.graph_data()
             Last_Pred,lastP_Data,Actual,Accuracy=uc1c_scikit_svr_rbf_telephonica_da.last_prediction()
        elif(Module_in=='Defect Defferal Rate'):
             module='Defect Defferal Rate'
             predicted_data=uc1c_scikit_svr_rbf_telephonica_ddr.predict_dc()
             Relid,graph_data,ucl,lcl=uc1c_scikit_svr_rbf_telephonica_ddr.graph_data()
             Last_Pred,lastP_Data,Actual,Accuracy=uc1c_scikit_svr_rbf_telephonica_ddr.last_prediction()
        elif(Module_in=='All Defect'):
             module='Defect Count'
             predicted_data=uc1c_scikit_svr_rbf_telephonica_alld.predict_dc()
             Relid,graph_data,ucl,lcl=uc1c_scikit_svr_rbf_telephonica_alld.graph_data()
             Last_Pred,lastP_Data,Actual,Accuracy=uc1c_scikit_svr_rbf_telephonica_alld.last_prediction()
        else :
            module='Functional Defect'
            print '3'
            predicted_data=uc1c_scikit_svr_rbf_telephonica_fund.predict_dc()
            Relid,graph_data,ucl,lcl=uc1c_scikit_svr_rbf_telephonica_fund.graph_data()
            Last_Pred,lastP_Data,Actual,Accuracy=uc1c_scikit_svr_rbf_telephonica_fund.last_prediction()



    rel_id=len(Relid)
    uclall=ucl[0]
    lclall=lcl[0]
    print Relid,graph_data,ucl,lcl
    for n,i in enumerate (ucl):
      if i==(uclall):
         ucl[n]=ucl_in
    for n,i in enumerate (lcl):
      if i==(lclall) :
         lcl[n]=lcl_in
    rel_id=Relid[rel_id-1]
    Relid_graph=[]
    graph_data_graph=[]
    ucl_graph=[]
    lcl_graph=[]
    accuracy=[]
    predicted_data_graph=[]
    length=len(Relid)
    last_predict=[]
    if(length>100):
        if(length>150):
            i=151
        else:
            i=101
    else:
        i=0
    j=0
    k=0
    #last=['4','5','3','2','4']
    for s in Relid:
        if(j>=i):
            Relid_graph.append(str(s))
        j=j+1
    j=0
    print Relid_graph
    for s in graph_data:
        if(j>=i):
            graph_data_graph.append(str(s))
        if(j<(length-(len(Last_Pred)+1)) and j>=i):
            last_predict.append(str(s))
        elif(j>=(length-len(Last_Pred))):
            last_predict.append(str(Last_Pred[k]))
            k=k+1
        j=j+1
    j=0
    for s in ucl:
        if(j>=i):
            ucl_graph.append(str(s))
        j=j+1
    j=0
    for s in lcl:
        if(j>=i):
            lcl_graph.append(str(s))
        j=j+1
    last_predict.append(str(predicted_data[0]))
    print last_predict
    for last ,Actual,Relid,Acc in lastP_Data:
        a=100-abs(Relid-Actual)/Actual*100
        accuracy.append(a)
    print "#############"    
    print accuracy   
    context={
        "graph_data": graph_data_graph,
        "predicted_data": predicted_data[0],
        "predicted_label":rel_id,
        "labels" : Relid_graph,
        "ucl" : ucl_graph,
        "lcl" : lcl_graph,
        "Algorithm_in":Algorithm_in,
        "Prediction_in":Module_in,
        "Trend_in":Trend_in,
        "last_prediction": last_predict,
        "lastP_Data":lastP_Data,
        "module":module,
        "ucl_in":ucl_in,
        "Actual":Actual,
        "Accuracy":Accuracy,


        }
    
    return render(request,'usecase1/Usecase1_dc_result.html', context)
    


def update_predictioncount(request):
    
         
    value = request.POST.get('predictiondata')
    print(type(value))
    value1=[]
    value1=value
    print(type(value1))
    save1.save(str(value), Module_in)
    return render(request,'usecase1/matrics.html')



