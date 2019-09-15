# -*- coding:utf-8 -*-
import cv2 as cv

img1 = cv.imread(r"‪F:\CSDN\Image\lena.bmp")
img2 = cv.imread(r"F:\CSDN\Image\logo.png")

print(img1)
# print(img2.shape)
# print(img1.shape)
# I want to put logo on top_left corner,so I create a ROI
# img2_shape = img2.shape
# roi = img1[0:img2_shape[0], 0:img2_shape[1]]

# cv.imshow('logo',img2)
# cv.imshow('lena', img1)
# cv.waitKey()
# cv.destroyAllWindows()
