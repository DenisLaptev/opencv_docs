import cv2
import numpy as np

print(cv2.useOptimized())

path_to_image = '../../resources/opencv_logo.png'
image = cv2.imread(path_to_image)

e1 = cv2.getTickCount()
img = cv2.medianBlur(image, 1)
e2 = cv2.getTickCount()

t = (e2 - e1) / cv2.getTickFrequency()
print(t)
