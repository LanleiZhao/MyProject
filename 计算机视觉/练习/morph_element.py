# -*- coding:utf-8 -*-

import cv2 as cv

element1 = cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
element2 = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))


print(element1.shape)
print(element1)
print(element1.dtype)

print('*'*30)
print(element2.shape)
print(element2)
