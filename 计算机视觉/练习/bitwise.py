# -*- coding:utf-8 -*-
import cv2 as cv

logo_path = r"F:\CSDN\Image\logo.png"
lena_path = r"F:\CSDN\Image\lena.bmp"

logo = cv.imread(logo_path)
lena = cv.imread(lena_path)
# print(lena.shape)
# print(logo.shape)
# I want to put logo on top-left corner,SO I create a ROI
rows,cols,channels = logo.shape
roi = lena[0:rows, 0:cols]




# cv.imshow('roi',roi)
cv.waitKey()
cv.destroyAllWindows()