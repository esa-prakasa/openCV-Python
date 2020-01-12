# This code is used to mask the frame acquired from laptop webcam
# The code is written based on tutorial given by https://www.youtube.com/watch?v=yvfI4p6Wyvk

import matplotlib.pylab as plt
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('frame',frame)

    #print(frame.shape)
    height = frame.shape[0]
    width = frame.shape[1]
    #print("Height: %5d  Width: %5d "% (height, width))

    roi_vertices = [
    	(0,height),
    	(width/2-100, height/3),
    	(width/2+100, height/3),
    	(width,height)
    ]

    def get_roi(img, vertices):
    	mask  = np.zeros_like(img)
    	channel_count = img.shape[2]
    	match_mask_color = (255,) * channel_count
    	cv2.fillPoly(mask, vertices, match_mask_color)
    	masked_image = cv2.bitwise_and(img, mask)
    	return masked_image

    cropped_image = get_roi(frame, 
    				np.array([roi_vertices], np.int32),)

    cv2.imshow('frame',cropped_image)


    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
