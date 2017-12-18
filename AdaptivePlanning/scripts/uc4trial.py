from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score
from sklearn.externals import joblib
import pandas as pd
import numpy as np
import math

df = pd.read_csv('train_data.csv')
#print df.Budget
dictReleaseBudget = dict(zip(df.rel_id, df.Budget_in_Use))

inputData = df[['defect_density','defect_leakage','defect_rejection','test_case_count','application_complexity','domain_knowledge','technical_skills','requirement_query_count','code_review_comments','design_review_comments','No_of_Resources','Budget_in_Use','Number_of_days_Completion','Cost_of_resource','Efficiency','Project_Status','Availability_Of_Budget']].as_matrix()

inputLabels = df.Project_Status.values.ravel()

#Create a RandomForest Regerssor
regressor = RandomForestRegressor(n_estimators=300,max_features='auto',min_samples_split=10)# initialize
regressor.fit(inputData, inputLabels) # fit the data to the algorithm

joblib.dump(regressor, 'randomforestregression.pkl')

print ("Model Saved Successfully")
