#Thresholding i.e binarizing image i.e where pixels are either 0 or 255

import cv2 as cv
import numpy as np

img = cv.imread('photos/scenery.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
#Simple Thresholding

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('thresholded image',thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('thresholded inverse image', thresh_inv)

#Adaptive Thresholding

adaptive_thres = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 13, 7)
cv.imshow('Adaptive Thresh', adaptive_thres)

cv.waitKey(0)