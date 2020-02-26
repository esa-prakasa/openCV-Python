from matplotlib import pyplot as plt
import numpy as np
import cv2

# read the image which is stored in the same folder with the code
img = cv2.imread('hello.jpg')

# fSz is the filter size. The size should be an ood number.
fSz = 21

# creating the filter
filt = np.ones((fSz,fSz),np.float32)/(fSz*fSz)
dst = cv2.filter2D(img,-1, filt)

# create several plot to show the images
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
