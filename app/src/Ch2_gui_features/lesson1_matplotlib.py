import numpy as np
import cv2
from matplotlib import pyplot as plt

PATH_TO_IMAGE = '../../resources/mainlogo.png'
# image = cv2.imread(path_to_image, 0)
image = cv2.imread(PATH_TO_IMAGE)
# image2 = image[:,:,::-1]
image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# plt.imshow(image, cmap='gray', interpolation='bicubic')
# plt.imshow(image, interpolation='bicubic')
plt.imshow(image2, interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()
