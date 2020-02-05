import numpy as np
import cv2
import os


cap = cv2.VideoCapture('C:\\Users\\Esa\\Documents\\a1OpenCVcodes\\data\\bubat.mp4')
totalFrames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(totalFrames)

scRatio = 0.3

ret, frame = cap.read()

hg = frame.shape[0]
wd = frame.shape[1]

hg2 = int(hg/2)


frameIdx = 1
while(True):
    ret, frame = cap.read()

    newRow = int(hg*scRatio)
    newCol = int(wd*scRatio)

    frame = cv2.resize(frame,(newCol,newRow) , interpolation = cv2.INTER_AREA)
    cv2.imshow('Original image',frame)

    pct = (frameIdx/totalFrames)*100
    print('Frame index: %d Pct: %3.2f %s' % (frameIdx,pct,chr(37)))
    frameIdx = frameIdx + 1

    frame = frame[int(0.6*newRow):newRow, int(0.5*newCol):newCol,:]

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img,(5,5))

    img,th1 = cv2.threshold(img,120,255,cv2.THRESH_BINARY)
    img = th1
    cv2.imshow('Binary images ',img)

    edges = cv2.Canny(img,50,60,apertureSize = 3)
    cv2.imshow('frame3- Edges',edges)

    if ((frameIdx < 310) or (frameIdx > 600)):
        lines = cv2.HoughLines(edges,3, np.pi/10,100)
        nLines = len(lines)
        print('Frame index: %d Pct: %3.2f %s : %d' % (frameIdx,pct,chr(37),nLines))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break







    
    

    #print(len(lines))

    #cv2.imshow('frame3- Edges',edges)
   
'''
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

        print('Point 1 ',x1,' ',y1,'  Point 2 ',x2,' ',y2)
        cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.imshow('Image',frame)


'''
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#    break


cap.release()
cv2.destroyAllWindows()

