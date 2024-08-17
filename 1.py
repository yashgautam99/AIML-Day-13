import cv2
import numpy as np 

path="C:\\Users\\STUDENT\\Desktop\\vid_mpeg4.mp4"

vid=cv2.VideoCapture(path)
print(vid)
print(vid.isOpened())

frame_counter = 0

while(vid.isOpened()):
    val,frame = vid.read()
    frame_counter +=1
    
    if(val):
        gray_im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ycrcb_im = cv2.cvtColor(frame, cv2.COLOR_BGR2YCrCb)
        hsv_im = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
    cv2.imshow('Frame', gray_im)
    cv2.imshow('HSV', hsv_im)
    cv2.imshow('YCRCB', ycrcb_im)
    cv2.imshow('Orignal', frame)
    if(cv2.waitKey(1)==ord('q')):
        break
vid.release()
cv2.destroyAllWindows()