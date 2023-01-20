#!/usr/bin/env python3
import rospy
import cv2 as cv
import ros_numpy
from sensor_msgs.msg import Image

class ImgCon:
    def __init__(self, obj, label):
        # Topic to read the image msg data
        self.label          = label
        rospy.init_node(label, anonymous=True)
        self.image_sub      = rospy.Subscriber("camera", Image, self.image_callback)
        self.img            = None
        self.hand           = obj.Hand()

    def image_callback(self, msg):
        self.img = ros_numpy.numpify(msg)
        
        if self.label == 'left_hand':
            self.hand.Left(self.img)
        elif self.label == 'right_hand':
            self.hand.Right(self.img)
    
    def showImage(self):
        if self.img is None:
            print("Could not read the image.")
        else:  
            cv.imshow("Image Window", self.img)      
            cv.waitKey(3)   
        