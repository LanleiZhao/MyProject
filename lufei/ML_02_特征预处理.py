# -*- coding:utf-8 -*-
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler,StandardScaler,Imputer
import numpy as np
import pandas as pd

def mm_scaler():
    """
    归一化处理
    :return:
    """
    mm = MinMaxScaler()  # 初始化实例对象
    data = mm.fit_transform([[90,2,10,40],[60,4,15,45],[75,3,13,46]])
    print(data)

def std_scaler():
    """
    标准化处理
    :return:
    """
    ss = StandardScaler()
    data = ss.fit_transform([[90,2,10,40],[60,4,15,45],[75,3,13,46]])
    print(ss.mean_)
    print('*'*50)
    print(data)

def im():
    """
    缺失值处理
    :return:
    """
    im = Imputer(missing_values='NaN',strategy='mean',axis=0)
    data = im.fit_transform([[1,2],[np.nan,3],[7,6]])
    print(data)

def pd_fillna():
    """
    pandas fill missing values
    :return:
    """
    df = pd.DataFrame([1,2,3,'?',4],columns=['row1'])
    print(df)
    df1 = df.replace('?',np.NaN).fillna(0)
    print(df1)

if __name__ == "__main__":
    # mm_scaler()
    # std_scaler()
    pd_fillna()


