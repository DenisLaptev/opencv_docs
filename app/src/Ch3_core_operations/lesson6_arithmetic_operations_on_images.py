import cv2
import numpy as np

PATH_TO_IMAGE = '../../resources/img2.jpg'
image = cv2.imread(PATH_TO_IMAGE)
image_copy = image.copy()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', image)

image_add = cv2.add(image,image_copy)
image_plus = image+image_copy
image_delta = image_add-image_plus

cv2.namedWindow('image_add', cv2.WINDOW_NORMAL)
cv2.imshow('image_add', image_add)

cv2.namedWindow('image_plus', cv2.WINDOW_NORMAL)
cv2.imshow('image_plus', image_plus)

cv2.namedWindow('image_delta', cv2.WINDOW_NORMAL)
cv2.imshow('image_delta', image_delta)

cv2.waitKey(0)
cv2.destroyAllWindows()