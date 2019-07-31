import numpy as np
import cv2

# Create a black image
# (y=h, x=w, number_of_channels=3)
image = np.zeros((512, 1000, 3), np.uint8)
cv2.imshow('black_image', image)
cv2.waitKey(0)

# Draw a diagonal blue line with thickness of 5 px
image1 = cv2.line(image, (0, 0), (511, 511), (255, 0, 0), 5)
cv2.imshow('black_image_with_line', image1)
cv2.waitKey(0)

image2 = cv2.rectangle(image, (384, 0), (510, 128), (0, 255, 0), 3)
cv2.imshow('black_image_with_rectangle', image2)
cv2.waitKey(0)

image3 = cv2.circle(image, (447, 63), 63, (0, 0, 255), -1)
cv2.imshow('black_image_with_circle', image3)
cv2.waitKey(0)

image4 = cv2.ellipse(image, (256, 256), (100, 50), 0, 0, 180, 255, -1)
cv2.imshow('black_image_with_ellipse', image4)
cv2.waitKey(0)

pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
image5 = cv2.polylines(image, [pts], True, (0, 255, 255))
cv2.imshow('black_image_with_polylines_closed', image5)
cv2.waitKey(0)

pts = np.array([[1, 50], [120, 30], [7, 2], [15, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
image6 = cv2.polylines(image, [pts], False, (0, 255, 0), 5)
cv2.imshow('black_image_with_polylines_unclosed', image6)
cv2.waitKey(0)

pts_square = np.array([[[10, 10], [100, 10], [100, 100], [10, 100]]], dtype=np.int32)
image_black = np.zeros([240, 320], dtype=np.uint8)
image7 = cv2.fillPoly(image_black, pts_square, 255)
cv2.imshow('black_image_with_fillPoly', image7)
cv2.waitKey(0)

font = cv2.FONT_HERSHEY_SIMPLEX
image8 = cv2.putText(image, 'OpenCV', (10, 500), font, 4, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow('black_image_with_text', image8)
cv2.waitKey(0)

cv2.destroyAllWindows()
