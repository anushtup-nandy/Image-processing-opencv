from calendar import c
import cv2 as cv
import numpy as np

img=cv.imread('OpenCV\Photos\lady.jpg')
cv.imshow("Lady", img)

#1. Translation
def translate(img, x, y):
    #x and y are pixels, where conventional coordinates are applicable.
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1], img.shape[0]) #1 width, 0 height->tuple
    return cv.warpAffine(img, transMat, dimensions)

translated=translate(img, 100, 100)

cv.imshow('Translated', translated)


#2. Rotation:

def rotate(img, angle, rotPoint=None):
    (height, width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)

    rotMat=cv.getRotationMatrix2D(rotPoint, angle, 1.0) #scaling is 1.0 since we don't know it yet.
    dimensions=(height,width)
    return cv.warpAffine(img, rotMat, dimensions) 

rotated=rotate(img, 45, (img.shape[0]//3,img.shape[1]//4))
cv.imshow("Rotated", rotated )

#3. Flipping
flip_vert=cv.flip(img, 0)
flip_hor=cv.flip(img, 1)
flip_mirror=cv.flip(img, -1)

cv.imshow("Vertical flipping", flip_vert)
cv.imshow("horizontal flipping", flip_hor)
cv.imshow("Mirror image", flip_mirror)
cv.waitKey(0)
