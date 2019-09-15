# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np

img = cv.imread(r"F:\CSDN\Image\sudoku.png")
cv.imshow('origin', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150)
cv.imshow('edges image', edges)

# h霍夫变换
lines = cv.HoughLines(edges, rho=1, theta=np.pi / 100, threshold=200)
print(lines.shape)
print(lines)
for i in range(lines.shape[0]):
    for rho, theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))

        cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv.imshow('img', img)

cv.waitKey()
cv.destroyAllWindows()
