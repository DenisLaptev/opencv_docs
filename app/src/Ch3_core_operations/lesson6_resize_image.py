import cv2

path_to_image = '../../resources/mainlogo.png'
path_to_save_image = '../../resources/mainlogo_large.png'
image = cv2.imread(path_to_image)

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

cv2.imwrite(path_to_save_image, resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
