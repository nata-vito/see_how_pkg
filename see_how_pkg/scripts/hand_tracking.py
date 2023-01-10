import math 
import cv2 as cv
import numpy as np
import mediapipe as mp
#from api_request import FireRise 

class handDetector():
    # Parameters
    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionCon=0.5, trackCon=0.5):
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
        self.fingers            = [] # To storing fingers
        self.side               = "" # Right/Left
        self.countFingers       = 0
        
    # To find hands in video
    def findHands(self, img, draw=True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
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

            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])

                if draw: cv.circle(img, (cx, cy), 5, (255, 0, 0), cv.FILLED)
            
        return self.lmList

    def levelOutput(self, frame):

        if len(self.lmList) != 0:
            #print(self.lmList[4], self.lmList[8])

            x1, y1 = self.lmList[4][1], self.lmList[4][2]                             # Thumb tip cicle
            x2, y2 = self.lmList[8][1], self.lmList[8][2]                             # Index tip circle
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
        if self.label == "Left" or self.label == "Right":
            for i in range(len(self.fingers)):
                self.handFingers += str(self.fingers[i])
        return self.handFingers

    # Find the positional hand's side
    def handsLabel(self, pose, ids):

        self.fingers = []

        # There is a hand in the frame
        if len(pose) != 0:
            
            # Finding the hand's label
            if self.label == 'Left':
                # hand Thumb -> Left
                if pose[ids[0]][1] > pose[ids[0] - 1][1]:
                        self.fingers.append(1)
                else: 
                    self.fingers.append(0)

            elif self.label == 'Right':
                # hand Thumb -> Right
                if pose[ids[0]][1] < pose[ids[0] - 1][1]:
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
            
            print(self.label, self.fingers)

            # Decosntruction of List to String
            self.handFingers = self.deconstructionHand()
            self.side        = self.label

    # Send data to api 
    """ def sendToApi(tracking):
        api = FireRise("https://myhand-ff333-default-rtdb.firebaseio.com/", tracking.fingers)
        api.putData("mao", True, None, tracking.fingers)
    """

    def labelText(self):
        self.countFingers = 0

        for i in range(len(self.fingers)):
            if self.fingers[i] == 1:
                self.countFingers += 1
        
        return self.side + " -> " + str(self.countFingers)
        