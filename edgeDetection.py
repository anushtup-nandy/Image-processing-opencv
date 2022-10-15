import cv2 as cv
import numpy as np

img=cv.imread('OpenCV\Photos\group 1.jpg')
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#LAPLACIAN:
lap=cv.Laplacian(gray, ddepth=cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('laplacian', lap)

#SOBEL:
sobelx=cv.Sobel(gray, cv.CV_64F, 1,0)
sobely=cv.Sobel(gray, cv.CV_64F, 0,1)
cv.imshow('Sobelx', sobelx)
cv.imshow('Sobely', sobely)

combined_sobel=cv.bitwise_or(sobelx,sobely)
cv.imshow('combined sobel', combined_sobel)

cv.waitKey(0)