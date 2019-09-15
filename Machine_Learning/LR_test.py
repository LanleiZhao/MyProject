# -*- coding:utf-8 -*-
from sklearn import linear_model

lr = linear_model.LinearRegression()

lr.fit([[0,0],[1,1],[2,2]],[0,1,2])
print(lr.coef_)