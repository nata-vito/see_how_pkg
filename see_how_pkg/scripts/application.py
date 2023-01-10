import cv2 as cv
from libcst import RightShift
import hand_tracking as ht

def videoCapture():
    # Camera capture
    cap         = cv.VideoCapture(0)
    i           = 0
    tracking    = ht.handDetector(detectionCon=0.75, maxHands=2)
    # Hand landmarks 
    ids         = [4, 8, 12, 16, 20]

    # Verify camera errors
    if(cap.isOpened() == False):
        print("Error openning the video")

    while(cap.isOpened()):
        
        success, frame  = cap.read()

        # Flip frame to correct predict
        frame = cv.flip(frame,1)

        # Hand's contour
        contour         = tracking.findHands(frame)
        i              += 1 

        tracking.findPosition(frame)    # Getting positional landmarks points
        level = tracking.levelOutput(frame)
        
        if level:
            print(level)

        # Detection and decosntruction of List to String
        tracking.handsLabel(tracking.lmList, ids)
        num = tracking.labelText()

        if success:
            font     = cv.FONT_HERSHEY_COMPLEX
            left     = (50,50)
            leftSt   = (50, 80)
            right    = (380, 50)
            rightSt  = (380, 80)
            level    = str(level) + '%'

            if tracking.countFingers > 0:
                if tracking.label == 'Left':
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
    videoCapture()