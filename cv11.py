import  cv2 as  cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), 255,-1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

bit_and = cv.bitwise_and(rectangle, circle)
bit_or = cv.bitwise_or(rectangle, circle)
bit_xor = cv.bitwise_xor(rectangle, circle)
bit_not = cv.bitwise_not(circle)


cv.imshow('bit_and', bit_and)
cv.imshow('bit_or', bit_or)
cv.imshow('bit_xor', bit_xor)
cv.imshow('Circle not',bit_not)
cv.waitKey(0)