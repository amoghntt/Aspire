import json
import sys
import math
import numpy as numpy
import mysql.connector    
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
from jubatus.common import Datum
from jubatus.regression.client import Regression
from jubatus.regression.types import *
import pprint
import argparse
import yaml

VERSION = (0, 0, 1, '')

def get_version():
  version_string = '%s.%s.%s' % VERSION[0:3]
  if len(VERSION[3]):
    version_string += '-' + VERSION[3]
  return version_string

def parse_options():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    '-v',
    '--version',
    action   = 'version',
    version  = '%(prog)s ' + get_version()
  )
  return parser.parse_args()


def juba_alld():
  client = Regression('10.248.3.91', 9199, '')
  cnx = mysql.connector.connect(user='cresta', password='cresta', host='10.248.3.91', database='cresta_uat')
  cols = ['ID','KLOC', 'test_case_count', 'application_complexity', 'domain_knowledge', 'technical_skills', 'requirements_query_count', 'code_review_comments', 'design_review_comments', 'defect_count']

  strColumns = ','.join(cols)
  query = "select " + strColumns + " from uc_alld_aspire"

  cursor = cnx.cursor()
  cursor.execute(query)
  d=[]
  data = cursor.fetchall()
  input_data=[]
  print(data[:][-1:])
  input_data = data[:][-1:]
  #print data
  data = data[:-1]
  data=data

  #print type(data)
  for row in data:
      kloc=row[1]
      #kloc=int(kloc)
      #print kloc
      d = Datum({
          'KLOC':float(row[1]),
          'test_case_count':int(row[2]),
          'application_complexity':int(row[3]),
          'domain_knowledge':int(row[4]),
          'technical_skills':int(row[5]),
          'requirements_query_count':int(row[6]),
          'code_review_comments':int(row[7]),
          'design_review_comments':int(row[8]),
          })
      train_data = [[float(row[9]), d]]
    # train
      client.train(train_data)
    #print ('train ... {}'.format(num))
    # anaylze
  for row in input_data:
      #print row
      d = Datum({
          'KLOC':int(row[1]),
          'test_case_count':int(row[2]),
          'application_complexity':int(row[3]),
          'domain_knowledge':int(row[4]),
          'technical_skills':int(row[5]),
          'requirements_query_count':int(row[6]),
          'code_review_comments':int(row[7]),
          'design_review_comments':int(row[8]),
          })
  analyze_data = [d]
  result = client.estimate(analyze_data)
  print ('prediction .... {}'.format(round(result[0], 1)))
  return format(round(result[0], 1))





def juba_da():
  client = Regression('10.248.3.91', 9199, '')
  cnx = mysql.connector.connect(user='cresta', password='cresta', host='10.248.3.91', database='cresta_uat')
  cols = ['ID','KLOC', 'test_case_count', 'application_complexity', 'domain_knowledge', 'technical_skills', 'requirements_query_count', 'code_review_comments', 'design_review_comments', 'acceptance']

  strColumns = ','.join(cols)
  query = "select " + strColumns + " from uc_da_aspire "

  cursor = cnx.cursor()
  cursor.execute(query)
  d=[]
  data = cursor.fetchall()
  input_data=[]
  print(data[:][-1:])
  input_data = data[:][-1:]
  #print data
  data = data[:-1]
  data=data

  #print type(data)
  for row in data:
      kloc=row[1]
      #kloc=int(kloc)
      #print kloc
      d = Datum({
          'KLOC':float(row[1]),
          'test_case_count':int(row[2]),
          'application_complexity':int(row[3]),
          'domain_knowledge':int(row[4]),
          'technical_skills':int(row[5]),
          'requirements_query_count':int(row[6]),
          'code_review_comments':int(row[7]),
          'design_review_comments':int(row[8]),
          })
      train_data = [[float(row[9]), d]]
    # train
      client.train(train_data)
    #print ('train ... {}'.format(num))
    # anaylze
  for row in input_data:
      #print row
      d = Datum({
          'KLOC':int(row[1]),
          'test_case_count':int(row[2]),
          'application_complexity':int(row[3]),
          'domain_knowledge':int(row[4]),
          'technical_skills':int(row[5]),
          'requirements_query_count':int(row[6]),
          'code_review_comments':int(row[7]),
          'design_review_comments':int(row[8]),
          })
  analyze_data = [d]
  result = client.estimate(analyze_data)
  print ('prediction .... {}'.format(round(result[0], 1)))
  return format(round(result[0], 1))






def juba_dd():
  client = Regression('10.248.3.91', 9199, '')
  cnx = mysql.connector.connect(user='cresta', password='cresta', host='10.248.3.91', database='cresta_uat')
  cols = ['ID','KLOC', 'test_case_count', 'application_complexity', 'domain_knowledge', 'technical_skills', 'requirements_query_count', 'code_review_comments', 'design_review_comments', 'defect_count','DEFECT_COUNT/KLOC']

  strColumns = ','.join(cols)
  query = "select " + strColumns + " from uc_dd_aspire"

  cursor = cnx.cursor()
  cursor.execute(query)
  d=[]
  data = cursor.fetchall()
  input_data=[]
  print(data[:][-1:])
  input_data = data[:][-1:]
  #print data
  data = data[:-1]
  data=data

  #print type(data)
  for row in data:
      kloc=row[1]
      #kloc=int(kloc)
      #print kloc
      d = Datum({
          'KLOC':float(row[1]),
          'test_case_count':int(row[2]),
          'application_complexity':int(row[3]),
          'domain_knowledge':int(row[4]),
          'technical_skills':int(row[5]),
          'requirements_query_count':int(row[6]),
          'code_review_comments':int(row[7]),
          'design_review_comments':int(row[8]),
          'defect_count':int(row[9]),
          })
      train_data = [[float(row[10]), d]]
    # train
      client.train(train_data)
    #print ('train ... {}'.format(num))
    # anaylze
  for row in input_data:
      #print row
      d = Datum({
          'KLOC':int(row[1]),
          'test_case_count':int(row[2]),
          'application_complexity':int(row[3]),
          'domain_knowledge':int(row[4]),
          'technical_skills':int(row[5]),
          'requirements_query_count':int(row[6]),
          'code_review_comments':int(row[7]),
          'design_review_comments':int(row[8]),
          'defect_count':int(row[9]),
          })
  analyze_data = [d]
  result = client.estimate(analyze_data)
  print ('prediction .... {}'.format(round(result[0], 1)))
  return format(round(result[0], 1))

def juba_ddr():
  client = Regression('10.248.3.91', 9199, '')
  cnx = mysql.connector.connect(user='cresta', password='cresta', host='10.248.3.91', database='cresta_uat')
  cols = ['ID','bg_severity', 'bg_priority', 'effort_to_fix_defect', 'impact_of_defect_fix', 'complexity_of_defect_fix', 'defect_deferral_rate']

  strColumns = ','.join(cols)
  query = "select " + strColumns + " from uc_ddr_aspire "

  cursor = cnx.cursor()
  cursor.execute(query)
  d=[]
  data = cursor.fetchall()
  input_data=[]
  print(data[:][-1:])
  input_data = data[:][-1:]
  #print data
  data = data[:-1]
  data=data

  #print type(data)
  for row in data:
      kloc=row[1]
      #kloc=int(kloc)
      #print kloc
      d = Datum({
          'bg_severity':float(row[1]),
          'bg_priority':int(row[2]),
          'effort_to_fix_defect':int(row[3]),
          'impact_of_defect_fix':int(row[4]),
          'complexity_of_defect_fix':int(row[5]),
          })
      train_data = [[float(row[6]), d]]
    # train
      client.train(train_data)
    #print ('train ... {}'.format(num))
    # anaylze
  for row in input_data:
      #print row
      d = Datum({
          'bg_severity':float(row[1]),
          'bg_priority':int(row[2]),
          'effort_to_fix_defect':int(row[3]),
          'impact_of_defect_fix':int(row[4]),
          'complexity_of_defect_fix':int(row[5]),
          })
  analyze_data = [d]
  result = client.estimate(analyze_data)
  print ('prediction .... {}'.format(round(result[0], 1)))
  return format(round(result[0], 1))

def juba_funnd():
  client = Regression('10.248.3.91', 9199, '')
  cnx = mysql.connector.connect(user='cresta', password='cresta', host='10.248.3.91', database='cresta_uat')
  cols = ['ID','KLOC', 'test_case_count', 'application_complexity', 'domain_knowledge', 'technical_skills', 'requirements_query_count', 'code_review_comments', 'design_review_comments', 'defect_count']

  strColumns = ','.join(cols)
  query = "select " + strColumns + " from uc_fund_aspire"

  cursor = cnx.cursor()
  cursor.execute(query)
  d=[]
  data = cursor.fetchall()
  input_data=[]
  print(data[:][-1:])
  input_data = data[:][-1:]
  #print data
  data = data[:-1]
  data=data

  #print type(data)
  for row in data:
      kloc=row[1]
      #kloc=int(kloc)
      #print kloc
      d = Datum({
          'KLOC':float(row[1]),
          'test_case_count':int(row[2]),
          'application_complexity':int(row[3]),
          'domain_knowledge':int(row[4]),
          'technical_skills':int(row[5]),
          'requirements_query_count':int(row[6]),
          'code_review_comments':int(row[7]),
          'design_review_comments':int(row[8]),
          })
      train_data = [[float(row[9]), d]]
    # train
      client.train(train_data)
    #print ('train ... {}'.format(num))
    # anaylze
  for row in input_data:
      #print row
      d = Datum({
          'KLOC':int(row[1]),
          'test_case_count':int(row[2]),
          'application_complexity':int(row[3]),
          'domain_knowledge':int(row[4]),
          'technical_skills':int(row[5]),
          'requirements_query_count':int(row[6]),
          'code_review_comments':int(row[7]),
          'design_review_comments':int(row[8]),
          })
  analyze_data = [d]
  result = client.estimate(analyze_data)
  print ('prediction .... {}'.format(round(result[0], 1)))
  return format(round(result[0], 1))


