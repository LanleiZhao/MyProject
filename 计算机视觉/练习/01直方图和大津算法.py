# -*- coding:utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt

file_path = r"F:\CSDN\Image\lena.bmp"
img = cv.imread(file_path)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 灰度转换
gaussianblur_img = cv.GaussianBlur(gray_img, (5, 5), 0)  # 高斯滤波
_, thresh1 = cv.threshold(gaussianblur_img, 0, 255, cv.THRESH_OTSU)  # 大津算法
hist_cv = cv.calcHist([img], [0], None, [256], [0, 255])  # 计算灰度直方图

plt.subplot(221)
plt.imshow(gray_img, 'gray')

plt.subplot(222)
plt.plot(hist_cv, 'gray')

plt.subplot(223)
plt.imshow(gaussianblur_img, 'gray')

plt.subplot(224)
plt.imshow(thresh1, 'gray')

plt.show()
