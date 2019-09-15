# -*- coding:utf-8 -*-
import cv2 as cv
import copy
import numpy as np
"""
检测图中所有面积>50的米粒
"""

# 图像采集
file_path = r"F:\CSDN\Image\rice_grain.jpg"
img = cv.imread(file_path)

# 图像预处理
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# 基于灰度的阈值分割
_, bw = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)
# bw = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, -3)

element = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))  # 定义结构元素
bw = cv.morphologyEx(bw, cv.MORPH_OPEN, element)  # 形态学滤波,开运算

seg = copy.deepcopy(bw)
bin, cnts, hier = cv.findContours(seg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
count = 0
# print(len(cnts))
for i in range(0, len(cnts)):
    c = cnts[i]
    area = cv.contourArea(c)
    if area < 10:
        continue
    count = count + 1
    print("blob", i + 1, ":", area)

    # 水平包围轮廓
    x, y, w, h = cv.boundingRect(c)
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0xff), 1)
    cv.putText(img, str(count), (x, y), cv.FONT_HERSHEY_PLAIN, 0.5, (0, 0xff, 0))

    # 最小包围轮廓


# 得到最终结果
print('米粒数量', count + 1)
cv.imshow('origin img', img)
cv.imshow('after thresh', bw)

cv.waitKey()
cv.destroyAllWindows()
