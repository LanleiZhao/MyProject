# -*- coding:utf-8 -*-
import cv2 as cv

file_path = r"F:\CSDN\Image\coins.jpg"
img = cv.imread(file_path)
cv.imshow('original image', img)

# 灰度转换
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 全局阈值法
_,global_thresh = cv.threshold(src=gray_image, thresh=120, maxval=255, type= cv.THRESH_BINARY)
cv.imshow('global thresh', global_thresh)

# 区域阈值法
adaptive_image = cv.adaptiveThreshold(src=gray_image, maxValue=256, adaptiveMethod=1, thresholdType=0, blockSize=9, C=10)
cv.imshow('adaptive_image',adaptive_image)

cv.waitKey()
cv.destroyAllWindows()

"""
参考资料：
https://blog.csdn.net/sinat_36264666/article/details/77586964
"""
