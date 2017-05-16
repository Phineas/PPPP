import cv2
import sys
import numpy as np

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
aPF = 0.0
lAvg = 1
threshold=200
video_capture = cv2.VideoCapture('/home/still/Downloads/video4.mp4')
#fgbg = cv2.BackgroundSubtractorMOG()
fgbg = cv2.BackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
BG_frame = None
#Reads from video capture device with 
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    #turning the colour frame into grey scale
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    if BG_frame==None:
        BG_frame=imgray
        continue

    fgmask = fgbg.apply(imgray)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Video',fgmask)
#    cv2.imshow('Video2',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

