# -*- coding:utf-8 -*-
import cv2 as cv
import copy
import numpy as np

"""
检测图中所有面积>50的米粒
"""

# 图像采集
file_path = r"F:\CSDN\Image\rice_grain.jpg"
imgRice = cv.imread(file_path)
cv.imshow('Original', imgRice)

imgRiceGray = cv.cvtColor(imgRice, cv.COLOR_BGR2GRAY)
# thresh = cv.adaptiveThreshold(imgRiceGray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 101, 1)
# _,thresh = cv.threshold(imgRiceGray,120,255,cv.THRESH_BINARY)
_,thresh = cv.threshold(imgRiceGray,0,255,cv.THRESH_OTSU)
# cv.imshow('thresh', thresh)
# cv.waitKey()
element = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
dst = cv.morphologyEx(thresh, cv.MORPH_OPEN, element)
# cv.imshow('dst', dst)

img_copy = copy.deepcopy(dst)  # 深拷贝一份
_, contours, hierarchy = cv.findContours(img_copy, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)  # 查找轮廓
cv.drawContours(imgRice, contours, -1, (0, 0, 255), 1)
print(len(contours))  # 轮廓的数量
cv.imshow('img_draw_contours', imgRice)

count = 0  # 米粒数量
area_list = []  # 定义一个列表，存储每个米粒的面积
length_list = []  # 定义一个列表，存储每个米粒的长度
# for i in range(0, len(contours)):
for cont in contours:
    area = cv.contourArea(cont)  # 每个米粒的面积
    if area < 50:
        continue
    count += 1  # 计数器
    area_list.append(area)
    # print("第{}米的面积是{}".format(count,area),end='\n')

    # 绘制外围矩形
    rect = cv.boundingRect(cont)  # 提取每粒米的外围矩形，返回第一个点，长，宽，x y w h
    length = max(rect[2], rect[3])  # 米粒的长度
    length_list.append(length)
    print("第{}粒米的面积={},长度={}".format(count, area, length), end='\n')
    cv.rectangle(imgRice, (rect[0], rect[1]), (rect[0] + rect[2], rect[1] + rect[3]), (0, 255, 0), 1)
    cv.putText(imgRice, str(count), (rect[0], rect[1]), cv.FONT_HERSHEY_PLAIN, 0.4, (255, 0, 0), 1)
    cv.imshow('result', imgRice)
print("------分割线---------------")
# # 米粒的平均面积
# # print("米粒的平均面积={}".format(round(sum(area_list)/count),2))
# print("米粒的平均面积={}".format(round(np.mean(area_list),2)))
# # 米粒面积的方差
# print("米粒面积的方差={}".format(round(np.var(area_list),2)))
# # 米粒面积的标准差
# print("米粒面积的标准差={}".format(np.std(area_list)))
# # 米粒的平均长度
# # print("米粒的平均长度={}".format(round(sum(length_list)/count),2))
# print("米粒的平均长度={}".format(round(np.mean(length_list),2)))
# #米粒长度的方差
# print("米粒长度的方差={}".format(round(np.var(length_list),2)))
# # 米粒长度的标准差
# print("米粒长度的标准差={}".format(np.str(area_list)))

print("面积小于50的米粒数量为：{}".format(count))
print(f"米粒的面积均值:{np.mean(area_list):.2f}, 方差:{np.var(area_list):.2f}, 标准差:{np.std(area_list):.2f}")
print(f"米粒的长度均值：{np.mean(length_list):.2f}, 方差:{np.var(length_list):.2f}, 标准差:{np.std(length_list):.2f}")

# 统计面积落在3sigma以内的米粒数
area_in_3sigma = 0
for area in area_list:
    if area >= np.mean(area_list)-3*np.std(area_list) and  area <= np.mean(area_list)+ 3* np.std(area_list):
        area_in_3sigma += 1
print("面积落在3sigma以内的米粒数={}".format(area_in_3sigma))

# 统计长度落在3sigma以内的米粒数
length_in_3sigma = 0
for length in length_list:
    if length >= np.mean(length_list)-3*np.std(length_list) and length<= np.mean(length_list)+3*np.std(length_list):
        length_in_3sigma += 1
print("长度落在3sigma以内的米粒数={}".format(length_in_3sigma))


cv.waitKey()
cv.destroyAllWindows()
