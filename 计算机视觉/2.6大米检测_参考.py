import cv2 as cv
import copy
import numpy as np

img = cv.imread(r"F:\CSDN\Image\rice_grain.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
bw1 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 25, -3)
element = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
bw = cv.morphologyEx(bw1, cv.MORPH_OPEN, element)

seg = copy.deepcopy(bw)
bin, cnts, hier = cv.findContours(seg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
count = 0
areas = []
lenss = []
for i in range(0, len(cnts)):
    c = cnts[i]
    area = cv.contourArea(c)
    if area < 10:
        continue
    count = count + 1
    areas.append(area)
    print(f'blob {i} = {area}')
    lens = cv.arcLength(c, True)
    lenss.append(lens)
    print(f'lens {i} = {lens:.2f}')

    rect = cv.minAreaRect(c)
    box = cv.boxPoints(rect)
    for j in range(0, 4):
        cv.line(img, tuple(box[j]), tuple(box[(j + 1) % 4]), (0, 0, 255))
    cv.putText(img, str(count), tuple(box[1]), cv.FONT_HERSHEY_PLAIN, 0.5, (0, 0xff, 0))
    a = cv.fitEllipse(c)
    cv.ellipse(img, a, (255, 255, 255))

print(f'米粒数量: {count}')
print(f'面积的均值: {np.mean(areas):.2f}, 方差: {np.var(areas):.2f}')
print(f'长度的均值: {np.mean(lenss):.2f}, 方差: {np.var(lenss):.2f}')
cv.imshow('source', img)
cv.imshow('bw', bw)
cv.imshow('adt', bw1)
cv.waitKey(0)
cv.destroyAllWindows()
