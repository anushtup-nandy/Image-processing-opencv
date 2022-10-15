import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img=cv.imread('OpenCV\Photos\park.jpg')
cv.imshow('Park', img)
# plt.imshow(img)
# plt.show()

#BGR to gray scale:
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('gray', gray)

#BGR to HSV (hue saturation value)
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#BGR to L*a*b
lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('L*a*b', lab)

#BGR to RGB
rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb version', rgb)



cv.waitKey(0)