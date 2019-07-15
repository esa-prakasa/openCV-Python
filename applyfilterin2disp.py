from matplotlib import pyplot as plt
import numpy as np
import cv2


# read the image which is stored in the same folder with the code
imgRGB = cv2.imread('pictures/corn0441.jpg')

scaleRatio = 0.1

height = int(imgRGB.shape[0]*scaleRatio)
width = int(imgRGB.shape[1]*scaleRatio)

newDim = (width, height)
imgRGB = cv2.resize(imgRGB, newDim, interpolation = cv2.INTER_AREA)


# fSz is the filter size. The size should be an ood number.
fSz = 15

# creating the filter
filt = np.ones((fSz,fSz),np.float32)/(fSz*fSz)
dstRGB = cv2.filter2D(imgRGB,-1, filt)

#The images will be displayed in two separated windows using OpenCV funstions
cv2.imshow('Original',imgRGB)
cv2.imshow('Filtered',dstRGB)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
 



# read the image which is stored in the same folder with the code
imgBGR = cv2.imread('pictures/corn0441.jpg')[:,:,::-1]

height = int(imgBGR.shape[0]*scaleRatio)
width = int(imgBGR.shape[1]*scaleRatio)

newDim = (width, height)
imgBGR = cv2.resize(imgBGR, newDim, interpolation = cv2.INTER_AREA)

# fSz is the filter size. The size should be an ood number.
fSz = 15

# creating the filter
filt = np.ones((fSz,fSz),np.float32)/(fSz*fSz)
dstBGR = cv2.filter2D(imgBGR,-1, filt)

#The images will be displayed in a single windows using matlotlib
plt.subplot(121),plt.imshow(imgBGR),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dstBGR),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

