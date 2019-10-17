import cv2
import numpy as np

print(cv2.useOptimized())

PATH_TO_IMAGE = '../../resources/opencv_logo.png'
image = cv2.imread(PATH_TO_IMAGE)

e1 = cv2.getTickCount()
img = cv2.medianBlur(image, 1)
e2 = cv2.getTickCount()

t = (e2 - e1) / cv2.getTickFrequency()
print(t)
