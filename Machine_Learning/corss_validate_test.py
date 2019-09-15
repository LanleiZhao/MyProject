# -*- coding:utf-8 -*-
from sklearn import datasets,linear_model
from sklearn.model_selection import cross_validate

diabetes = datasets.load_diabetes()
X = diabetes.data[:150]
y = diabetes.target[:150]
lasso = linear_model.Lasso()

cv_results = cross_validate(lasso,X,y,return_train_score=False)
# print(type(cv_results))
for i,j in cv_results.items():
    print(i,j,sep=',')

scores = cross_validate(lasso,X,y,scoring=('r2','neg_mean_squared_error'))
# print(type(scores))
print(scores['test_neg_mean_squared_error'])
print(scores['test_r2'])
print(scores['train_neg_mean_squared_error'])
print(scores['train_r2'])


