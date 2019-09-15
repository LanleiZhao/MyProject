# -*- coding:utf-8 -*-
import cv2 as cv

img = cv.imread(r"F:\CSDN\Image\lena.bmp")
img_gaussian_blur = cv.GaussianBlur(img, (3, 3), sigmaX=0)
gray = cv.cvtColor(img_gaussian_blur, cv.COLOR_BGR2GRAY)
cv.imshow('origin', img)
cv.imshow('gray', gray)

"""Sobel算子"""
Sobel_X = cv.Sobel(gray, ddepth=-1, dx=2, dy=0, ksize=3)  # x方向一阶导数
cv.imshow('Sobel_X_direction', Sobel_X)
Sobel_Y = cv.Sobel(gray, ddepth=-1, dx=0, dy=1, ksize=3)  # y方向一阶导数
cv.imshow('Sobel_Y_direction', Sobel_Y)
Sobel_XY = cv.Sobel(gray, ddepth=-1, dx=1, dy=1, ksize=3)  # xy方向一阶导数
cv.imshow('Sobel_XY', Sobel_XY)

"""
Canny算法中减少假边缘数量的方法是采用双阈值法。选择两个阈值.
根据高阈值得到一个边缘图像，这样一个图像含有很少的假边缘，但是由于阈值较高，产生的图像边缘可能不闭合，未解决这样一个问题采用了另外一个低阈值。
在高阈值图像中把边缘链接成轮廓，当到达轮廓的端点时，该算法会在断点的8邻域点中寻找满足低阈值的点，再根据此点收集新的边缘，直到整个图像边缘闭合。
"""
Canny_img = cv.Canny(gray, 100, 240)
cv.imshow('Canny_img', Canny_img)

"""
Sobel 算子使用比较普遍，但边缘检测容易出现虚边，多重边，不够清晰。
Canny算子是对Sobel算子的改进，有较低的错误率，边缘可以很好的定位。
"""
cv.waitKey()
cv.destroyAllWindows()

# 参考：https://www.cnblogs.com/wangyaning/p/4236949.html
