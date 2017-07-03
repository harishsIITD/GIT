import cv2
import numpy
import matplotlib.pyplot as plt

#img=cv2.imread('C:/Users/saragada/Desktop/Harish.jpg',cv2.IMREAD_GRAYSCALE)
#
#cv2.imshow('Image',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


cap=cv2.VideoCapture(0)

while True:
    
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    
    if cv2.waitKey(1) & oxFF == ord('q'):
        
        break
cap.release()
cv2.destroyAllWindows()
