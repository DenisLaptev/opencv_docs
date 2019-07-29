import cv2
import numpy as np

path_to_image = '../resources/mainlogo.png'
image = cv2.imread(path_to_image, 0)

path_to_save_image = '../resources/python.png'

cv2.imshow('image', image)
k = cv2.waitKey(0)


# wait for ESC key to exit
if k == 27:
    cv2.destroyAllWindows()

# wait for 's' key to save and exit
elif k == ord('s'):
    cv2.imwrite(path_to_save_image, image)
    cv2.destroyAllWindows()
