#!/venv/bin/python

import rospy
import cv2 as cv
import subscriber as sub
from sensor_msgs.msg import Image

def displayImg():
    camera              = sub.ImgCon(flag = 1)
    #camera              = sub.ImgCon(data = left.data, flag = 1)
    
    
    
    
if __name__ == '__main__':
    try:
        displayImg()
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Shutting down")