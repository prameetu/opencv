#Masking -- Enables us tp focus on certain specofic position of image
import cv2 as cv
import numpy as np

img = cv.imread('photos/dog2.jpg')
cv.imshow('Img', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('BLank', blank)

mask = cv.circle(blank, (img.shape[1]//2 + 45, img.shape[0]//2 + 45), 200, 255, -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)
cv.waitKey(0)