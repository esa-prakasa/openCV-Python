from matplotlib import pyplot as plt
import cv2

# read a RGB image
img = cv2.imread('3044.jpg')

# convert its colour map, from RGB to grayscale.
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# display the result
plt.imshow(gray,cmap = plt.cm.gray)
plt.title('Wood Surface')
plt.show()
