# -*- coding:utf-8 -*-
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img_path = r'F:\CSDN\Image\coins.png'
img = cv.imread(img_path)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
_,thresh = cv.threshold(gray_img, 0 , 255, cv.THRESH_OTSU + cv.THRESH_BINARY_INV)

kernal = np.ones((3,3), np.uint8)
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernal, iterations=2)

# sure background area
sure_bg = cv.dilate(opening, kernal, iterations=3) # 膨胀

# finding sure foreground area
dist_transform = cv.distanceTransform(opening, 1, 5)
_,sure_fg = cv.threshold(dist_transform, 0.2*dist_transform.max(), 255, cv.THRESH_BINARY)

# finding uknown region
sure_fg = np.uint8(sure_fg)
unknown = cv.subtract(sure_bg, sure_fg)
# cv.imshow('origion img', img)
cv.imshow('opening', opening)
# cv.imshow('gray_img', gray_img)
cv.imshow('thresh', thresh)
cv.imshow('dist_transform', dist_transform)
cv.imshow('sure_bg', sure_bg)
cv.imshow('sure_fg', sure_fg)
cv.imshow('unknown', unknown)
print(dist_transform.max())


cv.approxPolyDP()

cv.waitKey()
cv.destroyAllWindows()



