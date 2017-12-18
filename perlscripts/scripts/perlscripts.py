# -*- coding: cp1252 -*-
import logging
import ntpath
import glob
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from pprint import pprint
import os, sys
import numpy
from pandas import DataFrame
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from pprint import pprint
from collections import defaultdict
import json
import sys
CAL = 'CAL'
EMAIL = 'EMAIL'
FILE= 'FILE'
NEWLINE = '\n'
path='/home/aspire/Juniper_files/Juniper_UC1A/Training/'
SOURCES = [
    (path+'p1.pm', EMAIL),
    (path+'p2.pm', EMAIL),
    (path+'p4.pm', FILE),
    (path+'p5.pm', FILE),
    (path+'p7.pm', CAL),
    (path+'p8.pm', CAL),
    (path+'p9.pm', CAL)
]
def read_files(path):
        data=[]=[]
        file = open(path, "r")
        documents=""
        documents = file.readlines()
        for line in documents:
            data.append(line.replace('#',' '))
        doc=[]
        for i in range(len(data)):
            doc.append(data[i].rstrip(';'))
        doc1=[]
        for line in doc:
            doc1.append(line.replace('\\n',' '))
        doc2=[]
        for line in doc1:
            doc2.append(line.replace('"',' '))
        doc4=[]
        for line in doc2:
            doc4.append(line.replace(':',' '))
        doc5=[]
        for line in doc4:
            doc5.append(line.replace(',',''))
        doc6=[]
        for line in doc5:
            doc6.append(line.replace('-',' '))
        doc7=[]
        for line in doc6:
            doc7.append(line.replace('=',''))
        doc8=[]
        for line in doc7:
            doc8.append(line.replace('>',''))
        doc9=[]
        for line in doc8:
            doc9.append(line.replace('(',' '))
        doc10=[]
        for line in doc9:
            doc10.append(line.replace(')',' '))
        doc11=[]
        for line in doc10:
            doc11.append(line.replace('[',' '))
        doc12=[]
        for line in doc11:
            doc12.append(line.replace(']',' '))
        doc13=[]
        for line in doc12:
            doc13.append(line.replace('{',' '))
        doc14=[]
        for line in doc13:
            doc14.append(line.replace('}',' '))                
        file.close()
        content = NEWLINE.join(doc14)
        yield path, content
def build_data_frame(path, classification):
        rows = []
        index = []
        for file_name, text in read_files(path):
                rows.append({'text': text, 'class': classification})
                index.append(file_name)
        data_frame = DataFrame(rows, index=index)
        return data_frame

def pred():
        data1 = DataFrame({'text': [], 'class': []})
        for path, classification in SOURCES:
                data1 = data1.append(build_data_frame(path, classification))
        data1 = data1.reindex(numpy.random.permutation(data1.index))
        count_vectorizer = CountVectorizer(decode_error = u'ignore')
        counts = count_vectorizer.fit_transform(data1['text'].values)
        classifier = MultinomialNB()
        targets = data1['class'].values
        classifier.fit(counts, targets)
        path = "/home/aspire/Juniper_files/Juniper_UC1A/Test_Data"
        dirs = os.listdir( path )
        result=[]
        files1=[]
        s=[]
        pro=""
        for filename in glob.glob(os.path.join(path, '*.pm')):
                f=open(filename,"r")
                test_data=[]
                lines=""
                lines=f.read()
                test_data=[lines]
                example_counts = count_vectorizer.transform(test_data)
                predictions = classifier.predict(example_counts)
                filesnames=str(ntpath.basename(filename))
                result.append((predictions,filesnames))
        return result
print(pred())
