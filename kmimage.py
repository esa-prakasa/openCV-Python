#original source:
#https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_ml/py_kmeans/py_kmeans_opencv/py_kmeans_opencv.html#kmeans-opencv

import numpy as np
import cv2

#img = cv2.imread('pictures/corn0441.jpg')
img = cv2.imread('pictures/ppr.jpg')

scaleRatio = 1

height = int(img.shape[0]*scaleRatio)
width = int(img.shape[1]*scaleRatio)

newDim = (width, height)
img = cv2.resize(img, newDim, interpolation = cv2.INTER_AREA)


Z = img.reshape((-1,3))

# convert to np.float32
Z = np.float32(Z)

# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 2
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
res2 = res.reshape((img.shape))

cv2.imshow('res2',res2)
cv2.waitKey(0)
cv2.destroyAllWindows()
