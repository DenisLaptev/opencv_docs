import cv2
import numpy as np

# flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
# print(flags)
# print(len(flags))

cap = cv2.VideoCapture(0)

while (1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    blue_color = np.uint8([[[255, 0, 0]]])
    hsv_blue = cv2.cvtColor(blue_color, cv2.COLOR_BGR2HSV)
    print(hsv_blue)
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([140, 255, 255])

    # define range of green color in HSV
    green_color = np.uint8([[[0, 255, 0]]])
    hsv_green = cv2.cvtColor(green_color, cv2.COLOR_BGR2HSV)
    print(hsv_green)
    lower_green = np.array([30, 10, 10])
    upper_green = np.array([90, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Threshold the HSV image to get only blue and green colors
    mask_b = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_g = cv2.inRange(hsv, lower_green, upper_green)
    mask_b_and_g = cv2.add(mask_b, mask_g)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame, frame, mask=mask)
    res_bg = cv2.bitwise_and(frame, frame, mask=mask_b_and_g)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)  # extract blue objects
    cv2.imshow('res_bg', res_bg)  # extract blue and green objects
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
