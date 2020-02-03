import numpy as np
import cv2
import os


cap = cv2.VideoCapture('C:\\Users\\INKOM06\\Documents\\a1OpenCVcodes\\data\\bubat.mp4')

totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(totalFrames)


scRatio = 0.1

frameIdx = 1
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    pct = (frameIdx/totalFrames)*100
    print('Frame index: %d Pct: %3.2f %s' % (frameIdx,pct,chr(37)))
    frameIdx = frameIdx + 1

    # Our operations on the frame come here

    newRow = int(frame.shape[1]*scRatio)
    newCol = int(frame.shape[0]*scRatio)

    frame = cv2.resize(frame,(newRow, newCol) , interpolation = cv2.INTER_AREA)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    frame2 = frame[int(newCol/2):newRow, :]
    cv2.imshow('Original image',frame2)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

