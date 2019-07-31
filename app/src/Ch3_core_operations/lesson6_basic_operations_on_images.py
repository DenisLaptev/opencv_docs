import cv2
import numpy as np

path_to_image = '../../resources/mainlogo.png'
image = cv2.imread(path_to_image)

str_delimeter = '--------------------------------------------------'

px = image[60, 120]
print(px)

# ----------------------ACCESS using px---------------------------
# accessing only blue pixel
px_blue = image[60, 120, 0]
print(px_blue)

# accessing only green pixel
px_green = image[60, 120, 1]
print(px_green)

# accessing only red pixel
px_red = image[60, 120, 2]
print(px_red)

# ----------------------SET px---------------------------
print(str_delimeter)

image[60, 120] = [0, 0, 0]
print(image[60, 120])

# Numpy is a optimized library for fast array calculations.
# So simply accessing each and every pixel values and
# modifying it will be very slow and it is discouraged.
#
# For individual pixel access, Numpy array methods, array.item()
# and array.itemset() is considered to be better.
# But it always returns a scalar. So if you want to access all B,G,R values,
# you need to call array.item() separately for all.


# ----------------------ACCESS using numpy---------------------------
print(str_delimeter)

# accessing BLUE value
print(image.item(61, 120, 0))

# accessing GREEN value
print(image.item(61, 120, 1))

# accessing RED value
print(image.item(61, 120, 2))

# ----------------------SET using numpy---------------------------
print(str_delimeter)

# modifying RED value
print(image.item(61, 120, 2))
image.itemset((61, 120, 2), 100)
print(image.item(61, 120, 2))

# ----------------------image properties---------------------------
print(str_delimeter)

print(image.shape)
print(image.size)
print(image.dtype)

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
