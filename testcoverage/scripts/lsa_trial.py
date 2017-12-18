from __future__ import print_function
from tabulate import tabulate
import sklearn
import readrequirement
import testcaseread
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import Normalizer
from sklearn import metrics
from sklearn.cluster import KMeans, MiniBatchKMeans
import pandas as pd
import warnings
import numpy as np
import json
import operator

warnings.filterwarnings("ignore")
example =[]

def coverage():
 readrequirement.readRequirementFromTextFile()
 testCaseId = []

 testCaseId = testcaseread.readTestCasesFromExcelFile()
 print (testCaseId)
 with open("/home/aspire/client/juniper/juniper/media/textrequirementprocessed.txt", 'r') as f:
    #print (f.readlines()) 
    example1 = f.readlines()

 for i in range(len(example1)):
    example.append(example1[i].strip('\n'))

 vectorizer = CountVectorizer(min_df = 1, stop_words = 'english',strip_accents = 'ascii')
 dtm = vectorizer.fit_transform(example)
 #pd.DataFrame(dtm.toarray(),index=example,columns=vectorizer.get_feature_names()).head(10)
 
 vectorizer.get_feature_names()

 lsa = TruncatedSVD(100)
 dtm_lsa = lsa.fit_transform(dtm)
 dtm_lsa = Normalizer(copy=False).fit_transform(dtm_lsa)
 # Compute document similarity using LSA components
 similarity = np.asarray(np.asmatrix(dtm_lsa) * np.asmatrix(dtm_lsa).T)
 #if similarity > 0.7:
 #print similarity
 df = pd.DataFrame(similarity).head(1)

 resultlistdouble = []
 for i in range(0,1):
    for j in range(0,len(example)):
        opt=df.get_value(i,j)*100
        res=round(opt,2)
        resultlistdouble.append(abs(res))
        
 resultlistdouble.pop(0)


 thefile = open('/home/aspire/client/juniper/juniper/media/textrequirementprocessed.txt', 'w')
 thefile.close()

 #thefile = open('C:/Users/109100/Desktop/juniper/testcoverage/scripts/textrequirement.txt', 'w')
 #thefile.close()
 dict_1 = {}
 keys=[]
 value=[]
 #for i in range(60):
 dict_1 = create_dict(testCaseId,(resultlistdouble*100))
 sorted_x = sorted(dict_1.items(), key=operator.itemgetter(0))
 #print (testCaseId[1])
 print (sorted_x)
 #print (dict_1)
 for key,val in dict_1.iteritems():
  #print (type(key))   
  #keys=keys.append(str(key))
  #value=value.append(val)
  #print (key,val)
  #print (json.dumps(dict_1))
  #print (keys)
  return sorted_x 
def create_dict(keys, values):
    return dict(zip(keys, (values*100) + [None] * (len(keys) - len(values))))
#coverage() 


