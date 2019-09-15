import cv2 as cv
filename = r'F:\CSDN\lena.bmp'
img = cv.imread(filename)

#高斯模糊
imGauss = cv.GaussianBlur(img,(5,5),0)

# image1 = cv.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
#shape[1]是宽度方向，shape[0]是长度方向

image2 = cv.pyrDown(image1)

#彩色图片转换为黑白图片
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

_,gray1 = cv.threshold(gray,120,0xff,cv.THRESH_BINARY)

cv.imshow('source image',img)
# cv.imshow('Guassian Blur',imGauss)
# cv.imshow('half size',image1)
cv.imshow('quarter size',image2)
cv.imshow('gray',gray)
cv.imshow('Threshold image',gray1)
cv.waitKey()
cv.destroyAllWindows()
