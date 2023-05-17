import pandas as pd
from pgmpy.models import BayesianModel
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv('heart.csv', na_values='?')

model = BayesianModel([('age', 'fbs'), ('fbs', 'target'), ('target', 'restecg'), ('target', 'thalach'), ('target', 'chol')])

model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)

infer = VariableElimination(model)

query_result = infer.query(variables=['target'], evidence={'age': 37})
print(query_result)
