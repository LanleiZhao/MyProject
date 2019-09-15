# -*- coding:utf-8 -*-
# from sklearn.model_selection import train_test_split
# import numpy as np

"""train_test_split"""
# X,y = np.arange(10).reshape((5,2)),list(range(5))
# # print(X)
# # print(y)
# X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.33,random_state=42)
# print(X_train)
# print(y_train)
# print("----------------")
# print(X_test)
# print(y_test)

"""分层K折交叉验证"""
# from sklearn.model_selection import StratifiedKFold
# X = np.array([[1,2],[3,4],[1,2],[3,4]])
# y = np.array([0,0,1,1])
# print(X)
# print('y',y)
# # print(X.shape)
# skf = StratifiedKFold(n_splits=2,random_state=None,shuffle=False)
# print(skf)
# print(skf.get_n_splits(X,y))
# for train_index,test_index in skf.split(X,y):
## split每次取出每折训练集和校验集的数据索引
#     print("Train:",train_index,"Test:",test_index)
#     print("---details----")
#     X_train,y_train = X[train_index],y[train_index]
#     X_test,y_test = X[test_index],y[test_index]
#     print("X_train:",X_train)
#     print("y_train:",y_train)
#     print("X_test:",X_test)
#     print("y_test:",y_test)
#     print("-------------------------")

"""
K折交叉验证评估模型性能
cross_val_score:评估一个指标，在校验集上的得分
cross_validate:允许指定多个指标进行评估
"""
# from sklearn import datasets,linear_model
# from sklearn.model_selection import cross_val_score
# diabetes = datasets.load_diabetes()
# X = diabetes.data[:150]
# y = diabetes.target[:150]
# lasso = linear_model.Lasso()  # 学习器
# # Lasso超参数lambda默认是1
# print(cross_val_score(lasso,X,y))

"""cross_validate"""
# from sklearn import datasets, linear_model
# from sklearn.model_selection import cross_validate
# from sklearn.metrics.scorer import make_scorer
# from sklearn.metrics import confusion_matrix
# from sklearn.svm import LinearSVC
#
# diabetes = datasets.load_diabetes()
# X = diabetes.data[:150]
# y = diabetes.target[:150]
# lasso = linear_model.Lasso()  # 机器学习模型
# cv_results = cross_validate(lasso, X, y, return_train_score=True)
# print(sorted(cv_results.keys()))
# # print(cv_results.values())
# print(cv_results['fit_time'])
# print(cv_results['score_time'])
# print(cv_results['test_score'])
# print(cv_results['train_score'])
#
# scores = cross_validate(lasso, X, y, scoring=('r2', 'neg_mean_squared_error'))
# print(scores.items())
# print(scores.keys())
# print(scores['test_neg_mean_squared_error'])

"""
超参数调优
遍历不同的超参数取值，选择性能最好的超参数lambda
GridSearchCV实现超参数调优
模型再训练：在选定...
"""
# from sklearn import svm,datasets
# from sklearn.model_selection import GridSearchCV
# iris = datasets.load_iris()
# parameters = {'kernel':('linear','rbf'),'C':[1,10]}
# svc = svm.SVC()
# clf = GridSearchCV(svc,parameters)
# clf.fit(iris.data, iris.target)
# # print(clf)
# print(sorted(clf.cv_results_.keys()))
# print("Best_parameters:\n",clf.best_params_)
# print("Best_scores:\n",clf.best_score_)
# print("Best_estimator:\n",clf.best_estimator_)

"""特殊的交叉验证：留一交叉验证"""
"""广义交叉验证"""
# RidgeCV
# LassoCV

"""
代码中给出了岭回归（RidgeCV）和Lasso（LassoCV）超参数（alpha_）
调优的过程，请结合两个最佳模型以及最小二乘线性回归模型的结果，
给出什么场合应该用岭回归，什么场合用Lasso，什么场合用最小二乘。（30分）
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import LassoCV

# 导入标准化的数据
df = pd.read_csv(r"F:\CSDN\FE_boston_housing.csv")
# print(df.head())
# 分离特征X和输出y
y = df['MEDV']
X = df.drop(['MEDV','log_MEDV'],axis=1)
# 特征名称
feature_names = X.columns
# print(feature_names)
# 训练和测试数据分离,20%用于测试
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=.2,random_state=30)
# print(X_train.shape)
# print(X_test.shape)
# 线性回归
lr = LinearRegression()
# 用训练数据训练模型
lr.fit(X_train, y_train)
# 用训练好的模型去预测
y_train_predit = lr.predict(X_train)
y_test_predit = lr.predict(X_test)
# 打印个特征权重系数值
# print(lr.coef_)
fs = pd.DataFrame({"columns":list(feature_names),"coef":list(lr.coef_)})
print(fs.sort_values(by=['coef'],ascending=False))
# 使用r2_score评价在训练集和测试集上的性能
print("The r2_score of LinearRegression on train:",round(r2_score(y_train,y_train_predit),2))
print("The r2_score of LinearRegression on test:",round(r2_score(y_test,y_test_predit),2))

# 预测值和真值的散点图
plt.figure(figsize=(4,3))
plt.scatter(y_train,y_train_predit)
plt.plot([-3,3],[-3,3],'--k')
# plt.axis('tight')
plt.xlabel('True Price')
plt.ylabel('Predict Price')
plt.show()
#--------------------------------
#岭回归/L2正则
# 设置超参数范围
alphas = [0.01,0.1,1,10,100]
# 生成一个RidgeCV的对象
ridge = RidgeCV(alphas = alphas, store_cv_values=True)
# 训练模型
ridge.fit(X_train,y_train)
# 预测
y_train_pred_ridge = ridge.predict(X_train)
y_test_pred_ridge =ridge.predict(X_test)
# 评估
print("ridge.alpha_:",ridge.alpha_)  # 最佳超参数alpha
print("The r2_score of RidgeCV on train:",round(r2_score(y_train,y_train_pred_ridge),2))
print("The r2_score of RigerCV on test:",round(r2_score(y_test,y_test_pred_ridge),2))
plt.xlabel("log(alpha)")
plt.ylabel("mse")
mse_mean = np.mean(ridge.cv_values_,axis=0)
plt.plot(np.log10(alphas),mse_mean.reshape(len(alphas),1))
plt.show()

#--------------------------------------
# 正则化的线性回归，L1正则Lasso
# 生成Lasso学习器对象
lasso = LassoCV()
# 训练
lasso.fit(X_train,y_train)
# 测试
y_train_pred_lasso = lasso.predict(X_train)
y_test_pred_lasso = lasso.predict(X_test)
# 评估
print("The r2_score of LassoCV on train:",round(r2_score(y_train,y_train_pred_lasso),2))
print("The r2_score of LassoCV on test:",round(r2_score(y_test,y_test_pred_lasso),2))
print("lasso.alpha:",lasso.alpha_)

# 查看各特征的权重
fs = pd.DataFrame({"Columns":list(feature_names),
                   "coef_lr":list(lr.coef_),
                   "coef_ridge":list(ridge.coef_),
                   "coef_lasso":list(lasso.coef_)})
print(fs.sort_values(by=['coef_lr'],ascending=False))


