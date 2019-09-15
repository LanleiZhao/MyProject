# -*- coding:utf-8 -*-
import cv2 as cv
# 读取图片
file_path = r"F:\CSDN\Image\lena.bmp"
# file_path = r"F:\CSDN\Image\chessboard.jpg"
img = cv.imread(file_path)


# 灰度转换
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 高斯滤波
gaussian_blur = cv.GaussianBlur(gray, (3,3), 0)

# Laplace算子
Laplacian_img1 = cv.Laplacian(img, -1)
Laplacian_img2 = cv.Laplacian(img, cv.CV_64F)

# Canny算子
Canny_img = cv.Canny(gray,100,240)
Gaussian_Canny_img = cv.Canny(gaussian_blur,100,240)

cv.imshow('Laplacian_img1', Laplacian_img1)
cv.imshow('Laplacian_img2', Laplacian_img2)
cv.imshow('Canny_img', Canny_img)
cv.imshow('Gaussian_blur_Canny_img', Gaussian_Canny_img)
cv.waitKey()
cv.destroyAllWindows()