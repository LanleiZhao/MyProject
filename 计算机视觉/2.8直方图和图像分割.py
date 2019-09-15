# -*- coding:utf-8 -*-
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# file_path = r"F:\CSDN\Image\family.jpg"
file_path = r"F:\CSDN\Image\lena.bmp"
img = cv.imread(file_path, 0)

# open-cv方法，cv2.calcHist()
hist_cv = cv.calcHist([img], [0], None, [256], [0, 255])

# numpy方法读取np.histgram()
# hist_np, bins = np.histogram(img.ravel(), 256, [0, 256])
# numpy的另一种方法读取np.bincount()
# hist_np2 = np.bincount(img.ravel(), minlength=256)

plt.subplot(221)
plt.imshow(img, 'gray')

plt.subplot(223)
plt.plot(hist_cv)

# plt.subplot(223)
# plt.plot(hist_np)
#
# plt.subplot(224)
# plt.plot(hist_np2)

plt.show()

