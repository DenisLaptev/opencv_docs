import cv2
import numpy as np

PATH_TO_IMAGE = '../../resources/mainlogo.png'
image = cv2.imread(PATH_TO_IMAGE, 0)

PATH_TO_SAVE_IMAGE = '../../resources/python.png'

cv2.imshow('image', image)
k = cv2.waitKey(0)


# wait for ESC key to exit
if k == 27:
    cv2.destroyAllWindows()

# wait for 's' key to save and exit
elif k == ord('s'):
    cv2.imwrite(PATH_TO_SAVE_IMAGE, image)
    cv2.destroyAllWindows()
