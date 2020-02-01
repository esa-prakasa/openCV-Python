# reference: https://www.youtube.com/watch?v=1XTqE7LFQjI
# from webcam video can extract the frames
#


import cv2, time

video = cv2.VideoCapture(0)
a = 0
while True:
	a = a + 1

	check, frame = video.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#cv2.imshow("Capturing",frame)
	cv2.imshow("Capturing",frame)

	#cv2.waitKey(0)
	key = cv2.waitKey(1)

	if key == ord('q'):
		break
	print("  "+str(a))


video.release()
cv2.destroyallwindows()
