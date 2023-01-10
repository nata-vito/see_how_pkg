#!/usr/bin/env python3
import rospy
import cv2 as cv
import pub_see_how as Pub
import hand_tracking as ht

def videoCapture():
    # Camera capture
    cap         = cv.VideoCapture(0)
    i           = 0
    tracking    = ht.handDetector(detectionCon=0.75, maxHands=1, op='Left')
    # Hand landmarks 
    #ids         = [4, 8, 12, 16, 20]

    # Verify camera errors
    if(cap.isOpened() == False):
        print("Error openning the video")

    while(cap.isOpened() and not rospy.is_shutdown()):
        
        success, frame  = cap.read()

        # Flip frame to correct predict
        frame = cv.flip(frame,1)

        # Hand's contour
        contour         = tracking.findHands(frame, op='Left') # OP select the hand to detect
        i              += 1 

        level = tracking.levelOutput(frame)
        
        if level:
            print(str(level) + "%")
            
        num = tracking.labelText()            
        #print(num + "%")
        
        if success:
            font     = cv.FONT_HERSHEY_COMPLEX
            left     = (50,50)
            leftSt   = (50, 80)
            right    = (380, 50)
            rightSt  = (380, 80)
            level    = str(tracking.levelOutput(frame)) + '%'

            if tracking.countFingers > -1:
                if tracking.label == 'Left':
                    
                    # Pub Here
                    pub = Pub.Publisher(tracking.handFingers, tracking.side, 
                                        tracking.countFingers, tracking.op)
                    pub.talker()
                    
                    """ print(tracking.mpHands)
                    print(tracking.hands)
                    
                    print("ok") """
                    
                    cv.putText(frame, num, left, font, 1, (255,0,0), 2)
                    cv.putText(frame, level, leftSt, font, 1, (255,0,0), 2)
                else:
                     cv.putText(frame, num, right, font, 1, (255,0,0), 2)
                     cv.putText(frame, level, rightSt, font, 1, (255,0,0), 2)

            cv.imshow('Frame', frame)
            key = cv.waitKey(1)

            # Exit by user hand
            """ if tracking.handFingers == "01100":
                break  """

            # Exit by user using keyboard
            if key == ord('q'):
                break
        else:
            break

    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    try:
        videoCapture()
    except rospy.ROSInterruptException:
            pass