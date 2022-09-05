from re import I
import cv2
import numpy as np
 

cap=cv2.VideoCapture('videoplayback.mp4') 
# cap=cv2.VideoCapture(0) 

res,frame1= cap.read()
res,frame2= cap.read()

while cap.isOpened():
    diff = cv2.absdiff(frame1,frame2)
    gray= cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur= cv2.GaussianBlur(gray,(5,5),0)
    dilated= cv2.dilate(blur,None,iterations=3)
    _, thresh= cv2.threshold(dilated,15,255,cv2.THRESH_BINARY)
    # dilated= cv2.dilate(thresh,None,iterations=3)

    contours,_=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        (x,y,w,h)= cv2.boundingRect(contour)
        
        if cv2.contourArea(contour)<1:
            continue
        else:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame1,'Status : {}'.format('Movement'),(x,y),cv2.FONT_HERSHEY_COMPLEX,
            0.5,(255,20,5),1)

    # cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    
    cv2.imshow("Img",frame1)
    cv2.imshow("original",frame2)
    frame1=frame2
    res,frame2=cap.read()

    key= cv2.waitKey(50)
    if key==81 or key ==113:
        break
    # cv2.waitKey(20)

cap.release()
cv2.destroyAllWindows()    