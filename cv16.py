#Gradients and Edges

import cv2 as cv
import numpy as np

img = cv.imread('photos/boston.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Lap', lap)

#Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx,sobely)
#cv.imshow('sobel_x',sobelx)
#cv.imshow('sobel_y',sobely)
cv.imshow('Combined',combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)