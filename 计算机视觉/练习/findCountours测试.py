# -*- coding:utf-8 -*-
import cv2 as cv
import copy
import numpy as np

img = cv.imread(r"F:\CSDN\Image\findContours.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 灰度转换
_,thresh= cv.threshold(gray, 0, 255 , cv.THRESH_OTSU)  # 二值化，转换为黑白图像

_,cons,hire = cv.findContours(thresh,cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # 查找边缘
# cv.drawContours(img, cons, -1, (0,0,255), 3) # 绘制边缘
rect = cv.boundingRect(cons[0])
print(rect)
print(rect[0])
print(rect[1])
print(rect[2])
print(rect[3])

# 水平包围轮廓
# for i in range(0,len(cons)):
#     x,y,w,h = cv.boundingRect(cons[i])  # 获取水平包围矩形的角点
#     cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 1)  # 绘制水平包围矩形
#     cv.line(img,(x,y),(x+w,y+h),(255,0,0),2,cv.FONT_HERSHEY_PLAIN) #绘制包围轮廓的直线
#     cv.putText(img, "area:"+str(cv.contourArea(cons[i])), (x,y), cv.FONT_HERSHEY_PLAIN, 2, (255,0,0)) # 绘制文字
#
#
# print("cons类型", type(cons))
# print("cons长度",len(cons))
# # print("cons0长度",len(cons[0]))
# # print("cons1长度",len(cons[1]))
# # print('cont0的面积',cv.contourArea(cons[0]))
# # print('cont1的面积',cv.contourArea(cons[1]))
# print(cons[0])
# print('*'*30)




cv.imshow('img', img)
cv.waitKey()
cv.destroyAllWindows()





