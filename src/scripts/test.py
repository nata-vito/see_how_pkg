import cv2
import hand_tracking

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = hand_tracking.handDetector(detectionCon = 0.8, maxHands = 1)

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    cv2.imshow('Cam', img)
    cv2.waitKey(1)