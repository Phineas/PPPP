#!/usr/bin/python

import cv2
import sys
import numpy as np

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
aPF = 0.0
lAvg = 1
threshold=200

video_capture = cv2.VideoCapture(0)

#Reads from video capture device with 
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    edges = cv2.Canny(gray,50,150,apertureSize = 3)

    minLineLength = 1000
    maxLineGap = 100

    lines = cv2.HoughLines(edges,1,np.pi/180,threshold)
    ##lines = cv2.HoughLinesP(edges,1,np.pi/180,350,minLineLength,maxLineGap)

    if lines != None:
    
        for rho,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            
            cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
        #print "There are ", len(lines[0]), " lines."
        #print "There are ", len(edges), " edges."
        aPF = (aPF+len(lines[0]))/2
        print "The average is ", aPF
        print "Threshold = ", threshold
        if aPF<4.5:
            threshold-=1
        elif aPF>5.5:
            threshold+=1
        # Display the resulting frame
    else:
        threshold-=1
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

