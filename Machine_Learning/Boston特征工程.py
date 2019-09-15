# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV
from sklearn.metrics import r2_score

df = pd.read_csv(r"F:\CSDN\boston_housing.csv")
# print(df.head())
# print(df.info())
# print(df.describe())

# 数据去噪声
# df = df[df.MEDV<50]
# 输出样本数和特征维数
# print(df.shape)

y = df['MEDV']
X = df.drop('MEDV',axis=1)
# 对y进行log变换，对log变换之后的价格进行估计
log_y = np.log1p(y)

# 离散特征进行独热编码
X['RAD'].astype('object')
X_cat = X['RAD']
X_cat = pd.get_dummies(X_cat, prefix='RAD')
# print(X_cat.head())
X = X.drop('RAD',axis=1)
# 特征名称
feature_cols = X.columns

"""特征标准化处理，去量纲，使用sklearn.preprocessing.StandardScaler"""
# 初始化标准器对象
ss_X = StandardScaler()
ss_y = StandardScaler()
ss_log_y = StandardScaler()
# 标准化处理
X = ss_X.fit_transform(X)
y  = ss_y.fit_transform(y.values.reshape(-1,1))
log_y = ss_log_y.fit_transform(log_y.values.reshape(-1,1))
# print(X[:5])
# print(y[:2])

"""保存特征工程的结果到文件，供机器学习模型使用"""
fe_data = pd.DataFrame(data=X,columns=feature_cols,index=df.index)
fe_data = pd.concat([fe_data,X_cat],axis=1,ignore_index=False)
# print(fe_data.columns)

# 加上标签,添加两列，MEDV和log_MEDV
fe_data['MEDV'] = y
fe_data['log_MEDV'] = log_y
# print(fe_data.columns)
# print(fe_data.head())
# print(fe_data.info())
# 保存结果到文件
fe_data.to_csv(r"C:\Users\Lucas\Desktop\FE_boston_housing.csv",index=False)

# --------------------------------------------------------
df = pd.read_csv(r"C:\Users\Lucas\Desktop\FE_boston_housing.csv")
y = df['MEDV']
X = df.drop(['MEDV','log_MEDV'],axis=1)
feat_names = X.columns

# 训练和测试数据分离
X_train,X_test, y_train, y_test = train_test_split(X,y,test_size=0.2,random_state=33)

# 确定模型类型
# 线性回归
lr = LinearRegression() # 初始化
lr.fit(X_train,y_train)  # 训练
y_test_predict_lr = lr.predict(X_test)
y_train_predict_lr = lr.predict(X_train)
# 查看各特征的权重系数，系数的绝对值可以看作该特征的重要性
fs = pd.DataFrame({"columns":list(feat_names),"coef":np.abs(lr.coef_)})
print(fs.sort_values(by=['coef'],ascending=False))
# print(type(lr.coef_))
# print(lr.coef_)
# print(lr.coef_.shape)
# print(np.abs(lr.coef_))

# 使用r2_score评价模型的性能，并输出评估结果
print("The r2_score of LinearRegression on test:",r2_score(y_test,y_test_predict_lr))
print("The r2_score of LinearRegression on train:",r2_score(y_train,y_train_predict_lr))
# 观察预测值和真值的散点图
fig = plt.figure(figsize=(4,3))
plt.scatter(y_train,y_train_predict_lr)
plt.plot([-3,3],[-3,3],'--k')
plt.axis('tight')
plt.xlabel('True Value')
plt.ylabel("Predict Value")
plt.show()


