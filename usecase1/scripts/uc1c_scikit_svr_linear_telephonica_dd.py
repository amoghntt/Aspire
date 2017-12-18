# -*- coding: cp1252 -*-
import json
import sys
import math
import mysql.connector
from pandas import DataFrame
from sklearn.svm import SVR
import pprint as pprint
from numpy import mean
import numpy as numpy


def predict_dc():
    cnx = mysql.connector.connect(user='cresta', password='cresta',host='10.248.3.91',database='cresta_uat')
    cols = ['KLOC', 'test_case_count', 'application_complexity', 'domain_knowledge', 'technical_skills', 'requirements_query_count', 'code_review_comments', 'design_review_comments', 'defect_count','DEFECT_COUNT/KLOC']
    strColumns = ','.join(cols)
    #query = "select " + strColumns + " from usecase1CTelephonica"
    query = "select " + strColumns + " from uc_dd_aspire"
    try:
       cursor = cnx.cursor()
       cursor.execute(query)
       data = DataFrame(cursor.fetchall(), columns=cols)
       input_data = data[cols[:-1]][-1:]
       data = data[:-1]
       
    finally:
       cnx.close()
    X = data[cols[:-1]]
    data = data.rename(columns={'DEFECT_COUNT/KLOC': 'defect_density'})
    y = data.defect_density
    print y
    svr = SVR(kernel='linear', C=1e3)
    svr.fit(X, y)
    result = svr.predict(input_data)
    return list(result)
def graph_data():
   cnx = mysql.connector.connect(user='cresta', password='cresta',host='10.248.3.91',database='cresta_uat')
   cols = ['ID']
   strColumns = ','.join(cols)
   #query = "select " + strColumns + " from usecase1CTelephonica"
   query = "select " + strColumns + " from uc_dd_aspire"
   data=[]
   data1=[]
   data2=[]
   data3=[]
   data_d=[]
   data1_d=[]
   data2_d=[]
   data3_d=[]
   data4_d=[]
   data5_d=[]
   ucl=[]
   lcl=[]
   rel=[]
   try:
      cursor = cnx.cursor()
      cursor.execute(query)
      #data = DataFrame(cursor.fetchall(), columns=cols)
      data =cursor.fetchall()
      for x in data:
         x=str(x)
         data1.append(x.replace(',',''))
      for x in data1:
         x=str(x)
         data2.append(x.replace('(',''))
      for x in data2:
         x=str(x)
         data3.append(x.replace(')',''))
      length=len(data2)
      predic_rel=data2[length-1]
      rel.append(predic_rel.replace(')',''))
      print (type(rel))
      rel1=str(rel[0])

      #rel=int(rel)+1
      red_id=int(rel1)+1
      data3.append(red_id)
      Relid = data3[:]
      cols = ['DEFECT_COUNT/KLOC']
      strColumns = ','.join(cols)
      #query = "select " + strColumns + " from usecase1CTelephonica"
      query = "select " + strColumns + " from uc_dd_aspire"
      cursor = cnx.cursor()
      cursor.execute(query)
      data_d =cursor.fetchall()
      ucl1,lcl1=predict_ucllcl(data_d)
      for y in data_d:
         y=str(y)
         data1_d.append(y.replace(',',''))
      for y in data1_d:
         y=str(y)
         data2_d.append(y.replace('(',''))
      for y in data2_d:
         y=str(y)
         data3_d.append(y.replace(')',''))
      for y in data3_d:
         y=str(y)
         data4_d.append(y.replace("Decimal'",''))
      for y in data4_d:
         y=str(y)
         data5_d.append(y.replace("'",''))
      graph_data = data5_d[:]
   finally:
      cnx.close()
   print(ucl1,lcl1)
   predicted_result=predict_dc()
   predicted_result=str(predicted_result)
   pred=""
   pred1=""
   pred=predicted_result.replace('[','')
   pred1=pred.replace(']','')
   graph_data.append(pred1)
   for x in graph_data:
      ucl.append(ucl1)
      lcl.append(lcl1)
   return Relid,graph_data,ucl,lcl
def predict_ucllcl(mydata):
   data_set=mydata
   avg=0
   num=0
   i=len(data_set)
   #average = reduce(lambda x, y: x + y, data_set) / len(data_set)
   average=numpy.mean(data_set, axis=0)
   #average=avg/num
   s = [x-average for x in data_set]
   square = [x*x for x in s]
   avg_new=0
   data=[]
   for x in square:
      avg_new=x+avg_new
   varience=avg_new/i
   #sigma=(varience)^(1/2)
   sigma=math.pow(varience, 0.5)
   three_sigma=3*sigma
   print(three_sigma)
   ucl=average+int(three_sigma)
   lcl=average-int(three_sigma)
   print(ucl)
   ucl=round(ucl,0)
   if lcl<0:
      lcl=0
   else:
      lcl=round(lcl)
   return ucl,lcl
def last_prediction():
   cnx = mysql.connector.connect(user='cresta', password='cresta',host='10.248.3.91',database='cresta_uat')
   cols=['Rel_Id','Predicted','Actual','Accuracy']
   strColumns = ','.join(cols)
   query = "select " + strColumns + " from uc_dd_last_prediction where Algo='SVRLINEAR'"
   try:
      cursor = cnx.cursor()
      cursor.execute(query)
      #data = DataFrame(cursor.fetchall(), columns=cols)
      data =cursor.fetchall()
   finally:
      cnx.close()
   print data
   Last_predictions=[]
   Rel_Id=[]
   Actual=[]
   Accuracy=[]
   for actual,relid,predicted,acc in data:
      Last_predictions.append(str(predicted))
      Rel_Id.append(str(relid))
      Actual.append(str(actual))
      Accuracy.append(str(acc))
   print data   
   print Last_predictions
   return Last_predictions,data,Actual,Accuracy
#a,b,c,d=graph_data()
#print predict_dc()
