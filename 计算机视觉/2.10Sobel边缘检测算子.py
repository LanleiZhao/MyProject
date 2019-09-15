# -*- coding:utf-8 -*-
import cv2 as cv
# 读取图片
# file_path = r"F:\CSDN\Image\lena.bmp"
file_path = r"F:\CSDN\Image\chessboard.jpg"
img = cv.imread(file_path)

# 灰度转换
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 求取x方向边界
sobel_x = cv.Sobel(gray, ddepth=-1, dx=1, dy=0, ksize=3)
# 求取y方向边界
sobel_y = cv.Sobel(gray, ddepth=-1, dx=0, dy=1, ksize=3)
# 求取x,y两个方向的边界
sobel_xy = cv.Sobel(gray, ddepth=-1, dx=1, dy=1, ksize=3)

cv.imshow('origion', img)
cv.imshow('sobel_x', sobel_x)
cv.imshow('sobel_y', sobel_y)
cv.imshow('sobel_xy', sobel_xy)

cv.waitKey()
cv.destroyAllWindows()