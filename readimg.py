# This code is used to read a file image. The image is stored as img variable. The image is then resized according to the ratio. 
# The ratio should be a positive number. If the ratio value less than 1, then the resized image will be smaller than its original size.

import numpy as np
import cv2
img = cv2.imread("fileName.jpg",1)

scRatio = 0.2
img2 = cv2.resize(img, None, fx =scRatio, fy = scRatio, interpolation = cv2.INTER_CUBIC)

cv2.imshow('Smaller image',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

