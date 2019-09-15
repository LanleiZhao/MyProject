# -*- coding:utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread(r"F:\CSDN\Image\home.jpg")

# initate star detector
orb = cv.ORB_create(scoreType=cv.ORB_FAST_SCORE)

# find the keypoints with ORB
kp = orb.detect(img)

# cumpute the descriptors with ORB
kp, des = orb.compute(img, kp)

# draw only keypoints location, not size and orientation
img2 = cv.drawKeypoints(img, kp, None, (0, 255, 0), 0)
plt.imshow(img2)
plt.show()
