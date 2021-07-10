#Splitting and merging color channels

import cv2 as cv
import numpy as np

img = cv.imread('photos/scenery.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')
#Splitting
b, g, r = cv.split(img)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red', r)

#Merging the color channels
merged = cv.merge([b,g,r])
cv.imshow('Merged',merged)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue--', blue)
cv.imshow('green--', green)
cv.imshow('red--', red)


print(img.shape, b.shape, g.shape, r.shape)



cv.waitKey(0)