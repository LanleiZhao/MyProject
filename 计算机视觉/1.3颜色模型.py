import cv2 as cv
filename = r'F:\CSDN\Image\lena.bmp'
img = cv.imread(filename)
cv.imshow('source',img)
# cv.imshow('Blue',img[:,:,0])
# cv.imshow('Green',img[:,:,1])
# cv.imshow('Red',img[:,:,2])

# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)



hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)
cv.imshow('Hue',hsv[:,:,0])
cv.imshow('Saturation',hsv[:,:,1])
cv.imshow('Value',hsv[:,:,2])

cv.waitKey()
cv.destroyAllWindows()


