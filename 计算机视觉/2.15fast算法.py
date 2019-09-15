# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np
import time

start = time.process_time()  # 计时开始
img = cv.imread(r"F:\CSDN\Image\blox.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

fast = cv.FastFeatureDetector_create()  # 创建fast检测算子
keypoints = fast.detect(gray)  # 检测特征点
img_fast = np.copy(img)
cv.drawKeypoints(img, keypoints, img_fast)
cv.imshow('origin', img)
cv.imshow('fast image', img_fast)

end = time.process_time()
print('time elapse:', end-start)
# time elapse: 0.03125
cv.waitKey()
cv.destroyAllWindows()
"""FAST检测的角点比SIFT要多，比较准确，耗时更少"""