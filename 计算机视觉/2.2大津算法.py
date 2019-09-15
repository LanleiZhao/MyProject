# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# file_path = r"F:\CSDN\Image\rice_grain.jpg"
file_path = r"F:\CSDN\Image\lena.bmp"
img = cv.imread(file_path, 0) # 直接读取灰度图像

cv.imshow('original', img)

# 高斯模糊
gblur = cv.GaussianBlur(img,(5,5),0)

# 大津算法
_, thresh1 = cv.threshold(gblur, 120, 255 ,cv.THRESH_BINARY)
cv.imshow('thresh1', thresh1)


cv.waitKey()
cv.destroyAllWindows()