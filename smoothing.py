import cv2 as cv
import numpy as np

img=cv.imread('OpenCV\Photos\cats 2.jpg')

#AVERAGING:
average=cv.blur(img, (7,7))
cv.imshow("average", average)

#GAUSSIAN:
gauss=cv.GaussianBlur(img, (7,7), sigmaX=0)
cv.imshow("Gaussian", gauss)

#MEDIAN:
median=cv.medianBlur(img,3)
cv.imshow("median", median)

#BILATERAL:
bilateral=cv.bilateralFilter(img, 5, sigmaColor=15, sigmaSpace=15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)