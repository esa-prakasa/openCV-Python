import cv2
from matplotlib import pyplot as plt
 
img = cv2.imread('3044.jpg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)

scaleRatio = 0.5

height = int(img.shape[0]*scaleRatio)
width = int(img.shape[1]*scaleRatio)

newDim = (width, height)
img2 = cv2.resize(img, newDim, interpolation = cv2.INTER_AREA)

plt.subplot(121),plt.imshow(img,cmap = plt.cm.gray),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img2,cmap = plt.cm.gray),plt.title('Smaller')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.imshow("Resized image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
