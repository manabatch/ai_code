import numpy as np
from urllib.request import urlopen
import urllib
import pandas as pd
import pgmpy
from pgmpy.inference import VariableElimination
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator, BayesianEstimator 
names = ['age','chol', 'fbs', 'restecg', 'thalach','target'
]
heartDisease = pd.read_csv('D:\\Engineering\\SEM-6\\Artificial Intelligence\\Lab Work\\Programs\\heart_disease_data.csv')
heartDisease = heartDisease.replace('?', np.nan)
model = BayesianModel([('age', 'fbs'), ('fbs', 'target'), ('target', 'restecg'), ('target', 'thalach'), ('target',
'chol')])
model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)
from pgmpy.inference import VariableElimination
HeartDisease_infer = VariableElimination(model)
q = HeartDisease_infer.query(variables=['target'], evidence={'age': 37})
print(q)
