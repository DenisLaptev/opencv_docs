import cv2
import numpy as np
from matplotlib import pyplot as plt

PATH_TO_IMAGE = '../../resources/mainlogo.png'

img = cv2.imread(PATH_TO_IMAGE, 0)
img = cv2.medianBlur(img, 5)

ret, th1 = cv2.threshold(src=img,
                         thresh=127,
                         maxval=255,
                         type=cv2.THRESH_BINARY)

th2 = cv2.adaptiveThreshold(src=img,
                            maxValue=255,
                            adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,
                            thresholdType=cv2.THRESH_BINARY,
                            blockSize=11,
                            C=2)

th3 = cv2.adaptiveThreshold(src=img,
                            maxValue=255,
                            adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            thresholdType=cv2.THRESH_BINARY,
                            blockSize=11,
                            C=2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
          'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]

for i in range(4):
    plt.subplot(2, 2, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
