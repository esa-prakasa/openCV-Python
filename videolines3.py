import numpy as np
import cv2
import os


cap = cv2.VideoCapture('C:\\Users\\Esa\\Documents\\a1OpenCVcodes\\data\\lipi.mp4')
totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(totalFrames)

scRatio = 0.3


frameIdx = 1
while(True):
    ret, frame = cap.read()

    h = frame.shape[1]
    w = frame.shape[0]
    center = (w /5, h / 3)

    angle90 = 90
 
    scale = 1.0
 
    M = cv2.getRotationMatrix2D(center, angle90, scale)
    frame = cv2.warpAffine(frame, M, (w, h))


    newRow = int(frame.shape[1]*scRatio)
    newCol = int(frame.shape[0]*scRatio)

    frame = cv2.resize(frame,(newRow, newCol) , interpolation = cv2.INTER_AREA)
    cv2.imshow('Original image',frame)

    #frame2 = frame[int(frame.shape[0]*0.5):newRow, 0:frame.shape[1],:]
    #frame = frame2
    #cv2.imshow('ROI-RGB',frame)


    pct = (frameIdx/totalFrames)*100
    print('Frame index: %d Pct: %3.2f %s' % (frameIdx,pct,chr(37)))
    frameIdx = frameIdx + 1

    # Our operations on the frame come here
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img,(3,3))


    img,th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
    img = th1

    img = cv2.blur(img,(3,3))
    img,th1 = cv2.threshold(img,40,255,cv2.THRESH_BINARY_INV)
    img = th1

    cv2.imshow('Binary images ',img)


    edges = cv2.Canny(img,50,60,apertureSize = 3)
    cv2.imshow('frame3- Edges',edges)
    lines = cv2.HoughLines(edges,4, np.pi/30,100)

    cv2.imshow('frame3- Edges',edges)
   

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

        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 5)
        cv2.imshow('Image',frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

