# -*- coding:utf-8 -*-
import numpy as np
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression,SGDRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def mylinear():
    """
    预测房子价格
    :return:
    """
    # 获取数据
    lb = load_boston()

    # 分割数据集
    x_train, x_test, y_train, y_test = train_test_split(lb.data, lb.target, test_size=.25)

    # 标准化处理,分别对特征值和目标值进行标准化
    ssx = StandardScaler()
    ssy = StandardScaler()
    x_train = ssx.fit_transform(x_train)
    y_train = ssy.fit_transform(y_train.reshape(-1,1))  # 一列特征标准化时，必须转换为二维
    x_test = ssx.transform(x_test)
    y_test = ssy.transform(y_test.reshape(-1,1))

    # 预测
    lr = LinearRegression()
    lr.fit(x_train, y_train)
    y_test_pred = lr.predict(x_test)
    # 转换标准化之后的预测值
    y_lr_predict = ssy.inverse_transform(y_test_pred)

    print(lr.coef_)  # 回归系数
    print(y_lr_predict[:10])  # 预测的价格
    print("正规方差的均方误差：",mean_squared_error(ssy.inverse_transform(y_test), y_lr_predict))

    # SGD梯度下降
    sgd = SGDRegressor()
    sgd.fit(x_train,y_train)
    y_test_sgd_pred = sgd.predict(x_test)
    print(sgd.coef_)
    print(y_test_sgd_pred[:10])
    y_sgd_predict = ssy.inverse_transform(y_test_sgd_pred)  # 准换为标准化之前的预测值
    print("梯度下降的均方误差：",mean_squared_error(ssy.inverse_transform(y_test),y_sgd_predict))


if __name__ == '__main__':
    mylinear()
