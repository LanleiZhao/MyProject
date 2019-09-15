# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn.metrics import r2_score
import seaborn as sns

# 导入数据
df = pd.read_csv(r"F:\CSDN\class\第四周\hour.csv",engine='python')
print(df.head())
print(df.info())
print(df.describe())