# -*- coding:utf-8 -*-
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
import pandas as pd
import numpy as np


def knncls():
    """
    K-近邻预测用户签到位置
    :return:
    """
    # 读取数据
    data = pd.read_excel(r"F:\CSDN\数据集\Predicting_Check_Ins\train_small_sets.xlsx")
    # 处理数据
    # 1. 缩小数据,查询数据筛选
    data = data.query("x > 1.0 & x < 1.25 & y > 2.5 & y < 2.75")

    # 处理时间
    # 把日期格式转换成字典格式
    time_value = pd.to_datetime(data['time'], unit='s')
    print(time_value)

    # 构造一些日期、时间的特征
    time_value = pd.DatetimeIndex(time_value)
    data['day'] = time_value.day
    data['hour'] = time_value.hour
    data['weekday'] = time_value.weekday

    # 把时间戳特征删除
    data.drop(['time'], axis=1)

    # 把签到数量少于n个目标位置删除
    place_count = data.groupby('place_id').count()
    tf = place_count[place_count.row_id > 3].reset_index()
    data = data[data['place_id'].isin(tf.place_id)]

    # 取出数据中的特征值和目标值
    y = data['place_id']
    X = data.drop(['place_id','row_id'], axis=1)

    # 进行数据的分割训练集 和 测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

    # 特征工程
    std = StandardScaler()  # 标准化
    X_train = std.fit_transform(X_train)
    X_test = std.transform((X_test))

    # 进行算法流程
    # knn = KNeighborsClassifier(n_neighbors=5)
    # knn.fit(X_train, y_train)
    #
    # # 得出预测结果
    # y_predict = knn.predict(X_test)
    # print("预测的目标登记入住位置为：", y_predict)
    #
    # # 得出准确率
    # print("预测的分值为：", knn.score(X_test, y_test))

    # 超参数搜索
    # knn2 = KNeighborsClassifier()  # 不设置参数
    # # 构造参数的值
    # param = {'n_neighbors': [1,3,5,7]}
    # gc = GridSearchCV(knn2, param_grid=param, cv=2)
    # gc.fit(X_train, y_train)
    # # 预测准确率
    # print("测试集的得分：", gc.score(X_test, y_test))
    # print("最佳参数:", gc.best_params_)
    # print("最佳分数:", gc.best_score_)
    # print("最佳学习器:", gc.best_estimator_)
    # print("每次交叉验证的结果", gc.cv_results_)


if __name__ == "__main__":
    knncls()
    # print(help(pd.DatetimeIndex))
