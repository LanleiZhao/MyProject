# -*- coding:utf-8 -*-
from sklearn.naive_bayes import MultinomialNB
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report

def naviebays():
    """
    朴素贝叶斯进行文本分类
    :return:
    """
    news = fetch_20newsgroups(subset='all')

    # 进行数据分割
    X_train, X_test, y_train, y_test = train_test_split(news.data,news.target,test_size=0.25)

    # 对数据集进行特征抽取
    tf = TfidfVectorizer()

    # 以训练集当中的词的列表进行每篇文章重要性统计
    X_train = tf.fit_transform(X_train)
    print(tf.get_feature_names())

    X_test = tf.transform(X_test)
    # print(X_train.toarray()[:10])

    # 贝叶斯算法预测
    mlt = MultinomialNB(alpha=1.0)

    mlt.fit(X_train,y_train)
    y_test_predict = mlt.predict(X_test)

    # 准确率
    print("准确率：",mlt.score(X_test,y_test))
    cr = classification_report(y_test,y_test_predict,target_names=news.target_names)
    print(cr)

if __name__ == '__main__':
    naviebays()




