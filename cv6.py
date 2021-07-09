#Basic Image transformations

import cv2 as cv
import numpy as np

img = cv.imread('photos/scenery.jpg')
cv.imshow('Scenery',img)

#translation
#shiting the the images up - down - left -right
# -ve x --> shifting left
# -ve y --> Up
# +ve x --> Right
# +ve y --> Down
#
def translate(img,x,y):
    trans_mat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[0],img.shape[1])
    return cv.warpAffine(img,trans_mat,dimensions)

translated = translate(img,100,200)
cv.imshow('Translated',translated)

#Rotation

def rotate(img,angle,rotPt = None):
    (height,width)  = img.shape[:2]

    if rotPt is None:
        rotPt = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPt,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotate(img,45)
cv.imshow('Rotate',rotated)

rotated2 = rotate(rotated,45)
cv.imshow('Rotated2',rotated2)

#Resizing an image
resized  = cv.resize(img,(200,200))
cv.imshow('Resized',resized)

#Flipping an image
#0 --> flipping the image vertically
#1 --> flipping the image horizontally
#-1 --> fliiping both vertically and horizontally
flipped = cv.flip(img,-1)
cv.imshow('Flip',flipped)

cv.waitKey(0)