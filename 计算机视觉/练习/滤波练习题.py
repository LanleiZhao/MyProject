# -*- coding:utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt

"""1. 以Lena为原始图像，通过OpenCV实现平均滤波，高斯滤波及中值滤波，比较滤波结果。"""

img = cv.imread(r"F:\CSDN\Image\lena.bmp")
# cv.imshow('origin', img)

"""平均滤波是取锚点邻域像素的均值，作为瞄点的新像素值,kernal越大，图像滤波之后越模糊"""
mean_blur3 = cv.blur(img, (3, 3))  # (3,3)表示3x3的卷积模板
mean_blur5 = cv.blur(img, (5, 5))  # (5,5)表示5x5的卷积模板
# cv.imshow('mean_blur3', mean_blur3)
# cv.imshow('mean_blur5', mean_blur5)

"""
高斯滤波每一个像素点的值，都由其本身和邻域内的其他像素值经过加权平均后得到，权值由高斯函数确定
第四个参数，double类型的sigmaX，表示高斯核函数在X方向的的标准偏差。
第五个参数，double类型的sigmaY，表示高斯核函数在Y方向的的标准偏差。若sigmaY为0，就将它设为sigmaX，如果sigmaX和sigmaY都是0，那么就由ksize.width和ksize.height计算出来。
"""
gaussian_blur = cv.GaussianBlur(img, ksize=(5, 5), sigmaX=0)
# cv.imshow('Gaussian Blur', gaussian_blur)

"""中值滤波可以有效去除椒盐噪波，但是图像也会有一定的模糊，锐利度有所下降"""
median_blur = cv.medianBlur(img, ksize=7)  #ksize为整数，且为奇数
# cv.imshow('median_blur', median_blur)
plt.subplot(221)
plt.imshow(img)

plt.show()

cv.waitKey()
cv.destroyAllWindows()
