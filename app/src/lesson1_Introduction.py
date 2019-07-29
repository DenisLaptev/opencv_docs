import cv2
import numpy as np

print(cv2.__version__)


path_to_image = '../resources/mainlogo.png'
image = cv2.imread(path_to_image,0)

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.namedWindow('named_window_image', cv2.WINDOW_NORMAL)
cv2.imshow('named_window_image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()