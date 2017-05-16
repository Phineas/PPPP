import cv2
import sys
import numpy as np

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
aPF = 0.0
lAvg = 1
threshold=200

video_capture = cv2.VideoCapture('/home/still/Downloads/video4.mp4')
prev_frame = None
#Reads from video capture device with 
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)
    gaus_frame=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
    if prev_frame==None:
        prev_frame=gaus_frame
        continue

##    diff_frame=gray-prev_frame

    ##    for x in range(len(gray)):
    ##        for y in range(len(gray[0])):
    ##            print gray[x][y]-prev_frame[x][y]
    ##           
    ##            if gray[x][y]-prev_frame[x][y]>250:
    ##                diff_frame[x][y]=0
    ##            else:
    ##                diff_frame[x][y]=gray[x][y]-prev_frame[x][y]
    diff_frame=gaus_frame-prev_frame
    edges = cv2.Canny(gaus_frame,50,150,apertureSize = 3)

 #   prev_frame=gray
    
    minLineLength = 50
    maxLineGap =10

    #lines = cv2.HoughLines(edges,1,np.pi/180,threshold)
    lines = cv2.HoughLinesP(edges,2,np.pi/180,200,minLineLength,maxLineGap)

    if lines != None:
    
##        for rho,theta in lines[0]:
        for x1,y1,x2,y2 in lines[0]:
##            a = np.cos(theta)
##            b = np.sin(theta)
##            x0 = a*rho
##            y0 = b*rho
##            x1 = int(x0 + 1000*(-b))
##            y1 = int(y0 + 1000*(a))
##            x2 = int(x0 - 1000*(-b))
##            y2 = int(y0 - 1000*(a))
            
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
    cv2.imshow('Video', gaus_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

