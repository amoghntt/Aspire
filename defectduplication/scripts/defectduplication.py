import warnings
import testcaseread
warnings.filterwarnings("ignore")
import gensim
import scipy as sc
import numpy as np
import json
import nltk
import os
from django.conf import settings

#testcaseread.readTestCasesFromExcelFile()

def avg_feature_vector1(words, model, num_features):
        #function to average all words vectors in a given paragraph
        featureVec = np.zeros((num_features,), dtype="float32")
        nwords = 0

        #list containing names of words in the vocabulary
        index2word_set = set(model.index2word)
        for word in words:
            if word in index2word_set:
                nwords = nwords+1
                featureVec = np.add(featureVec, model[word])

        if(nwords>0):
            featureVec = np.divide(featureVec, nwords)
        return featureVec

def optimize( corpora ):
        corpora_lan=corpora
        testcaseread.readTestCasesFromExcelFile(corpora_lan)
        with open('/home/aspire/client/juniper/juniper/media/textrequirementprocessed.txt', 'r') as myfile:
        #with open(os.path.join(settings.PROJECT_ROOT, 'media/textrequirementprocessed.txt'), 'r') as myfile:
                content = myfile.readlines()
        content = [x.strip() for x in content]
        resultArray = np.zeros((len(content),len(content)))
        i = -1
        j = -1
        for sentence in content:
                i = i + 1
                j=-1
                for sentence1 in content:
                        j = j + 1
                        if (sentence is not sentence1):
                                with open('/home/aspire/client/juniper/juniper/media/result.txt', 'w') as myfile:
                                #with open(os.path.join(settings.PROJECT_ROOT, 'media/result.txt'),'w') as myfile:
                                        myfile.write(sentence + "\n")
                                        myfile.write(sentence1)
                                inputData1 = gensim.models.word2vec.LineSentence("/home/aspire/client/juniper/juniper/media/result.txt")
                                model = gensim.models.Word2Vec(inputData1, size=200, window=5, min_count=1, workers=1)
                                sentence1AvgVector = abs(avg_feature_vector1(sentence.split(), model, 200))
                                sentence2AvgVector = abs(avg_feature_vector1(sentence1.split(), model, 200))
                               
                                similarity = 1 - sc.spatial.distance.cosine(sentence2AvgVector,sentence1AvgVector)
                                resultArray[i,j] = round(similarity,4)*100
                        else:
                                similarity = 1
                                resultArray[i,j] = similarity*100
        thefile = open('/home/aspire/client/juniper/juniper/media/textrequirementprocessed.txt', 'w')
        #thefile = open(os.path.join(settings.PROJECT_ROOT, 'media/textrequirementprocessed.txt'), 'w')
        thefile.close()
        #Convert numpy array to List
        resultArraytoList = resultArray.tolist()
        print (json.dumps(resultArraytoList))
        return resultArraytoList
#optimize('english')
