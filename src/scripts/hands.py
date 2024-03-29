#!/venv/bin/python

import rospy
import cv2 as cv
import numpy as np
import pub_see_how as Pub
import hand_tracking as ht

class Hand:
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
               
    def Left(self, img):
        
        # Capturing the first image to processing
        self.imageCapture(img)

        if self.isImg and not rospy.is_shutdown():
            
            # Hand's contour
            contour             = self.tracking.findHands(self.frame, op='Left')    # OP select the hand to detect
            level               = self.tracking.levelOutput(self.frame)             # Get the level scale
            num                 = self.tracking.labelText()                         # Count the hand fingers
            self.i             += 1
            left_x              = 50
            left_y              = 50    
            left_St_X           = 50
            left_St_Y           = 80
            level               = str(level) + '%'              
            
            # Pub Here
            pub = Pub.Publisher(self.tracking.handFingers, self.tracking.side, self.tracking.countFingers, self.tracking.op, 
                                self.tracking.levelOutput(self.frame), left_x, left_y, left_St_X, left_St_Y)
            pub.talker()
        
    def Right(self, img):
        
        # Capturing the first image to processing
        self.imageCapture(img)

        if self.isImg and not rospy.is_shutdown():
            
            # Hand's contour
            contour             = self.tracking.findHands(self.frame, op='Right')   # OP select the hand to detect
            level               = self.tracking.levelOutput(self.frame)             # Get the level scale
            num                 = self.tracking.labelText()                         # Count the hand fingers
            self.i             += 1
            right_x             = 50
            right_y             = 50    
            St_X                = 50
            St_Y                = 80
            level               = str(level) + '%'  
            command             = 'Nope'
            bounding_box        = str(self.tracking.bounding_box(img))
            
            # Switch Case to commands 
            if self.tracking.handFingers   == '00000':
                command = 'Stop'
            elif self.tracking.handFingers   == '10001':
                command = 'Start'
            elif self.tracking.handFingers   == '01000':
                command = '1'
            elif self.tracking.handFingers == '01100':
                command = '2'
            elif self.tracking.handFingers == '01110':
                command = '3'
            elif self.tracking.handFingers == '01111':
                command = '4'
            elif self.tracking.handFingers == '11111':
                command = '5'
            elif self.tracking.handFingers   == '10000':
                command = '6'
            elif self.tracking.handFingers   == '11000':
                command = '7'
            elif self.tracking.handFingers   == '11100':
                command = '8'
            elif self.tracking.handFingers   == '11110':
                command = '9'
            elif self.tracking.handFingers   == '11111':
                command = '10'
            elif self.tracking.handFingers   == '00001':
                command = 'Exit'
               
            # Pub Here
            pub = Pub.Publisher(self.tracking.handFingers, self.tracking.side, self.tracking.countFingers, self.tracking.op, 
                                self.tracking.levelOutput(self.frame), right_x, right_y, St_X, St_Y, command, bounding_box)
            pub.talker()