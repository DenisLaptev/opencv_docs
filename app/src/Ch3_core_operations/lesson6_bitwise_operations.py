import cv2
import numpy as np

# Load two images
PATH_TO_IMAGE1 = '../../resources/opencv_logo.png'
PATH_TO_IMAGE2 = '../../resources/mainlogo.png'

image1 = cv2.imread(PATH_TO_IMAGE1)
image2 = cv2.imread(PATH_TO_IMAGE2)

# I want to put logo on top-left corner, So I create a ROI
rows, cols, channels = image2.shape
roi = image1[0:rows, 0:cols]

# Now create a mask of python_logo and create its inverse mask also
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(image2_gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# Now black-out the area of logo in ROI
image1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# Take only region of logo from logo image.
image2_fg = cv2.bitwise_and(image2, image2, mask=mask)

# Put logo in ROI and modify the main image
dst = cv2.add(image1_bg, image2_fg)
image1[0:rows, 0:cols] = dst

cv2.imshow('res', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
