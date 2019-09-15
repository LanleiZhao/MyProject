# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np

# file_path = r"F:\CSDN\Image\chessboard.jpg"
file_path = r"F:\CSDN\Image\blox.jpg"

img = cv.imread(file_path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = np.float32(gray)

# the input image must be float32
dst = cv.cornerHarris(gray, blockSize=2, ksize=3, k =0.04)

# result is dilated for marking the corners
dst = cv.dilate(dst,None)

# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()] = [0,255,0]


cv.imshow('harris corner image' , img)
# cv.imshow('dst', dst)
print(dst.shape)
cv.waitKey()
cv.destroyAllWindows()

"""
https://www.cnblogs.com/DOMLX/p/8763369.html
"""













