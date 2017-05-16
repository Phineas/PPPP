import cv2
import sys
import numpy as np

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
aPF = 0.0
lAvg = 1
threshold=200

video_capture = cv2.VideoCapture('/home/still/Downloads/video4.mp4')
BG_frame = None
#Reads from video capture device with 
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    #turning the colour frame into grey scale
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ##ret, thresh = cv2.threshold(imgray, 50, 150, 0)


    thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,2)
    #im2, contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    ##cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    cv2.imshow('Video', thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

