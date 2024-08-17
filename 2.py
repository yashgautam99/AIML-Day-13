# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 11:13:33 2024

@author: STUDENT
"""

import cv2
import numpy as np

path="C:\\Users\\STUDENT\\Desktop\\vid_mpeg4.mp4"
vid=cv2.VideoCapture(path)
#background subtractor
#back_gd= dv2.getStructuringElement(cv2.MORPH.ELLIPSE(3,3))

back_subtractor = cv2.createBackgroundSubtractorKNN(dist2Threshold=8000)

print(vid)
print(vid.isOpened())

frame_counter=0

while(vid.isOpened()):
    val,frame = vid.read()
    frame_counter+=1
    #if the frame is captured
    mask_image= back_subtractor.apply(frame)
    cv2.imshow('Frame',mask_image)
    cv2.imshow('Original',frame)
    if(cv2.waitKey(1)==ord('q')):
        break
vid.release() #close the object
cv2.destroyAllWindows()
print(frame_counter)