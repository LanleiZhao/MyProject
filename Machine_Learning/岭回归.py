# -*- coding:utf-8 -*-
from sklearn import linear_model
reg = linear_model.Ridge(alpha=.5)
reg.fit()
