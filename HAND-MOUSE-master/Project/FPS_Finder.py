# Checking git commit
#check check check
import cv2
import numpy as np
import time
import os
import mediapipe 


cap = cv2.VideoCapture(0)
ptime=0
fps=0
fps_text=''
while True:
    ext, frame=cap.read()
    ctime=time.time()
   
    fps=fps+1
    # fps_txt = "FPS : {:.2f}".format(fps)


    if ctime-ptime >=1:
      
      
       # # fps= 1/(ctime-ptime)
      # cv2.waitKey(100)
      print(ctime-ptime,fps,ctime,ptime)

      ptime=ctime
      
      fps_txt = "FPS : {:.2f}".format(fps)
      
    #  cv2.imshow("Webcam",frame)
    # cv2.putText(frame,fps_txt, (5,30) , cv2.FONT_HERSHEY_PLAIN, 1 , (0,255,0), 1)
      fps=0
    cv2.putText(frame,fps_txt, (5,30) , cv2.FONT_HERSHEY_PLAIN, 1 , (0,255,0), 1)
  
    cv2.imshow("Webcam",frame)
    key = cv2.waitKey(1)

    if key== 81 or key == 113 :
         break
    # cv2.waitKey(10)

cap.release()
cv2.destroyAllWindows()