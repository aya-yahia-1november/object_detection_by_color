import cv2

import numpy as np

while(True):
    frame=cv2.imread("OIP.jpeg",1)
    cv2.imshow("frist",frame)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_b=np.array([110,50,50])
    u_b=np.array([130,255,255])
    mask=cv2.inRange(hsv,l_b,u_b)
    result=cv2.bitwise_not(frame,frame,mask=mask)
    cv2.imshow("detection ball",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    k=cv2.waitKey(0)
    if k==27:
      break


cv2.destroyAllWindows()