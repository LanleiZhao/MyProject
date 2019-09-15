# -*- coding:utf-8 -*-
import jieba

con1 = jieba.cut("每一次的成长都必然伴随着痛苦,世界上只有一种真正的英雄主义，那就是在认清生活的真相后依然热爱生活。")
print(type(con1))
content1 = list(con1)
print(type(content1))
print(content1)
rslt = '|'.join(content1)
print(type(rslt))
print(rslt)
