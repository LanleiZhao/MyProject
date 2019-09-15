import cv2


img = cv2.imread(r'F:\CSDN\lena.bmp')
# img = cv2.imread(r'‪C:\Users\Lucas\Desktop\lena.bmp')
# print(img)
cv2.namedWindow('wwindow', 1)
# cv2.imshow('hello,world', img)
cv2.imshow('wwindow', img)
# cv2.imwrite('0822.jpg', img)
cv2.waitKey()
cv2.destroyAllWindows()


