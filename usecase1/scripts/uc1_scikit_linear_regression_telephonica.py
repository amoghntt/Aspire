import json
import sys
import math

import mysql.connector
import numpy
from pandas import DataFrame
from sklearn.linear_model import LinearRegression

def predict_dc(Prediction_in):

 Predictionin=int(Prediction_in)
 if (Predictionin==1):
  cnx = mysql.connector.connect(user='cresta', password='cresta',
                              host='10.248.3.91',
                           database='cresta')
  cols = ['defect_count','KLOC', 'test_case_count', 'application_complexity', 'domain_knowledge', 'technical_skills', 'requirements_query_count', 'code_review_comments', 'design_review_comments','effort_to_fix_defect', 'cost_to_fix_defect','impact_of_defect_fix', 'feasibility_within_milestone', 'availability_of_budget', 'complexity_of_defect_fix', 'defect_deferral_rate', 'bg_severity', 'bg_priority','defect_count/KLOC']
  strColumns = ','.join(cols)
  query = "select " + strColumns + " from UseCaseData where pred_code=%s and user_id=%s"
  params = (sys.argv[1], sys.argv[2])
  try:
   cursor = cnx.cursor()
   cursor.execute(query, params)
   data = DataFrame(cursor.fetchall(), columns=cols)
   input_data = data[cols[:-1]][-1:]
   data = data[:-1]
  finally:
    cnx.close()

  X = data[cols[:-1]]
  data = data.rename(columns={'defect_count/KLOC': Predictionin})
  y = data.Predictionin
  lm = LinearRegression()
  lm.fit(X, y)

  result = lm.predict(input_data)
  return result


def graph_data():
   cnx = mysql.connector.connect(user='cresta', password='cresta',host='10.248.3.91',database='cresta')
   cols = ['ID']
   strColumns = ','.join(cols)
   query = "select " + strColumns + " from usecase1CTelephonica"
   data=[]
   data1=[]
   data2=[]
   data3=[]
   data_d=[]
   data1_d=[]
   data2_d=[]
   data3_d=[]
   ucl=[]
   lcl=[]
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
      data3.append('20192')
      Relid = data3[:]
      cols = ['defect_count']
      strColumns = ','.join(cols)
      query = "select " + strColumns + " from usecase1CTelephonica"
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
      graph_data = data3_d[:]
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
   ucl=average+three_sigma
   lcl=average-three_sigma
   print(ucl)
   ucl=(ucl,0)
   if lcl<0:
      lcl=0
   return ucl,lcl