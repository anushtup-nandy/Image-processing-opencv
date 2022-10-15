import cv2 as cv
from cv2 import THRESH_BINARY_INV
import numpy as np

img=cv.imread('OpenCV\Photos\cats.jpg')

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#SIMPLE THRESHOLDING:
threshold, thresh= cv.threshold(gray, 150, 255, cv.THRESH_BINARY) 
threshold, thresh_inv= cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple threshold', thresh)
#cv.imshow('gray', gray)
cv.imshow('Simple threshold inv', thresh_inv)


#ADAPTIVE THRESHOLDING:
adaptive_thresh=cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)

cv.imshow('Adaptive show', adaptive_thresh)


adaptive_thresh_gauss=cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)

cv.imshow('Adaptive show', adaptive_thresh_gauss)

cv.waitKey(0)