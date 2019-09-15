# -*- coding:utf-8 -*-
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

li = load_iris()
print("特征值")
print(li.data)
print("目标值")
print(li.target)
# print("描述信息")
# print(li.DESCR)

X_train,X_test,y_train,y_test = train_test_split(li.data,li.target,test_size=0.25)

sklearn.datasets.fetch_20newsgroups(data_home=None,subset='train')
#subset：'train','test','all',可选参数，选择要加载的数据集
datasets.clear_data_home(data_home=None)
#清除目录下的数据