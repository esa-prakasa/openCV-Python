
import numpy as np
import cv2

#img = cv2.imread("C:\\Users\\Esa\\Documents\\a1OpenCVcodes\\krb.jpg",1)
img = cv2.imread("C:\\Users\\Esa\\Documents\\a1OpenCVcodes\\krb3.jpg",1)
scRatio = 0.7
img = cv2.resize(img, None, fx =scRatio, fy = scRatio, interpolation = cv2.INTER_CUBIC)

height = img.shape[0]
width = img.shape[1]

hdiv2 = int(height/5)
#img = img[hdiv2:height, 0:width]

#img = cv2.GaussianBlur(img,(3,3),cv2.BORDER_DEFAULT)
img = cv2.blur(img,(3,3))


gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

edges = cv2.Canny(gray, 80,200, apertureSize=3)
lines = cv2.HoughLines(edges,1, np.pi/180,200)


cv2.imshow('Edge image',edges)

getH = 1

if getH == 1:
	for line in lines:
		rho,theta = line[0]
		a = np.cos(theta)
		b = np.sin(theta)
		x0 = a * rho
		y0 = b * rho

		x1 = int(x0 + 1000*(-b))
		y1 = int(y0 + 1000*(a))

		x2 = int(x0 - 1000*(-b))
		y2 = int(y0 - 1000*(a))

		cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
		cv2.imshow('Image',img)


cv2.waitKey(0)
cv2.destroyAllWindows()

