import cv2 as cv
file = r'F:\CSDN\Image\lena.bmp'
img = cv.imread(file)

cv.imshow('source',img)         #输出RGB图片
# cv.imshow('Blue',img[:,:,0])    #输出RGB蓝色通道
# cv.imshow('Green',img[:,:,1])   #输出RGB绿色通道
# cv.imshow('Red',img[:,:,2])     #输出RGB红色通道

# hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)     #将图片颜色模式从RGB转换为HSV
# cv.imshow('Hue',hsv[:,:,0])             #输出hsv的H通道
# cv.imshow('Saturation',hsv[:,:,1])      #输出hsv的S通道
# cv.imshow('Value',hsv[:,:,2])           #输出hsv的V通道

cv.waitKey()
cv.destroyAllWindows()


