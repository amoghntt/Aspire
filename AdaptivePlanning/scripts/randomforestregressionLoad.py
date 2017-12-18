from sklearn.externals import joblib
import json
import sys
import string
import os
from django.conf import settings
#listInput = sys.argv[0]

#resultInputInt = map(int, listInput.strip('[]').split(','))
def res( resultInput=[]):
    resultInputInt=(resultInput)
    regressor = joblib.load(os.path.join(settings.PROJECT_ROOT, 'media/randomforestregression.pkl'))

    predictedProjectStatus= regressor.predict([resultInputInt])
    print(type(predictedProjectStatus))
    print predictedProjectStatus
    availabilityOfBudget = resultInputInt[16]
    print(type(availabilityOfBudget))

    adaptiveBudget = float((predictedProjectStatus.astype(float)/3)*int(availabilityOfBudget))

    print(type(adaptiveBudget))

    adaptiveBudget = round(adaptiveBudget,2)

    predictedProjectStatus = round(float(predictedProjectStatus),2)

    resultList = []

    resultList.append(predictedProjectStatus)

    resultList.append(adaptiveBudget)

    return adaptiveBudget,availabilityOfBudget


