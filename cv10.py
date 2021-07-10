#Blurring and Smoothing the images
import cv2 as cv
import numpy as np

img = cv.imread('photos/kittens.jpg')
cv.imshow('Img', img)

#Averaging method of blurring
avg = cv.blur(img, (3, 3))
cv.imshow('Avg Blur', avg)

#Gaussian method of Blurring

gaussian_blur = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow('Gaussian Blur', gaussian_blur)

#Median Blurring

median_blur = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median_blur)

#Bilateral Blurring --- most effective blurring
#because it applies blurring and also retains edges
#d: Diameter of each pixel neighborhood.
#sigmaColor: The greater the value, the colors farther to each other will start to get mixed.
#sigmaSpace: The greater its value, the more further pixels will mix together, given that their colors lie within the sigmaColor range.
bilateral_blur = cv.bilateralFilter(img, d=10, sigmaColor=75, sigmaSpace=75)
cv.imshow('Bilateral Blur', bilateral_blur)

cv.waitKey(0)
