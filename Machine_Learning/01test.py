# -*- coding:utf-8 -*-
from sklearn import datasets
from sklearn.model_selection import train_test_split

# iris = datasets.load_iris()
iris = datasets.load_diabetes()
# print(iris.data)

# 输出数据所属的真实标签
# print(iris.target)

# 输出数据的维度
print(iris.data.shape)

# 输出数据标签的名字
# print(iris.target_names)
# ['setosa' 'versicolor' 'virginica']

# ------------------------------------------
print("iris数据集的大小：",iris.data.shape)
print("iris目标数据集的大小：",iris.target.shape)
X_train,X_test,Y_train,Y_test = train_test_split(iris.data,iris.target,test_size=0.5,random_state=0)
print("生成的训练集的特征个数(数据个数): ",X_train.shape)
print("生成的训练集的标签个数： ",Y_train.shape)
print("生成的测试集的特征个数： ",X_test.shape)
print("生成的测试集的标签个数： ",Y_test.shape)
print("iris数据集的前5行的数据： ",iris.data[:5])
print("生成的训练集的前5行数据： ",X_train[:5])
print("生成的训练集的前5行,前两列的数据： ",X_train[:5,:2])

