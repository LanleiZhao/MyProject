# -*- coding:utf-8 -*-
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA


def var():
    """
    特征选择，删除低方差的特征
    :return:
    """
    var_ts = VarianceThreshold(threshold=0)
    data = var_ts.fit_transform([[0, 2, 0, 3], [0, 1, 4, 3], [0, 1, 1, 3]])
    print(data)


def pca():
    """
    主成分分析，特征降维
    :return:
    """
    pca = PCA(n_components=.9)
    X_data = [[2, 8, 4, 5], [6, 3, 0, 8], [5, 4, 9, 1]]
    data = pca.fit_transform(X_data)
    print(X_data)
    print(data)

if __name__ == '__main__':
    var()
    # pca()


