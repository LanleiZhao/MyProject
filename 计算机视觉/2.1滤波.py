# -*- coding:utf-8 -*-
import cv2 as cv

# 测试图片路径
# file_path = r"F:\CSDN\Image\smoothing.jpg"
file_path = r"F:\CSDN\Image\family.jpg"
# 读取图片
img = cv.imread(file_path)
# 显示原始图片
cv.imshow('original imgage', img)

"""图片平滑处理"""
# 高斯模糊
Gaussian_img = cv.GaussianBlur(src=img,ksize=(15,15),sigmaX=0)
cv.imshow('Guassian Blur', Gaussian_img)

# 中值模糊
media_blur = cv.medianBlur(src=img, ksize=9, dst=None)
cv.imshow('Media Blur',media_blur)

# 腐蚀
erode_img = cv.erode(src=img, kernel=(5,5), iterations=10)
cv.imshow('erode_img', erode_img)

# 膨胀
dilate_img = cv.dilate(src=img,kernel=(5,5),iterations=20)
cv.imshow('dilate_img', dilate_img)

# 形态学滤波，开运算，先腐蚀后膨胀
morphology_open= cv.morphologyEx(src=img, op=cv.MORPH_OPEN, kernel=(5,5), iterations=10)
cv.imshow('morphology_open', morphology_open)

# 形态学滤波，闭运算，先膨胀后腐蚀
morphology_close = cv.morphologyEx(src=img, op=cv.MORPH_CLOSE, kernel=(5,5), iterations=10)
cv.imshow('morphology_close', morphology_close)

# canny算子
canny_img = cv.Canny(img,60,100)
cv.imshow('canny_img',canny_img)

# sobel算子
# Sobel_img = cv.Sobel(src=img,ddepth=-1, dx=1, dy=0)
# cv.imshow('Sobel_img', Sobel_img)
#
# Sobel_img2 = cv.Sobel(src=img,ddepth=-1, dx=0, dy=1)
# cv.imshow('Sobel_img2', Sobel_img2)

# Sobel_img3 = cv.Sobel(src=img,ddepth=-1, dx=1, dy=1)
# cv.imshow('Sobel_img3', Sobel_img3)


# 拉普拉斯算子
# laplace_img = cv.Laplacian(src=img,ddepth=-1)
# cv.imshow('laplace_img', laplace_img)

# loG算子
# loG_img = cv.log(src=img)
# cv.imshow('loG_img',loG_img)


cv.waitKey()
cv.destroyAllWindows()
