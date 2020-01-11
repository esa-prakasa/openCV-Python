import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ret,th1 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    ret,th2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY_INV)
    edges = cv2.Canny(th1,90,100,5)



    # Display the resulting frame
    cv2.imshow('frame-Binary',th1)
    cv2.imshow('frame2-Inv Binary',th2)
    cv2.imshow('frame3- Edges',edges)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
