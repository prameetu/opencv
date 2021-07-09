#Drawing shapes and putting texts on image

import cv2 as cv
import numpy as np

img = cv.imread('photos/dog.jpg')
cv.imshow('Dog',img)

#Paint the image certain color

img[100:200,200:256] =255,0,0
cv.imshow('Blue',img)

img[:] =0,255,0
cv.imshow('Green',img)

img[:] =0,0,255
cv.imshow('Red',img)

#Draw a rectangle
cv.rectangle(img,(0,0),(250,150),(0,255,0),thickness=-1)
cv.imshow('Rectange',img)

img = cv.imread('photos/dog.jpg')
cv.imshow('Dog',img)

#Draw a circle
cv.circle(img,(img.shape[0]//2,img.shape[1]//2),50,(255,0,0),thickness=3)
cv.imshow('Circle',img)

#Draw a line
cv.line(img,(0,0),(img.shape[0]//2,img.shape[1]//2),(255,0,0),thickness=2)
cv.imshow('Line',img)

#Writing text on image
cv.putText(img,'Hello',(img.shape[0]//2,img.shape[1]//2),fontFace=cv.FONT_HERSHEY_TRIPLEX,fontScale=1.0,color=(0,255,0),thickness=2)
cv.imshow('Text',img)

cv.waitKey(0)
