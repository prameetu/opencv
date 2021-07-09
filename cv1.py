#Reading image from opencv

import cv2 as cv

img = cv.imread('photos/dog-large.jpg')

cv.imshow('Dog',img)

cv.waitKey(0)