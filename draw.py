import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8')
#cv.imshow('Blank', blank)
#img=cv.imread('OpenCV\Photos\cat.jpg')
#cv.imshow('Cat', img)

#1. paint the image in a certain colour:
#blank[100:300, 300:500]=0,255,0 #stands for green
#cv.imshow('Green', blank)

#2. Draw a rectangle:
cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness=2 )
#cv.imshow('Rectangle', blank)

#3. Drawing a circle:
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
#cv.imshow('Circle', blank)

#4. Drawing a line:
cv.line(blank,  (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=4)
#cv.imshow('LCR', blank)

#5. WRITE TEXT:

cv.putText(blank, "HEY this is L_C_R_T", (100,350), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.0, (255,255,255), thickness=2)
cv.imshow('ALL', blank)

cv.waitKey(0)





