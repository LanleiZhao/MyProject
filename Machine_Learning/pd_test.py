# -*- coding:utf-8 -*-
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# df = pd.read_csv(r"‪F:\CSDN\boston_housing.csv")
df = pd.read_csv(r"F:\CSDN\boston_housing.csv")
"""
开始read_csv报错，不是中文路径，也加了r或者\转义，都不管用。
最后发现是在win下点击文件属性复制路径，会加一个奇怪的字符。
所以重新拼了路径，问题解决。
"""
fig = plt.figure()
sns.distplot(df['MEDV'],bins=30,kde=True,color='orange')


fig1 = plt.figure()
sns.countplot(df['CHAS'])
plt.xlabel("River")
plt.ylabel("Count of Occurence")

fig2 = plt.figure()
sns.countplot(df["PTRATIO"])


plt.show()


