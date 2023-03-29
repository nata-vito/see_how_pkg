import cv2
import numpy as np
import hand_tracking as htm
import time
import autopy, pyautogui
    

class Mouse:
    
    #
    def __init__(self, ros = False, cam = 0):
        
        self.wCam, self.hCam      = 640, 480
        self.frameR               = 100            # Frame Reduction
        self.smoothening          = 7
        self.ros                  = ros
        self.pTime                = 0
        self.plocX, self.plocY    = 0, 0 # prev location mouse
        self.clocX, self.clocY    = 0, 0 # current location mouse
        self.active               = 0
        self.controll_mode        = ''
        self.fingers              = ''
        self.img                  = ''

        if self.ros:
            self.cap              = cam
            self.cap              = cv2.resize(self.cap, (self.wCam, self.hCam), interpolation = cv2.INTER_AREA)
    
        else:
            self.cap              = cv2.VideoCapture(cam)
            self.cap.set(3, self.wCam)
            self.cap.set(4, self.hCam)
        
        
        self.detector             = htm.handDetector(maxHands=1)
        self.wScr, self.hScr      = autopy.screen.size()
        self.lmList, self.bbox    = '', ''
        self.x1, self.x2          = '', ''
        self.y1, self.y2          = '', ''
        self.fingers              = [0, 0, 0, 0, 0]
        self.controll_mode        = ''
        self.controll_mode_aux    = ''
        self.active               = ''
        
        pyautogui.FAILSAFE = False

    #
    def findHandLm(self):
        
        # 2. Get the tip of the index and middle fingers
        if len(self.lmList) != 0:
            self.x1, self.y1 = self.lmList[8][1:]
            self.x2, self.y2 = self.lmList[12][1:]
            
            # 3. Check which fingers are up
            self.fingers = self.detector.fingersUp()
        
        return self.fingers
    
    #
    def isCursor(self):      
        return True if (self.fingers == [1, 1, 1, 1, 1]) and (self.active == 0) else False
    
    #
    def isScroll(self):
        return True if (self.fingers == [0, 1, 0, 0, 0] or self.fingers == [0, 1, 1, 0, 0]) and (self.active == 0) else False
        
    #
    def isActivate(self):
        return False if self.fingers == [0, 0, 0, 0, 0] else True
        
    #  
    def decisionTaking(self):
                      
        if self.isCursor():
            self.controll_mode   = 'Cursor'
            self.active          = 1    
            self.controll_mode_aux = ''
            
        if self.isScroll():
            self.controll_mode   = 'Scroll'
            self.active          = 1

        if self.isActivate():
            self.controll_mode   = 'N'
            self.active          = 0
        
        
    #
    def actingControlMode(self):
        
        if self.controll_mode == 'Cursor' :
            
            # 4. Only Index Finger : Moving Mode
            if self.fingers[1] == 1 and self.fingers[2] == 0:
                
                # 5. Convert Coordinates
                cv2.rectangle(self.img, (self.frameR, self.frameR),  (self.wCam - self.frameR, self.hCam - self.frameR), (255, 0, 255), 2)
                x3 = np.interp(self.x1, (self.frameR, self.wCam - self.frameR), (0, self.wScr))
                y3 = np.interp(self.y1, (self.frameR, self.hCam - self.frameR), (0, self.hScr))
            
                # 6. Smoothen Values
                clocX = self.plocX + (x3 - self.plocX) / self.smoothening
                clocY = self.plocY + (y3 - self.plocY) / self.smoothening
                
                # 7. Move Mouse
                autopy.mouse.move(self.wScr - clocX, clocY)
                cv2.circle(self.img, (self.x1, self.y1), 15, (255, 0, 255), cv2.FILLED)
                self.plocX, self.plocY = clocX, clocY
                
            # 8. Both Index and middle fingers are up : Clicking Mode
            if self.fingers[1] == 1 and self.fingers[2] == 1:
                
                # 9. Find distance between fingers
                length, img, lineInfo = self.detector.findDistance(8, 12, self.img)
                print(length)
                
                # To avoid errors if the hand is not found in the image
                if length == 0:
                    self.controll_mode_aux = self.controll_mode
                    return 0
                
                # 10. Click mouse if distance short
                if length > 0 and length < 30:
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    autopy.mouse.click()
                    
        elif self.controll_mode == 'Scroll':
            
            cv2.rectangle(self.img, (200, 410), (245, 460), (255, 255, 255), cv2.FILLED)
            
            if len(self.lmList) != 0:
                
                if self.fingers == [0,1,0,0,0]:
                    pyautogui.scroll(1)

                if self.fingers == [0,1,1,0,0]:
                    pyautogui.scroll(-1)
                    
                elif self.fingers == [0, 0, 0, 0, 0]:
                    active = 0
                    mode = 'N'
                    
    #                         
    def main(self, img, flag):
        
        #print(self.ros)
        # 1. Find hand Landmarks
        if flag == False:
            success, self.img       = self.cap.read()
            self.img                = self.detector.findHandstoMouse(self.img)
            self.lmList, self.bbox  = self.detector.findMousePosition(self.img)
        else:
            img = cv2.resize(img, (self.wCam, self.hCam), interpolation = cv2.INTER_AREA)
            self.img                = self.detector.findHandstoMouse(img)
            self.lmList, self.bbox  = self.detector.findMousePosition(img)
        
        self.findHandLm()
        self.decisionTaking()
        self.actingControlMode()

        print(self.controll_mode, self.active)
        
        # 11. Frame Rate
        cTime = time.time()
        fps = 1 / (cTime - self.pTime)
        self.pTime = cTime
        cv2.putText(self.img, str(int(fps)), (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)
        
        # 12. Display
        cv2.imshow("Image", self.img)
        cv2.waitKey(1)
            
#                              
if __name__ == '__main__':
    mouse = Mouse(0)
    mouse.main()
else:
    pass
