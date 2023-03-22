import cv2
import math
import hand_tracking

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = hand_tracking.handDetector(detectionCon = 0.8, maxHands = 1)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    
    if hands:
        lmList = hands[0]['lmList']
        print(lmList)
        
        x1, y1 = lmList[5]
        x2, y2 = lmList[17]
        
        print(abs(x2 - x1))
        
    cv2.imshow('Cam', img)
    cv2.waitKey(1)