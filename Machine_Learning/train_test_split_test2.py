# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r"F:\CSDN\FE_boston_housing.csv")
# print(df.head())
# print(df.columns)
col_y = ['MEDV','log_MEDV']
y = pd.DataFrame(df,columns=col_y)
# print(y)
X = df.drop(['MEDV','log_MEDV'],axis=1)
feature_names = X.columns
# print(feature_names)

# 训练数据和测试数据分割
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=33)

# 线性回归模型
# 初始化
lr = LinearRegression()
# 训练模型
lr.fit(X_train,y_train)
# print(lr.coef_)
# print(lr.intercept_)
# 预测
y_train_predict_lr = lr.predict(X_train)
y_test_predict_lr = lr.predict(X_test)

# 查看个特征的权重
data = {"columns":list(feature_names),"coef_org":list(lr.coef_[0,:].T),"coef_log":list(lr.coef_[1:].T)}
fs = pd.DataFrame(data)
# print(fs)

# 评估打分
# print("r2_score on train:",r2_score(y_train,y_train_predict_lr))
# print("r2_score on test:",r2_score(y_test,y_test_predict_lr))
# 训练集
print("r2 score of LinearRegression on train with original MEDV:",r2_score(y_train.iloc[:,0],y_train_predict_lr[:,0]))
# 测试集
print("r2 score of LinearRegression on test with Original MEDV:",r2_score(y_test.iloc[:,0],y_test_predict_lr[:,0]))

# 训练集
print("r2 score of LinearRegression on train with log MEDV:",r2_score(y_train.iloc[:,1],y_train_predict_lr[:,1]))
# 测试集
print("r2 score of LinearRegression on test with log MEDV:",r2_score(y_test.iloc[:,1],y_test_predict_lr[:,1]))




