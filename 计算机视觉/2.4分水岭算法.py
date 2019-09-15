# -*- coding:utf-8 -*-
import cv2 as cv

file_path = r"F:\CSDN\Image\coins.jpg"
img = cv.imread(file_path)
cv.imshow('original image', img)

markers = cv.watershed(img, markers=None)
cv.imshow('watershed',markers)


cv.waitKey()
cv.destroyAllWindows()
