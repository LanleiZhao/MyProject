# -*- coding:utf-8 -*-
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

"""
泰坦尼克号预测生死
"http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt"
"""


def dtcls():
    # 读取数据
    data = pd.read_csv(r"http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    # print(type(data))
    # print(data.columns)
    # print(data.head())
    x = data[['pclass', 'age', 'sex']]
    y = data['survived']

    # 数据预处理
    print(x.head())
    print(x.info())
    # age特征有近一半的空值，缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True)
    # 数据分为训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    # 特征工程
    # pclass 和 sex都是文本，因此要进行Ont-HOT编码，字典特征抽取
    dv = DictVectorizer(sparse=False)
    x_train = dv.fit_transform(x_train.to_dict(orient='records'))
    # print(type(x_train))
    # print(x_train[:10])
    # print(dv.get_feature_names())
    x_test = dv.transform(x_test.to_dict(orient='records'))

    # 决策树分析
    dt = DecisionTreeClassifier()
    dt.fit(x_train, y_train)

    # 预测
    y_test_predict = dt.predict(x_test)
    # 评估性能
    print("测试集上的评估分数：", dt.score(x_test, y_test))
    # x_test = pd.DataFrame(data=x_test,columns=dv.get_feature_names())
    # x_test.to_csv("test_data.csv")


def dt_csv():
    # 读取数据
    data = pd.read_csv(r'F:\CSDN\数据集\titanic.csv', engine='python')

    # 数据预处理
    x = data[['pclass', 'age', 'sex']]
    y = data['survived']
    # print(x.head(10))
    # 缺失值处理
    x['age'].fillna(x['age'].median(), inplace=True)
    # 数据集划分训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.25)

    # 特征工程
    # One-Hot编码
    dv = DictVectorizer(sparse=False)
    x_train = dv.fit_transform(x_train.to_dict(orient='records'))
    print(type(x_train))
    x_test = dv.transform(x_test.to_dict(orient='records'))

    # # 决策树训练
    # DT = DecisionTreeClassifier()
    # DT.fit(x_train, y_train)
    # # 决策树预测
    # y_test_pred = DT.predict(x_test)
    # # 决策树评估
    # print("score:",DT.score(x_test,y_test))

    # 随机森林进行预测,超参数调优
    rf = RandomForestClassifier()
    # params = {'n_estimators': [120, 200, 300, 500, 800, 1200], 'max_depth': [5, 8, 15, 25, 30]}
    params = {'n_estimators': [50,60,70, 80, 90, 100, 110, 120,130], 'max_depth': [3,4,5, 7,9]}

    # 网格搜索
    gc = GridSearchCV(rf, param_grid=params, cv=2)
    gc.fit(x_train, y_train)
    print("准确率：", gc.score(x_test, y_test))
    print("参数模型：", gc.best_params_)


if __name__ == '__main__':
    # dtcls()
    dt_csv()
