import cv2 as cv
import numpy as np

img=cv.imread('OpenCV\Photos\cats.jpg')
cv.imshow('Cats', img)

blank=np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

#converting to grayscale:
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray cats", gray)

#BLURRING:
blur=cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

#grabbing the edges:
canny=cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)
canny2=cv.Canny(blur, 125, 175)
cv.imshow('canny blurred', canny2)

#CONTOURS NOW:
contours1, hierarchies= cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#print(f'{len(contours1)} many contours found in normal image')

#contours2, hierarchies= cv.findContours(canny2, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
#print(f'{len(contours2)} many contours found in blurred image')

#CONTOURS METHOD 2:    does not use CANNY
ret, thresh= cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

contours3, hierarchies= cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours3)} many contours found in thresh method')

cv.drawContours(blank, contours1, -1, (0,0,255), 1)  # -1 means all, and 2 means thinckenss
cv.imshow('Contours drawn', blank)
cv.waitKey(0)