import numpy as np
import cv2
img = cv2.imread("fileName.jpg",1)

scRatio = 0.2
img2 = cv2.resize(img, None, fx =scRatio, fy = scRatio, interpolation = cv2.INTER_CUBIC)

cv2.imshow('Smaller image',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

