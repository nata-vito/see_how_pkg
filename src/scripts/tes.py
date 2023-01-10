#!/usr/bin/env python3
import rospy
import cv2 as cv
import pub_see_how as Pub
import image_sub as imgSub
#import hand_tracking as ht

def leftHand(img):
    i           = 0
    #tracking    = ht.handDetector(detectionCon=0.75, maxHands=1, op='Left')
    success     = 0
  
    #frame  = imgSub.image_converter().img

    cv.imshow('test', img)
    cv.waitKey(3) 

    """ cv.imshow("test", imgSub.image_converter().img)
    cv.waitKey(3) """


""" if __name__ == '__main__':
    try:
        leftHand()
        
        print("ok - left")
    except rospy.ROSInterruptException:
            pass """