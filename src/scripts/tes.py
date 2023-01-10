#!/usr/bin/env python3
import rospy
import cv2 as cv
import hand_tracking as ht

def leftHand():
    path = r'/home/rota2030/Documents/ws_see_how/src/see_how_pkg/src/scripts/img/imgTest.jpg'
    
    while cv.haveImageReader(path):
        img = cv.imread(path, cv.IMREAD_ANYCOLOR)
        cv.imshow('test', img)
        cv.waitKey(3) 

    """ cv.imshow("test", imgSub.image_converter().img)
    cv.waitKey(3) """


if __name__ == '__main__':
    try:
        leftHand()
        
        #print("ok - left")
    except rospy.ROSInterruptException:
            pass