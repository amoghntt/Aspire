import json
import sys
import math
import numpy as numpy
import mysql.connector    
from pandas import DataFrame

def adaptive():
   cnx = mysql.connector.connect(user='cresta', password='cresta',host='10.248.3.91',database='cresta_uat')
   cols=['rel_id','defect_density','defect_rejection','defect_leakage','test_case_count','application_complexity','domain_knowledge','technical_skills','requirement_query_count','code_review_comments','design_review_comments','No_of_Resources','Budget_in_Use','Number_of_days_Completion','Cost_of_resource','Efficiency','Project_Status','Availability_Of_Budget']
   strColumns = ','.join(cols)
   query = "select " + strColumns + " from test_data "
   try:
      cursor = cnx.cursor()
      cursor.execute(query)
      #data = DataFrame(cursor.fetchall(), columns=cols)
      data =cursor.fetchall()
   finally:
      cnx.close()
   print data   
   return data
adaptive()
