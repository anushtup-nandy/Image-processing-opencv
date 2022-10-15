import cv2 as cv


img= cv.imread('OpenCV\Photos\cats.jpg')
cv.imshow("Cat", img)

#1. Converting Image to grayscale.
#gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)

#2. Basic Blurring.
#blur= cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
#cv.imshow('Blurred', blur)

#3. Edge Cascade:
canny=cv.Canny(img, 125, 175)
cv.imshow("Edge Cascaded", canny)
 
#4. Dilating the image:
dilated=cv.dilate(canny, (3,3), iterations=1)
cv.imshow("Dialated image", dilated)

#5. Eroding:
eroded=cv.erode(dilated, (3,3), iterations=3)
cv.imshow('Eroded image', eroded)

#6. Cropping:
crop=img[50:200,200:400]
cv.imshow('cropped', crop)

cv.waitKey(0)
