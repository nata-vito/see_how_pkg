#!/usr/bin/env python3
import sys
import rospy
import cv2 as cv
import ros_numpy
import pub_see_how as Pub
import left_hand as lfHand
from sensor_msgs.msg import Image

class image_converter:
    def __init__(self):
        # Topic to read the image msg data
        rospy.init_node('image_converter', anonymous=True)
        self.image_sub = rospy.Subscriber("camera", Image, self.image_callback)
        self.img = None
        self.lf = lfHand.LeftHand()

    def image_callback(self, msg):
        self.img = ros_numpy.numpify(msg)
        self.lf.HandCapture(self.img)
        #print(self.img)
    
    def showImage(self):
        if self.img is None:
            print("Could not read the image.")
        else:  
            cv.imshow("Image Window", self.img)      
            cv.waitKey(3)   
        
        
def main(args):
    ic = image_converter()
    
    
if __name__ == "__main__":
    try:
        main(sys.argv)
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Shutting down")