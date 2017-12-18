import json
import sys
import math
import numpy as numpy
import mysql.connector
import pymysql
from pandas import DataFrame

def defectdbpg(problemarea,defecttitle,defectdescription,priority,steps,defecttype):
   
   cnx = pymysql.connect(host='10.248.3.91', port=3306, user='cresta', password='cresta', db='Aspire')


   query = """INSERT INTO Aspire.DefectDBpg(Problem_area,Defect_Title,Defect_Desciption,Defect_Type,Priority,Steps) VALUES (%s,%s,%s,%s,%s,%s)"""
   values=(str(problemarea),str(defecttitle),str(defectdescription),str(defecttype),str(priority),str(steps))
   print values,str(priority)
   print query,values
   try:
      cursor = cnx.cursor()
      cursor.execute(query,values)
      cnx.commit()
      #P=cursor.execute("SELECT * FROM Aspire.DefectDBpg")
      #data = DataFrame(cursor.fetchall(), columns=cols)
      #data =cursor.fetchall()
   finally:
      cnx.close()
    

