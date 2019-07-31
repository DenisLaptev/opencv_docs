import cv2
import numpy as np

path_to_image = '../../resources/mainlogo_large.png'
image = cv2.imread(path_to_image)

b, g, r = cv2.split(image)

#other way:
blue = image[:,:,0]
green = image[:,:,1]
red = image[:,:,2]

cv2.imshow('image', image)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)

cv2.waitKey(0)
cv2.destroyAllWindows()
