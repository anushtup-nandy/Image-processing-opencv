import cv2 as cv
import numpy as np

img=cv.imread('OpenCV\Photos\group 2.jpg')
cv.imshow('group2', img)

#splitting
b,g,r=cv.split(img)
# cv.imshow('blue', b)
# cv.imshow('green', g)
# cv.imshow('red', r) 

# #checking the shapes:
# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

#merging the images:
merge=cv.merge([b,g,r])
cv.imshow('merged image', merge)

#doing the same using numpy:
blank=np.zeros(img.shape[:2], dtype='uint8')

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)


cv.waitKey(0)