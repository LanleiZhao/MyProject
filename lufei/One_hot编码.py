# -*- coding:utf-8 -*-
from sklearn.feature_extraction import DictVectorizer

dc = DictVectorizer()

data = [{'city':'北京','temperature':100},{'city':'上海','temperature':80},{'city':'广州','temperature':120}]
# print(data[1])
data_after = dc.fit_transform(data)
print(dc.feature_names_)
print(data)
print('*'*50)
print(data_after.toarray())

