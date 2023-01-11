#!/usr/bin/env python3
import rospy
import cv2 as cv
import subprocess
import hand_tracking as ht

def checkFile(imageFile):
    try:
        subprocess.run(["identify", "-regard-warnings", imageFile]).check_returncode()
        return True
    except (subprocess.CalledProcessError) as e:
        return False

def leftHand():
    path = r'/home/rota2030/Documents/ws_see_how/src/see_how_pkg/src/scripts/img/imgTest.jpg'
    
    while cv.haveImageReader(path):
        if checkFile(path) == True:
            img = cv.imread(path, cv.IMREAD_ANYCOLOR)
            cv.imshow('test', img)
            cv.waitKey(20) 

    """ cv.imshow("test", imgSub.image_converter().img)
    cv.waitKey(3) """


if __name__ == '__main__':
    try:
        leftHand()
        
        #print("ok - left")
    except rospy.ROSInterruptException:
            pass