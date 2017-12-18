import json
import sys
import math
import numpy as numpy
import mysql.connector    
from pandas import DataFrame
from sklearn.linear_model import LinearRegression


def predict_dc():
 #Predictionin=Prediction_in

 #if (Predictionin == 1):
   cnx = mysql.connector.connect(user='cresta', password='cresta', host='10.248.3.91', database='cresta_uat')
   cols = ['KLOC', 'test_case_count', 'application_complexity', 'domain_knowledge', 'technical_skills', 'requirements_query_count', 'code_review_comments', 'design_review_comments','defect_count/KLOC']
   strColumns = ','.join(cols)
   query = "select " + strColumns + " from usecase1 "
   print(1)
   try:
    cursor = cnx.cursor()
    cursor.execute(query)
    data = DataFrame(cursor.fetchall(), columns=cols)
    input_data = data[cols[:-1]][-1:]
    data = data[:-1]
   finally:
      cnx.close()

   X = data[cols[:-1]]
   data = data.rename(columns={'defect_count/KLOC': 'defect_density'})
   y = data.defect_density
   lm = LinearRegression()
   lm.fit(X, y)

   result = lm.predict(input_data)

   return result



   '''#elif(Predictionin==2):


   cnx = mysql.connector.connect(user='cresta', password='cresta',  host='10.248.3.91', database='cresta')
   cols = ['KLOC', 'test_case_count', 'application_complexity', 'domain_knowledge', 'technical_skills', 'requirements_query_count', 'code_review_comments', 'design_review_comments', 'acceptance']
   strColumns = ','.join(cols)
   query = "select " + strColumns + " from UseCaseData "
   print(2)
   try:
    cursor = cnx.cursor()
    cursor.execute(query)
    data = DataFrame(cursor.fetchall(), columns=cols)
    input_data = data[cols[:-1]][-1:]
    data = data[:-1]
   finally:
     cnx.close()

   X = data[cols[:-1]]
   y = data.acceptance
   lm = LinearRegression()
   lm.fit(X, y)

   result = lm.predict(input_data)


 elif(Predictionin==3):


   cnx = mysql.connector.connect(user='cresta', password='cresta',  host='10.248.3.91', database='cresta')
   cols = ['KLOC', 'test_case_count', 'application_complexity', 'domain_knowledge', 'technical_skills', 'requirements_query_count', 'code_review_comments', 'design_review_comments', 'defect_count']
   strColumns = ','.join(cols)
   query = "select " + strColumns + " from usecase1C "
   print (21)
   try:
    cursor = cnx.cursor()
    cursor.execute(query)
    data = DataFrame(cursor.fetchall(), columns=cols)
    input_data = data[cols[:-1]][-1:]
    data = data[:-1]
   finally:
    cnx.close()

   X = data[cols[:-1]]
   y = data.defect_count
   lm = LinearRegression()
   lm.fit(X, y)

   result = lm.predict(input_data)


 else:


   cnx = mysql.connector.connect(user='cresta', password='cresta', host='10.248.3.91', database='cresta')
   cols = ['KLOC', 'test_case_count', 'application_complexity', 'domain_knowledge', 'technical_skills', 'requirements_query_count', 'code_review_comments', 'design_review_comments', 'defect_count']
   strColumns = ','.join(cols)
   query = "select " + strColumns + " from usecase1D "
   print(23)
   try:
    cursor = cnx.cursor()
    cursor.execute(query)
    data = DataFrame(cursor.fetchall(), columns=cols)
    input_data = data[cols[:-1]][-1:]
    data = data[:-1]
   finally:
      cnx.close()

   X = data[cols[:-1]]
   y = data.defect_count
   lm = LinearRegression()
   lm.fit(X, y)

   result = lm.predict(input_data)
'''



def graph_data(Prediction_in):
   Predictionin=Prediction_in


   if (Predictionin == 1):
    cnx = mysql.connector.connect(user='cresta', password='cresta', host='10.248.3.91', database='cresta')
    cols = ['ID']
    strColumns = ','.join(cols)
    query = "select " + strColumns + " from usecase1"
    data = []
    data1 = []
    data2 = []
    data3 = []
    data_d = []
    data1_d = []
    data2_d = []
    data3_d = []
    ucl = []
    lcl = []
    try:
      cursor = cnx.cursor()
      cursor.execute(query)
      # data = DataFrame(cursor.fetchall(), columns=cols)
      data = cursor.fetchall()
      for x in data:
         x = str(x)
         data1.append(x.replace(',', ''))
      for x in data1:
         x = str(x)
         data2.append(x.replace('(', ''))
      for x in data2:
         x = str(x)
         data3.append(x.replace(')', ''))
      data3.append('20192')
      Relid = data3[:]
      cols = ['defect_count']
      strColumns = ','.join(cols)
      query = "select " + strColumns + " from usecase1CTelephonica"
      cursor = cnx.cursor()
      cursor.execute(query)
      data_d = cursor.fetchall()
      ucl1, lcl1 = predict_ucllcl(data_d)
      for y in data_d:
         y = str(y)
         data1_d.append(y.replace(',', ''))
      for y in data1_d:
         y = str(y)
         data2_d.append(y.replace('(', ''))
      for y in data2_d:
         y = str(y)
         data3_d.append(y.replace(')', ''))
      graph_data = data3_d[:]
    finally:
      cnx.close()
    print(ucl1, lcl1)
    predicted_result = predict_dc(Predictionin)
    predicted_result = str(Predictionin)
    pred = ""
    pred1 = ""
    pred = predicted_result.replace('[', '')
    pred1 = pred.replace(']', '')
    graph_data.append(pred1)
    for x in graph_data:
      ucl.append(ucl1)
      lcl.append(lcl1)
   return Relid, graph_data, ucl, lcl
'''   elif (Predictionin == 2):
      cnx = mysql.connector.connect(user='cresta', password='cresta', host='10.248.3.91', database='cresta')
      cols = ['ID']
      strColumns = ','.join(cols)
      query = "select " + strColumns + " from UseCaseData"
      data = []
      data1 = []
      data2 = []
      data3 = []
      data_d = []
      data1_d = []
      data2_d = []
      data3_d = []
      ucl = []
      lcl = []
      try:
       cursor = cnx.cursor()
       cursor.execute(query)
       # data = DataFrame(cursor.fetchall(), columns=cols)
       data = cursor.fetchall()
       for x in data:
         x = str(x)
         data1.append(x.replace(',', ''))
       for x in data1:
         x = str(x)
         data2.append(x.replace('(', ''))
       for x in data2:
         x = str(x)
         data3.append(x.replace(')', ''))
       data3.append('20192')
       Relid = data3[:]
       cols = ['defect_count']
       strColumns = ','.join(cols)
       query = "select " + strColumns + " from usecase1CTelephonica"
       cursor = cnx.cursor()
       cursor.execute(query)
       data_d = cursor.fetchall()
       ucl1, lcl1 = predict_ucllcl(data_d)
       for y in data_d:
         y = str(y)
         data1_d.append(y.replace(',', ''))
       for y in data1_d:
         y = str(y)
         data2_d.append(y.replace('(', ''))
       for y in data2_d:
         y = str(y)
         data3_d.append(y.replace(')', ''))
       graph_data = data3_d[:]
      finally:
        cnx.close()
      print(ucl1, lcl1)
      predicted_result = predict_dc(Predictionin)
      predicted_result = str(Predictionin)
      pred = ""
      pred1 = ""
      pred = predicted_result.replace('[', '')
      pred1 = pred.replace(']', '')
      graph_data.append(pred1)
      for x in graph_data:
       ucl.append(ucl1)
       lcl.append(lcl1)

   elif (Predictionin == 3):
     cnx = mysql.connector.connect(user='cresta', password='cresta', host='10.248.3.91', database='cresta')
     cols = ['ID']
     strColumns = ','.join(cols)
     query = "select " + strColumns + " from usecase1C"
     data = []
     data1 = []
     data2 = []
     data3 = []
     data_d = []
     data1_d = []
     data2_d = []
     data3_d = []
     ucl = []
     lcl = []
     try:
      cursor = cnx.cursor()
      cursor.execute(query)
      # data = DataFrame(cursor.fetchall(), columns=cols)
      data = cursor.fetchall()
      for x in data:
         x = str(x)
         data1.append(x.replace(',', ''))
      for x in data1:
         x = str(x)
         data2.append(x.replace('(', ''))
      for x in data2:
         x = str(x)
         data3.append(x.replace(')', ''))
      data3.append('20192')
      Relid = data3[:]
      cols = ['defect_count']
      strColumns = ','.join(cols)
      query = "select " + strColumns + " from usecase1CTelephonica"
      cursor = cnx.cursor()
      cursor.execute(query)
      data_d = cursor.fetchall()
      ucl1, lcl1 = predict_ucllcl(data_d)
      for y in data_d:
         y = str(y)
         data1_d.append(y.replace(',', ''))
      for y in data1_d:
         y = str(y)
         data2_d.append(y.replace('(', ''))
      for y in data2_d:
         y = str(y)
         data3_d.append(y.replace(')', ''))
      graph_data = data3_d[:]
     finally:
      cnx.close()
     print(ucl1, lcl1)
     predicted_result = predict_dc(Predictionin)
     predicted_result = str(Predictionin)
     pred = ""
     pred1 = ""
     pred = predicted_result.replace('[', '')
     pred1 = pred.replace(']', '')
     graph_data.append(pred1)
     for x in graph_data:
      ucl.append(ucl1)
      lcl.append(lcl1)

   else :
     cnx = mysql.connector.connect(user='cresta', password='cresta', host='10.248.3.91', database='cresta')
     cols = ['ID']
     strColumns = ','.join(cols)
     query = "select " + strColumns + " from usecase1D"
     data = []
     data1 = []
     data2 = []
     data3 = []
     data_d = []
     data1_d = []
     data2_d = []
     data3_d = []
     ucl = []
     lcl = []
     try:
      cursor = cnx.cursor()
      cursor.execute(query)
      # data = DataFrame(cursor.fetchall(), columns=cols)
      data = cursor.fetchall()
      for x in data:
         x = str(x)
         data1.append(x.replace(',', ''))
      for x in data1:
         x = str(x)
         data2.append(x.replace('(', ''))
      for x in data2:
         x = str(x)
         data3.append(x.replace(')', ''))
      data3.append('20192')
      Relid = data3[:]
      cols = ['defect_count']
      strColumns = ','.join(cols)
      query = "select " + strColumns + " from usecase1CTelephonica"
      cursor = cnx.cursor()
      cursor.execute(query)
      data_d = cursor.fetchall()
      ucl1, lcl1 = predict_ucllcl(data_d)
      for y in data_d:
         y = str(y)
         data1_d.append(y.replace(',', ''))
      for y in data1_d:
         y = str(y)
         data2_d.append(y.replace('(', ''))
      for y in data2_d:
         y = str(y)
         data3_d.append(y.replace(')', ''))
      graph_data = data3_d[:]
     finally:
      cnx.close()
     print(ucl1, lcl1)
     predicted_result = predict_dc(Predictionin)
     predicted_result = str(Predictionin)
     pred = ""
     pred1 = ""
     pred = predicted_result.replace('[', '')
     pred1 = pred.replace(']', '')
     graph_data.append(pred1)
     for x in graph_data:
      ucl.append(ucl1)
      lcl.append(lcl1)
'''



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
   ucl=average+three_sigma
   lcl=average-three_sigma
   print(ucl)
   ucl= math.floor(ucl)
   if lcl<0:
      lcl=0
   return ucl,lcl



