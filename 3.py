import cv2
import numpy as np
import imutils

path="C:\\Users\\STUDENT\\Desktop\\vid_mpeg4.mp4"
vid=cv2.VideoCapture(path)
back_subtractor = cv2.createBackgroundSubtractorKNN(dist2Threshold=8000)

print(vid)
print(vid.isOpened())

frame_counter=0
f = 0

while(f<=500):
    f = f+1
    val,frame = vid.read() 
    
    #if the frame is captured
    mask_image= back_subtractor.apply(frame)
    cnts = cv2.findContours(mask_image,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    final_counters = imutils.grab_contours(cnts)
    
    #big object detection
    for c in final_counters:
        area = cv2.contourArea(c)
        if (area>50):
            print(area)
            M = cv2.moments(c)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            
    cv2.imshow('Frame',mask_image)
    cv2.imshow('Original',frame)
    if(cv2.waitKey(1)==ord('q')):
        break
vid.release() #close the object
cv2.destroyAllWindows()
print(frame_counter)