import cv2
import numpy as np


def nothing(x):
    pass


# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(image, (x, y), radius, (b, g, r), -1)


# Create palette, a window
palette = np.zeros((100, 500, 3), np.uint8)
cv2.namedWindow('palette')

# Create a black image, a window and bind the function to window
image = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

# create trackbars for color change
cv2.createTrackbar('R', 'palette', 0, 255, nothing)
cv2.createTrackbar('G', 'palette', 0, 255, nothing)
cv2.createTrackbar('B', 'palette', 0, 255, nothing)

# create trackbar for circle Radius
cv2.createTrackbar('Radius', 'palette', 0, 100, nothing)

while (1):
    cv2.imshow('palette', palette)
    cv2.imshow('image', image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R', 'palette')
    g = cv2.getTrackbarPos('G', 'palette')
    b = cv2.getTrackbarPos('B', 'palette')
    radius = cv2.getTrackbarPos('Radius', 'palette')

    palette[:] = [b, g, r]

cv2.destroyAllWindows()
