# -*- coding:utf-8 -*-
import numpy as np
import cv2 as cv

file_path = r"F:\CSDN\Image\lena.bmp"
gray_file_path = r"F:\CSDN\Image\gray.bmp"
img = cv.imread(file_path)
gray_img = cv.imread(gray_file_path,0)


px = img[100,100]
print("px value:", px)
blue = img[100,100][0]
print('blue:', blue)

print("img shape:", img.shape)
print("gray img shape:", gray_img.shape)

print("img size:", img.size)
print("gray img size:", gray_img.size)

# dtype
print(img.dtype)
print(gray_img.dtype)

# Image ROI
ROI = img[200:380,230:400]
# img[10:190,10:180] = ROI
#
# cv.imshow('ROI', ROI)
# cv.imshow('After Img', img)
# cv.waitKey()
# cv.destroyAllWindows()

# Splitting and Merging Image Channels
channel_list = cv.split(img)
# print(type(a))
for i,channel in enumerate(channel_list):
    cv.imshow(i, channel)
    cv.waitKey()
    cv.destroyAllWindows()










