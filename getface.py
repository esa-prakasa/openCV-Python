#from picamera.array import PiRGBArray
#from picamera import PiCamera
import cv2
import numpy as np

# Load a cascade file for detecting faces

#img = cv2.imread("C:\\Users\\Esa\\Documents\\a1OpenCVcodes\\data\\fam.jpg",1)
#img = cv2.imread("C:\\Users\\Esa\\Documents\\a1OpenCVcodes\\data\\comvis2.jpg",1)
img = cv2.imread("C:\\Users\\Esa\\Documents\\a1OpenCVcodes\\data\\fam2.jpg",1)


def getSmallerSize(img):
	scRatio = 0.9
	newRow = int(img.shape[1]*scRatio)
	newCol = int(img.shape[0]*scRatio)
	img = cv2.resize(img,(newRow, newCol) , interpolation = cv2.INTER_AREA)
	return img



img = getSmallerSize(img)
#cv2.imshow("Original image",img)

face_cascade = cv2.CascadeClassifier("C:\\Users\\Esa\\Documents\\a1OpenCVcodes\\data\\haarcascade_frontalface_default.xml");


# Convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Look for faces in the image using the loaded cascade file
faces = face_cascade.detectMultiScale(gray, 1.08, 3)
#faces = face_cascade.detectMultiScale(gray, 1.1, 3, 0, 50, 70 )
#faces = face_cascade.detectMultiScale(gray, 1.001, 8)
#cv2.imshow("Grayscale image",gray)


faceDetected = False
# Draw a rectangle around every found face
for (x,y,w,h) in faces:
	faceDetected = True
		# Create rectangle around the face
	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
		# Save the image
	cv2.imwrite("C:\\Users\\Esa\\Documents\\a1OpenCVcodes\\data\\result.jpg", img)
	


cv2.imshow("Detected face",img)


cv2.waitKey(0)
cv2.destroyAllWindows()