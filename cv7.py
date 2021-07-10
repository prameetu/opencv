#Detecting contours in opencv

import cv2 as cv
import numpy as np

#2 ways of finding contours in img
img = cv.imread('photos/scenery.jpg')

blank = np.zeros(img.shape,dtype='uint8') #Creating a blank image
#cv.imshow('Blank', blank)

#Find grayscale blur and edges of the img and pass it in into find contours
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

edges = cv.Canny(blur, 125, 175)
#cv.imshow('Scenery', img)
#cv.imshow('Scenery_GRAY', gray)
cv.imshow('Edges', edges)

#2nd way is to to use threshold which binarizes image acc to pixels
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow("Thresh",thresh)

contours, heirarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1,)
cv.imshow('Contours', blank)
cv.waitKey(0)