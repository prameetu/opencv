#Switching between color spaces
import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('photos/scenery.jpg')
cv.imshow('Scenery',img)

#plt.imshow(img)
#plt.show()

#BGR to grayscale

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR  to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

#hsv to bgr
hsv_bgr  = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR',hsv_bgr)

#lab to bgr
lab_bgr  = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB-->BGR',lab_bgr)


#plt.imshow(rgb)
#plt.show()

cv.waitKey(0)