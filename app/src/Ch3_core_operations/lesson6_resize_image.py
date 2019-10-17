import cv2

PATH_TO_IMAGE = '../../resources/mainlogo.png'
PATH_TO_SAVE_IMAGE = '../../resources/mainlogo_large.png'
image = cv2.imread(PATH_TO_IMAGE)

print('Original Dimensions : ', image.shape)

scale_percent = 500  # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

print('Resized Dimensions : ', resized.shape)

cv2.imshow("Initial image", image)
cv2.imshow("Resized image", resized)

cv2.imwrite(PATH_TO_SAVE_IMAGE, resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
