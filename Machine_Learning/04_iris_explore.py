# -*- coding:utf-8 -*-
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# 加载鸢尾花数据
iris = datasets.load_iris()

# 查看特征名称
print("feature_names:{0}".format(iris.feature_names))
# 查看标签名称
print("target_names:{}".format(iris.target_names))
# 查看元数据(特征矩阵)的形状
print("data shape:{0}".format(iris.data.shape))
# 查看数据前5行
print("data top 5:\n {0}".format(iris.data[:5]))
# 查看目标标签的类比标识
print("target unique:{}".format(np.unique(iris.target)))
print("target top 5：\n{0}".format(iris.target[:5]))

# 数据可视化
sepal_lenth_list = iris.data[:, 0]  # 花萼长度
sepal_width_list = iris.data[:, 1]  # 花萼宽度
# 构建setosa,versicolor,virginica索引数组
setosa_index_list = iris.target == 0
versicolor_index_list = iris.target == 1
virginica_index_list = iris.target == 2

plt.scatter(sepal_lenth_list[setosa_index_list], sepal_width_list[setosa_index_list], color='red', marker='o',
            label='setosa')
plt.scatter(sepal_lenth_list[versicolor_index_list], sepal_width_list[versicolor_index_list], color='blue', marker='x',
            label='versicolor')
plt.scatter(sepal_lenth_list[virginica_index_list], sepal_width_list[versicolor_index_list], color='green', marker='+',
            label='virginica')
# 设置legend
plt.legend(loc='best', title='iris type')
# 设置横坐标名称
plt.xlabel('sepal_length(cm')
plt.ylabel('sepal_with(cm')

plt.show()

"""使用逻辑回归分类器识别"""
# 指定训练数据 X
X = iris.data
# 指定训练目标
y = iris.target

# 创建一个逻辑回归分类器
clf = linear_model.LogisticRegression()
# 使用样本数据训练（喂养）分类器
clf.fit(X, y)
# 待预测样本
wait_predict_sample = X[np.newaxis, 0]
print("wait_predict_sample:{0}".format(wait_predict_sample))
# 预测所属目标类别
print("predict:{0}".format(clf.predict(wait_predict_sample)))
# 预测所属不同目标类别的概率
print("predict_proba:{0}".format(clf.predict_proba(wait_predict_sample)))
