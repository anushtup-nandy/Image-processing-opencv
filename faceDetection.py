import cv2 as cv
from cv2 import SparsePyrLKOpticalFlow_create
import numpy as np
from scipy.misc import face

img=cv.imread('OpenCV\Photos\lady.jpg')

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haar_cascade=cv.CascadeClassifier('haar_cascade.xml')

faces_rect=haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print('number of faces found :', len(faces_rect))