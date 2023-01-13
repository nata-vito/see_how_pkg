#!/usr/bin/env python3
import rospy
import cv2 as cv
import numpy as np
import pub_see_how as Pub
import hand_tracking as ht

class LeftHand:
    def __init__(self, frame = None):
        self.frame      = np.asarray(frame)
        self.isImg      = False
        self.i          = 0
        self.tracking   = ht.handDetector(detectionCon=0.75, maxHands=1, op='Left')
        #print(type(self.frame))

    def HandCapture(self):

        # Verify camera errors
        #if(type(self.frame) == np.ndarray):
        #    self.isImg = True
        #else:
         #   print("Error openning the image")
          #  self.isImg = False
            

        #while(self.isImg):

        # Flip frame to correct predict
        self.frame = cv.flip(self.frame,1)
        
        

        # Hand's contour
        #contour         = self.tracking.findHands(self.frame, op='Left') # OP select the hand to detect
        """
        self.i         += 1 

        level = self.tracking.levelOutput(self.frame)
        
        print('Frame Flip - ok')
        
        if level:
            print(str(level) + "%")
            
        num = self.tracking.labelText()            
        #print(num + "%")
        
        if self.isImg:
            font     = cv.FONT_HERSHEY_COMPLEX
            left     = (50,50)
            leftSt   = (50, 80)
            right    = (380, 50)
            rightSt  = (380, 80)
            level    = str(self.tracking.levelOutput(self.frame)) + '%'
            
            if self.tracking.countFingers > -1:
                print('Count Fingers - ok')
                if self.tracking.label == 'Left':
                    
                    # Pub Here
                     pub = Pub.Publisher(self.tracking.handFingers, self.tracking.side, 
                                        self.tracking.countFingers, self.tracking.op)
                    pub.talker() 
                    
                   
                    #cv.putText(self.frame, num, left, font, 1, (255,0,0), 2)
                    #cv.putText(self.frame, level, leftSt, font, 1, (255,0,0), 2)
                    
             #   else:
                    #cv.putText(self.frame, num, right, font, 1, (255,0,0), 2)
                    #cv.putText(self.frame, level, rightSt, font, 1, (255,0,0), 2)

            #cv.imshow('Frame', self.frame)
            #cv.waitKey(3)

            # Exit by user hand
            if tracking.handFingers == "01100":
                break  

            # Exit by user using keyboard
           # if key == ord('q'):
            #    break
            
            self.isImg = False
            #else:
             #   break

        #cv.destroyAllWindows()
        """


