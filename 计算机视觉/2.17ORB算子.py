# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread(r"F:\CSDN\Image\left.jpeg")
img2 = cv.imread(r"F:\CSDN\Image\right.jpeg")

# orb算子
orb = cv.ORB_create()
kp1 = orb.detect(img1, None)
kp2 = orb.detect(img2, None)
kp1, des1 = orb.compute(img1, kp1)
kp2, des2 = orb.compute(img2, kp2)
bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
matches1 = bf.match(des1, des2)
matches1 = sorted(matches1, key=lambda x: x.distance)
result = cv.drawMatches(img1, kp1, img2, kp2, matches1[:20], None, flags=2)
cv.imshow('orb', result)

cv.waitKey()
cv.destroyAllWindows()
