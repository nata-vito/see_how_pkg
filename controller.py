import cv2
import math
from mouse import Mouse
import numpy as np
from hand_tracking import handDetector

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = handDetector(detectionCon = 0.8, maxHands = 1)

x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2)


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    if hands:
        lmList = hands[0]['lmList']
        x1, y1, z1 = lmList[5]
        x2, y2, z2 = lmList[17]
        
        distance = math.sqrt((y2 - y1) ** 2 + (x2 - x1)**2)
        A, B, C = coff
        distanceCM = A * distance ** 2 + B * distance + C
        
        if distanceCM > 30 and distanceCM < 100:
            #mouse = Mouse(img)
            #mouse.main()
            print('Start', distanceCM)
        else:
            print('Stop')
        
    else: print('Stop')
        
    cv2.imshow("Image", img)
    cv2.waitKey(1)