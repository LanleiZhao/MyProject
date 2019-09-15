# -*- coding:utf-8 -*-
import  cv2 as cv

# file_path = r"F:\CSDN\Image\lena.bmp"
file_path = r"F:\CSDN\Image\rice_grain.jpg"
img = cv.imread(file_path)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.xfeatures2d.SIFT_create()
kp = sift.detect(gray, None)

cv.drawKeypoints(gray, kp, img)
cv.imwrite('sift_keypoints.jpg',img)
