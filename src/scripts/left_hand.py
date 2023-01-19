#!/usr/bin/env python3
import rospy
import cv2 as cv
import numpy as np
import pub_see_how as Pub
import hand_tracking as ht

class LeftHand:
    def __init__(self, frame = None):
        self.frame      = frame
        self.isImg      = False
        self.i          = 0
        self.count      = 0
        self.tracking   = ht.handDetector(detectionCon=0.75, maxHands=1, op='Left')

    def showImage(self, img):
        cv.imshow('Test', img)
        cv.waitKey(3)
        
    def imageCapture(self, img):
        self.frame = img
        
        # Verify camera errors
        if(type(self.frame) == np.ndarray):
            self.isImg = True
            
            # Flip frame to correct predict
            self.frame = cv.flip(self.frame, 1)
        else:
           print("Error openning the image")
           self.isImg = False
               
    def HandCapture(self, img):
        
        # Capturing the first image to processing
        self.imageCapture(img)

        if self.isImg and not rospy.is_shutdown():
            
            # Hand's contour
            contour         = self.tracking.findHands(self.frame, op='Left') # OP select the hand to detect
            self.i         += 1
            level           = self.tracking.levelOutput(self.frame)
            
            if level:
                print(str(level) + "%")
                
            num = self.tracking.labelText()  
            
            font     = cv.FONT_HERSHEY_COMPLEX
            left     = (50,50)
            leftSt   = (50, 80)
            right    = (380, 50)
            rightSt  = (380, 80)
            level    = str(level) + '%'

            if self.tracking.countFingers > -1 and self.tracking.label == 'Left':                   
                cv.putText(self.frame, num, left, font, 1, (255,0,0), 2)
                cv.putText(self.frame, level, leftSt, font, 1, (255,0,0), 2)

            # Pub Here
            pub = Pub.Publisher(self.tracking.handFingers, self.tracking.side, self.tracking.countFingers, self.tracking.op, self.tracking.levelOutput(self.frame))
            pub.talker()
            
            cv.imshow('Frame', self.frame)
            key = cv.waitKey(1)
        

        


