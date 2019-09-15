import cv2 as cv
import copy
import numpy as np

img = cv.imread(r'E:\SSS\python practice\Rice.png')  # 读取图像，加r可仅用一个\
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 转换为灰度图，任何图像输入(即使是灰色图像，也拥有三个通道)
bw1 = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 25, -3)
# 自适应阈值分割，高于阈值设置为255白色，方法为像素邻域加权和减去常量C，二进制阈值类型，邻域大小一般设置较大，此处25，C为-20
element = cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
# 建立形态学运算结构元素，此处为5*5十字形
bw = cv.morphologyEx(bw1, cv.MORPH_OPEN, element)  # 通过形态学开运算

seg = copy.deepcopy(bw)  # 将上一步得到的结果进行深度复制，即拷贝矩阵所有信息
bin, cnts, hier = cv.findContours(seg, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# 查找轮廓，此处仅查找最外层轮廓，检测出的轮廓仅保留终点坐标，压缩水平方向，垂直方向，对角线方向的元素
count = 0  # 建立计数器
areas = []  # 创建储存面积与长度的列表
lenss = []
for i in range(0, len(cnts)):
    c = cnts[i]
    area = cv.contourArea(c)  # 计算轮廓面积
    if area < 10:  # 若面积小于10，则判定为噪声去除
        continue
    elif area > 300:  # 若面积大于300，则米粒粘合，去除
        continue
    count = count + 1  # 若大于10，使计数器加1
    areas.append(area)  # 在面积列表末尾插入新元素
    print(f'blob {i} 面积= {area}')

    rect = cv.minAreaRect(c)
    # 计算最小包围矩形，返回最小外接矩形的（中心(x,y), (宽,高), 旋转角度）
    box = cv.boxPoints(rect)  # 获取最小外接矩形的4个顶点
    for j in range(0, 4):  # 设置循环将四个点连起来
        cv.line(img, tuple(box[j]), tuple(box[(j + 1) % 4]), (0, 0, 255))
    a1 = np.linalg.norm(np.array(box[0]) - np.array(box[1]))  # 判断出最小外接矩形的长边，作为米粒的长度
    a2 = np.linalg.norm(np.array(box[0]) - np.array(box[3]))
    if a1 > a2:
        lenss.append(a1)
        print(f'lens {i} = {a1:.2f}')
    else:
        lenss.append(a2)
        print(f'lens {i} = {a2:.2f}')
    cv.putText(img, str(count), tuple(box[1]), cv.FONT_HERSHEY_PLAIN, 0.5, (0, 0xff, 0))
    # 添加文本框，（图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细）
    a = cv.fitEllipse(c)  # 根据轮廓计算最佳拟合椭圆
    cv.ellipse(img, a, (255, 255, 255))  # 绘制拟合椭圆，最后一个参数为颜色

print(f'米粒数量: {count}')
print(f'面积的均值: {np.mean(areas):.2f}, 方差: {np.var(areas):.2f}, 标准差:{np.std(areas):.2f}')
print(f'长度的均值: {np.mean(lenss):.2f}, 方差: {np.var(lenss):.2f}, 标准差:{np.std(lenss):.2f}')
cv.imshow('source', img)
cv.imshow('bw', bw)
cv.imshow('adt', bw1)
cv.waitKey(0)
cv.destroyAllWindows()
