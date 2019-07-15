import numpy as np
import cv2

cap = cv2.VideoCapture('wild.avi')

# creating three types of filter dimension
fSz1 = 5
fSz2 = 15
fSz3 = 45

# creating the filters
filt1 = np.ones((fSz1,fSz1),np.float32)/(fSz1*fSz1)
filt2 = np.ones((fSz2,fSz2),np.float32)/(fSz2*fSz2)
filt3 = np.ones((fSz3,fSz3),np.float32)/(fSz3*fSz3)

while(cap.isOpened()):
    ret, frame = cap.read()
    # Applying the filters to the same image
    dstRGB1 = cv2.filter2D(frame,-1, filt1)
    dstRGB2 = cv2.filter2D(frame,-1, filt2)
    dstRGB3 = cv2.filter2D(frame,-1, filt3)

    # Show the filtered images in three different windows
    cv2.imshow('Filter 1: '+str(fSz1)+'x'+str(fSz1),dstRGB1)
    cv2.imshow('Filter 2: '+str(fSz2)+'x'+str(fSz2),dstRGB2)
    cv2.imshow('Filter 3: '+str(fSz3)+'x'+str(fSz3),dstRGB3)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
