# -*- coding:utf-8 -*-
import cv2 as cv
import numpy as np

# video_path = r"‪F:\CSDN\Image\vtest.avi"
cap = cv.VideoCapture(r"‪F:\CSDN\Image\wind.mp4")
# cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame, exiting ...")
        break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()