import cv2 as cv

img = cv.imread('photos/scenery.jpg')
cv.imshow('Scenery',img)
#Converting image into greyscale

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Greyscale',gray)

#Blurring the images
blur = cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#Edge Cascade
edge = cv.Canny(img,125,175,)
cv.imshow('Canny Edges',edge)
#Edges can be reduced by using the blurred images

#Dilating the images
dilated = cv.dilate(edge,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

#Eroding the images
eroded = cv.erode(dilated ,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

#Resizing images

resized_img = cv.resize(img,(200,200),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized_img)

#Cropping images

cropped_img  = img[50:200,200:300]
cv.imshow('Cropped',cropped_img)


cv.waitKey(0)