# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np
import time

start = time.process_time()  # 计时开始
img = cv.imread(r"F:\CSDN\Image\blox.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

sift = cv.xfeatures2d.SIFT_create()  # 创建sift检测算子
kp = sift.detect(gray, None)  # 检测
img_sift = np.copy(img)  # 复制一份图像
cv.drawKeypoints(img, kp, img_sift)  # 绘制角点,img_sift是输出图像
cv.imshow('origin', img)
cv.imshow('sift image', img_sift)

end = time.process_time()
print('time elapse:', end - start)
# time elapse: 0.140625

cv.waitKey()
cv.destroyAllWindows()
