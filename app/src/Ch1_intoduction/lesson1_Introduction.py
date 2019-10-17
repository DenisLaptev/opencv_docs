import cv2
import numpy as np

print(cv2.__version__)

PATH_TO_IMAGE = '../../resources/mainlogo.png'
image = cv2.imread(PATH_TO_IMAGE, 1)
#cv2.IMREAD_COLOR       #1(default)
#cv2.IMREAD_GRAYSCALE   #0
#cv2.IMREAD_UNCHANGED   #-1


cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow('named_window_image', cv2.WINDOW_NORMAL)
cv2.imshow('named_window_image', image)


cv2.waitKey(0)
cv2.destroyAllWindows()
