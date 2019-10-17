import numpy as np
import cv2

PATH_TO_SAVE_IMAGE = '../../resources/opencv_logo.png'

# Create a black image
# (y=h, x=w, number_of_channels=3)
image_black = np.zeros((512, 512, 3), np.uint8)
image_white = cv2.bitwise_not(image_black)
# cv2.imshow('black_image', image_black)
cv2.imshow('opencv_logo', image_white)
cv2.waitKey(0)

# Blue
# image1 = cv2.circle(image_white, (384, 221), 60, (255, 0, 0), -1)
# cv2.imshow('image_white_with_circle', image1)
# cv2.waitKey(0)


# Green
image3 = cv2.circle(image_white, (128, 221), 60, (0, 255, 0), -1)
cv2.imshow('opencv_logo', image3)
cv2.waitKey(0)

# Green_white
image4 = cv2.circle(image_white, (128, 221), 30, (255, 255, 255), -1)
cv2.imshow('opencv_logo', image4)
cv2.waitKey(0)

# Red
image5 = cv2.circle(image_white, (256, 70), 60, (0, 0, 255), -1)
cv2.imshow('opencv_logo', image5)
cv2.waitKey(0)

# Red_white
image6 = cv2.circle(image_white, (256, 70), 30, (255, 255, 255), -1)
cv2.imshow('opencv_logo', image6)
cv2.waitKey(0)

# White_triangle
pts_triangle = np.array([[[384, 221], [128, 221], [256, 70]]], dtype=np.int32)
image7 = cv2.fillPoly(image_white, pts_triangle, (255, 255, 255))
cv2.imshow('opencv_logo', image7)
cv2.waitKey(0)

font = cv2.FONT_HERSHEY_SIMPLEX
image8 = cv2.putText(image_white, 'OpenCV', (68, 450), font, 3, (0, 0, 0), 5, cv2.LINE_AA)
cv2.imshow('opencv_logo', image8)
cv2.waitKey(0)

image9 = cv2.ellipse(image_white, (384, 221), (60, 60), -60, 0, 300, (255, 0, 0), -1)
cv2.imshow('opencv_logo', image9)
cv2.waitKey(0)

# Blue_white
image2 = cv2.circle(image_white, (384, 221), 30, (255, 255, 255), -1)
cv2.imshow('opencv_logo', image2)
cv2.waitKey(0)

cv2.imwrite(PATH_TO_SAVE_IMAGE, image_white)

cv2.destroyAllWindows()
