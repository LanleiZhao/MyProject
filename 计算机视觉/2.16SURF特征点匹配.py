# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np

img1 = cv.imread(r"F:\CSDN\Image\left.jpeg")
img2 = cv.imread(r"F:\CSDN\Image\right.jpeg")
# SURF算子
minHessian = 1000
dectector = cv.xfeatures2d.SURF_create(minHessian)
descriptor = cv.xfeatures2d.SURF_create()
matcher1 = cv.DescriptorMatcher_create("BruteForce")

# 检测特征点
keypoint1 = dectector.detect(img1)
keypoint2 = dectector.detect(img2)

# 计算特征点描述子
_, descriptors1 = descriptor.compute(img1, keypoint1)
_, descriptors2 = descriptor.compute(img2, keypoint2)

# 特征匹配
matches = matcher1.match(descriptors1, descriptors2)
img_matches = np.empty(img2.shape)
img_matches1 = cv.drawMatches(img1, keypoint1, img2, keypoint2, matches, img_matches)
cv.imshow("img matches", img_matches1)
print(f"keypoint1.size={len(keypoint1)}")
print(f"keypoint2.size={len(keypoint2)}")

cv.waitKey()
cv.destroyAllWindows()
