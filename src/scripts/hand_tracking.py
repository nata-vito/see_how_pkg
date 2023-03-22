#!/venv/bin/python

import math 
import cv2 as cv
import numpy as np
import mediapipe as mp

class handDetector():
    
    # Parameters
    def __init__(self, mode=True, maxHands=2, modelComplexity=0, detectionCon=0.5, trackCon=0.5, op = ''):
        
        # To video streal False, any image true
        self.mode               = mode     

        # Maximum number of hands to detect         
        self.maxHands           = maxHands

        # Complexity of the hand landmark model
        self.modelComplexity    = modelComplexity

        # Minimum confidence value from the hand detection model
        self.detectionCon       = detectionCon

        # Minimum confidence value from the landmark-tracking model
        self.trackCon           = trackCon

        # Solutions from MediaPipe
        self.mpHands            = mp.solutions.hands
        self.hands              = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionCon, self.trackCon)
        self.mpDraw             = mp.solutions.drawing_utils
        self.handFingers        = "0" # To transform list in a string
        self.fingers            = 0   # To storing fingers
        self.side               = ""  # Right/Left
        self.countFingers       = -1
        self.ids                = [4, 8, 12, 16, 20]
        self.op                 = "" # To define what is the correct hant to detect
        
    # To find hands in video
    def findHands(self, img, op = "", draw=True):
        
        imgRGB              = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results        = self.hands.process(imgRGB)
        self.op             = op

        self.findPosition(img)
        
        if self.side == self.op:
            
            if self.results.multi_hand_landmarks:
                
                for handLms in self.results.multi_hand_landmarks:
                    
                    #Drawing Landmarks
                    if draw: self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

            return img

    # Getting landmarks position
    def findPosition(self, img, handNo=0, draw=True):
        self.lmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]

            # Hand Labeling
            for id, hand_handedness in enumerate(self.results.multi_handedness):
                self.label = hand_handedness.classification[0].label
    
            if self.label == self.op:
                for id, lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    self.lmList.append([id, cx, cy])
                        
                    # Drawing blue points
                    if draw: cv.circle(img, (cx, cy), 5, (255, 0, 0), cv.FILLED)

        self.handsLabel(self.lmList, self.ids)
            
        return self.lmList
    
    def bounding_box(self, img, handNo=0, draw=True):
        h, w, c = img.shape
        if self.results.multi_hand_landmarks:
            #myHand = self.results.multi_hand_landmarks[handNo]
            myHand = self.results.multi_hand_landmarks
            for handLMs in myHand:
                x_max = 0
                y_max = 0
                x_min = w
                y_min = h
                for lm in handLMs.landmark:
                    x, y = int(lm.x * w), int(lm.y * h)
                    if x > x_max:
                        x_max = x
                    if x < x_min:
                        x_min = x
                    if y > y_max:
                        y_max = y
                    if y < y_min:
                        y_min = y
            coordinates = x_min, y_min, x_max, y_max
        # if draw: cv.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)
            print(coordinates)
            return coordinates
    
    # Getting the level output
    def levelOutput(self, frame):

        if len(self.lmList) != 0:
            x1, y1 = self.lmList[4][1], self.lmList[4][2]               # Thumb tip circle
            x2, y2 = self.lmList[8][1], self.lmList[8][2]               # Index tip circle
            cx, cy = (x1 + x2) // 2, (y1 + y2) //2                      # Middle circle

            cv.circle(frame, (x1, y1), 10, (255, 0, 255), cv.FILLED)
            cv.circle(frame, (x2, y2), 10, (255, 0, 255), cv.FILLED)
            cv.line(frame, (x1, y1), (x2,y2), (255,0,255), 3)
            cv.circle(frame, (cx, cy), 10, (255, 0, 255), cv.FILLED)

            self.length = math.hypot(x2-x1, y2-y1)
            self.length = int(np.interp(self.length, [30, 230], [0, 100]))

            if self.length < 20:
                cv.circle(frame, (cx, cy), 10, (0, 255, 0), cv.FILLED)
            
            return self.length

    # Transforming list in a string
    def deconstructionHand(self):
        self.handFingers = ""
        
        if self.label == self.op:
            for i in range(len(self.fingers)):
                self.handFingers += str(self.fingers[i])
            return self.handFingers

    # Find the positional hand's side
    def handsLabel(self, pose, ids):

        self.fingers = []

        # There is a hand in the frame
        if len(pose) != 0:
            
            # Finding the hand's label
            if self.label == self.op:
                # hand Thumb -> Left
                if pose[ids[0]][1] > pose[ids[0] - 1][1] and self.op == "Left":
                        self.fingers.append(1)
                        
                # hand thumb -> Right
                if pose[ids[0]][1] < pose[ids[0] - 1][1] and self.op == "Right":
                    self.fingers.append(1)
                    
                else: 
                    self.fingers.append(0)

                # 4 Fingers
                for id in range(1, 5):
                    # Check finger reference points to define hand is open or not
                    if pose[ids[id]][2] < pose[ids[id] - 2][2]:
                        self.fingers.append(1)
                    else: 
                        self.fingers.append(0)

            # Decosntruction of List to String
            self.handFingers = self.deconstructionHand()
            self.side        = self.label
    
    # Text to inform the user if required       
    def labelText(self):
        
        if self.side == self.op:
            self.countFingers = 0
            
            if self.countFingers != 0:
                self.fingers = 00000
            else:
                for i in range(len(self.fingers)):
                    if self.fingers[i] == 1:
                        self.countFingers += 1
                
            
            
            return self.side + " -> " + str(self.countFingers)
        