# -*- coding:utf-8 -*-
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import export_graphviz
import pandas as pd

def dtcls():
    """
    泰坦尼克号预测生死
    :return:
    """
    # 读取数据
    data = pd.read_csv(r"http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    print(data.head())

    # 处理数据，找出特征值和目标值
    x = data[['pclass', 'age', 'sex']]
    y = data['survived']
    print(x.head())

    # 缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True)

    # 分割数据集到训练集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.25)

    # 进行特征工程，one_hot编码
    # print(data.info())
    dict = DictVectorizer(sparse=False)
    x_train = dict.fit_transform(x_train.to_dict(orient='records'))
    print(dict.get_feature_names())
    print('dict\n', x_train[:10])
    x_test = dict.transform(x_test.to_dict(orient='records'))

    # 决策树进行预测
    dec = DecisionTreeClassifier()
    dec.fit(x_train, y_train)
    # 预测
    y_test_predict = dec.predict(x_test)
    # 评价
    print("准确率", dec.score(x_test, y_test))

    # 导出决策树的结构
    # export_graphviz(dec,out_file="./tree2.dot",feature_names=['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=female', 'sex=male'])

if __name__ == '__main__':
    dtcls()
