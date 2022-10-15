from logging import captureWarnings
import cv2 as cv

#reading images

img= cv.imread('OpenCV\Photos\cat.jpg')
img2=cv.imread('OpenCV\Photos\cat_large.jpg')

cv.imshow('cat', img)
cv.imshow('catLarge',img2)

cv.waitKey(0)
'''

#reading videos

capture= cv.VideoCapture('OpenCV\Videos\dog.mp4')

while(True):
    isTrue, frame=capture.read()
    cv.imshow('Video', frame)

    if (cv.waitKey(20) & 0xFF==ord('d')):
        break

capture.release()
cv.destroyAllWindows()
'''

