#!/usr/bin/python

import cv2
import sys

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
aPF = 0.0
lAvg = 1

video_capture = cv2.VideoCapture(0)

#Reads from video capture device with 
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
    
    # Draw a rectangle around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        

    # Display the resulting frame
    cv2.imshow('Video', frame)
   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    lAvg = len(faces)
    if(lAvg != 0):
        aPF = (aPF +lAvg) / 2


    print("No. of faces: " + str(lAvg)  + " faces")
    print("Avg. No. of faces: " + str(aPF)+ " faces")
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
print "Average = " + str(apF)
