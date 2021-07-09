#Changing resoultion and rescaling frame
import cv2 as cv

def changeRes(width,height): #works for live videos only
    capture.set(3,width)
    capture.set(4,height)

def rescaleFrame(frame,scale=0.75):     #works for both video and photos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)

    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


img = cv.imread('photos/dog-large.jpg')
resized_img = rescaleFrame(img)
cv.imshow('Dog',img)
cv.imshow('Dog-resized',resized_img)



capture = cv.VideoCapture('videos/dog-video.mp4')

while True:
    isTrue, frame  =  capture.read()

    frame_resize = rescaleFrame(frame,0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video_resized', frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()
