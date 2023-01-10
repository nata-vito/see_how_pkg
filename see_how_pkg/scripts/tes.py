import cv2
import time
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    cv2.imshow("Img", img)
    cv2.waitKey(1)