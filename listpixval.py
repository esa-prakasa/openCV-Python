import cv2

img = cv2.imread("block.jpg",0)

for i in range (25,35):
	for j in range (1,2):
		pixel = img[i,j]
		print(str(i)+" "+str(j)+" "+str(pixel))
