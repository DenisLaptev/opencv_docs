import cv2
import numpy as np
from matplotlib import pyplot as plt

PATH_TO_IMAGE = '../../../resources/mainlogo.png'
img = cv2.imread(PATH_TO_IMAGE, 0)

# hist is a 256x1 array,
# each value corresponds to number of pixels in that image
# with its corresponding pixel value
hist = cv2.calcHist(images=[img],
                    channels=[0],
                    mask=None,
                    histSize=[256],
                    ranges=[0, 256])
cv2.imshow('hist', hist)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread(PATH_TO_IMAGE)
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
    plt.ylim([0, 1000])
plt.show()
