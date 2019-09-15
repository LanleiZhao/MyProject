# -*- coding:utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"F:\CSDN\Image\lena.bmp")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 灰度转换

plt.subplot(231)
plt.title('gray image')
plt.imshow(gray, 'gray')

# BGR模式下的蓝色通道直方图
plt.subplot(232)
hist_cv1 = cv.calcHist([img], [0], None, [256], [0, 255])
plt.title('blue channel')
plt.plot(hist_cv1)

# BGR模式下的绿色通道直方图
plt.subplot(233)
hist_cv2 = cv.calcHist([img], [1], None, [256], [0, 255])
plt.title('green channel')
plt.plot(hist_cv2)

# BGR模式下的红色通道直方图
plt.subplot(234)
hist_cv3 = cv.calcHist([img], [2], None, [256], [0, 255])
plt.title('red channel')
plt.plot(hist_cv3)

# GRAY模式下的灰度直方图
plt.subplot(235)
hist_cv4 = cv.calcHist([gray], [0], None, [256], [0, 255])
plt.title('gray histgram')
plt.plot(hist_cv4)

plt.show()

"""
大津算法，将灰度图像二值化，转化为黑白图像，是一种全局阈值法，
通过遍历灰度范围，找到一个灰度值(阈值)，是前景和背景的组间差异最大，组内差异最小。
通过cv.threshold(img,thresh,maxval,type)实现。
大津算法只能读取灰度图，因此通过cvtColor转换为灰度图。
"""
_, thresh_B = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)  # 二值化
_, thresh_BI = cv.threshold(gray, 120, 255, cv.THRESH_BINARY_INV)  # 反向二值化
_, thresh_OTSU = cv.threshold(gray, 0, 255, cv.THRESH_OTSU)  # 自己选择最合适的thresh_type
cv.imshow('thresh_binary_B', thresh_B)
cv.imshow('thresh_binary_BI', thresh_BI)
cv.imshow('thresh_OTSU', thresh_OTSU)

# 阈值化之前，可以对灰度图高斯模糊，减小噪声,得到的图像更平滑
gray_gblur = cv.GaussianBlur(gray, (5, 5), sigmaX=0)
_, thresh1 = cv.threshold(gray_gblur, 120, 255, cv.THRESH_BINARY)
cv.imshow('blur_thresh_binary', thresh1)

cv.waitKey()
cv.destroyAllWindows()
