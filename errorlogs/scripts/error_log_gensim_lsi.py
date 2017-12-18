import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora
import gensim as gensim
from collections import defaultdict
from pprint import pprint
from gensim import corpora, models, similarities
import os
import numpy as np
import scipy as sc
Path="/home/aspire/Juniper_files/Juniper_UC3/"
Training_data=Path+"Master_log.txt"
Test_data=Path+"Test_Log_Def.txt"
def avg_feature_vector(words, model, num_features):
        #function to average all words vectors in a given paragraph
        featureVec = np.zeros((num_features,), dtype="float32")
        nwords = 0

        #list containing names of words in the vocabulary
        #index2word_set = set(model.index2word) this is moved as input param for performance reasons
        index2word_set = set(model.wv.index2word)
        for word in words:
            if word in index2word_set:
                nwords = nwords+1
                featureVec = np.add(featureVec, model[word])

        if(nwords>0):
            featureVec = np.divide(featureVec, nwords)
        return featureVec
def predict_error_log():
        d=[]
        file = open(Training_data, "r")
        lines = file.readlines()
        for line in lines:
                d.append(line.replace('\n',''))
        data=[]
        for i in range(len(lines)):
                #grades.append(lines[i].rstrip('\n').split(','))
                data.append(lines[i].rstrip('\n'))
        stoplist = set('for a of the and to in'.split())
        #stoplist = set('english')
        texts = [[word for word in document.lower().split() if word not in stoplist]
                 for document in data]
        frequency = defaultdict(int)
        for text in texts:
                for token in text:
                        frequency[token] +=1
        texts=[[token for token in text if frequency[token]>0]for text in texts]
        dictionary=corpora.Dictionary(texts)
        corpus=[dictionary.doc2bow(text) for text in texts]
        tfidf = models.TfidfModel(corpus)
        corpus_tfidf = tfidf[corpus]
        lsi = models.LsiModel(corpus_tfidf, id2word=dictionary)
        f=open(Test_data,"r")
        data=""
        data = f.readlines()
        doc=""
        doc=repr(data)
        vec_bow = dictionary.doc2bow(doc.lower().split())
        vec_lsi = lsi[vec_bow]
        index = similarities.MatrixSimilarity(lsi[corpus])
        sims = index[vec_lsi]
        data=["LogDef 0","LogDef 1","LogDef 2","LogDef 3","LogScript 0","LogScript 1","LogScript 2","LogScript 3","LogEnv 0","LogEnv 1","LogEnv 2","LogEnv 3",]
        i=0
        log_similarities=[]
        for text in list(enumerate(sims)):
                #print(text)
                log_similarities.append((data[i],text))
                i=i+1
        return list(enumerate(sims))
#pprint(predict_error_log())

