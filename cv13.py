#Computing Histograms for determing the pixel intensities in the image

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('photos/people.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')

circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', mask)

cv.imshow('Gray', gray)

#grayscale Histogram
gray_hist = cv.calcHist([gray], [0], mask=mask, histSize=[256], ranges=[0, 256],)
plt.figure()
plt.title('GrayScale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.show()

#RGB histogram
#on cv-14.py



cv.waitKey(0)