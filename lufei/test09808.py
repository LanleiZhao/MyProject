# -*- coding:utf-8 -*-
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import  TfidfVectorizer

import jieba

def dictvec():
    """"
    字典数据抽取
    """
    # 实例化
    dict = DictVectorizer(sparse=False)
    # 调用fit_transform
    data = dict.fit_transform([{'city':'北京','temperature':100},{'city':'上海','temperature':80},{'city':'广州','temperature':120}])
    print(dict.get_feature_names())
    print(type(data))
    print(data)

def countvec():
    """
    对文本特征值化
    """
    # 实例化对象
    cv = CountVectorizer()
    # data = cv.fit_transform(["Life Life is short,I use Python","Life is long,I dislike dislike Python"])
    data = cv.fit_transform(["人生 苦短，我 用 python","人生 漫长，我 不用 python"])
    print(cv.get_feature_names())
    # print(data)
    print(data.toarray())

def jieba_cut():
    con1 = jieba.cut("每一次的成长都必然伴随着痛苦,世界上只有一种真正的英雄主义，那就是在认清生活的真相后依然热爱生活。")
    con2 = jieba.cut("不想干，也不愿意去想，安于现状、与世无争、承受不了压力，只想不劳而获，每天做着美梦，温水煮青蛙，这种人是舒服死的。")
    # 转化成列表
    content1 = list(con1)
    content2 = list(con2)
    # 把列表转换成字符串
    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    return c1,c2

def hanzivec():
    """中文特征值化"""
    c1,c2 =jieba_cut()
    print('c1',c1)
    print('c2',c2)
    cv = CountVectorizer()
    data = cv.fit_transform([c1,c2])
    print(cv.get_feature_names())
    print(data.toarray())

def hanzitf():
    """TF-IDF特征值化"""
    c1,c2 = jieba_cut()
    # print('c1',c1)
    # print('c2',c2)
    tf = TfidfVectorizer()
    # tf_data =tf.fit_transform([c1,c2])
    tf_data =tf.fit_transform(['千江 有水 千 江月，万里 无云 万里 天',' 万里 长征 红军'])
    print(tf.get_feature_names())
    print(tf_data.toarray())



if __name__ == "__main__":
    # dictvec()
    # countvec()
    # hanzivec()
    hanzitf()


