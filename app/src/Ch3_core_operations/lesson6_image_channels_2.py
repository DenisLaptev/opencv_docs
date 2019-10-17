import cv2
import numpy as np

PATH_TO_IMAGE = '../../resources/mainlogo_large.png'
image = cv2.imread(PATH_TO_IMAGE)

b, g, r = cv2.split(image)

cv2.imshow('image', image)
cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)

# make all the green pixels to zero
image[:, :, 1] = 0

# merge to one image
img = cv2.merge((b, g, r))

cv2.imshow('image_new', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
