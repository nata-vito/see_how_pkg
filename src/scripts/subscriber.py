#!/usr/local/bin/python3.9
import rospy
import cv2 as cv
import ros_numpy
from see_how_pkg.msg import Hand
from sensor_msgs.msg import Image

class ImgCon:
    def __init__(self, obj = None, label = None, data = None, flag = 0):
        
        if obj and label != None:
            rospy.init_node(label, anonymous=True)
            self.hand           = obj.Hand()
            self.label          = label
            
        else:
            rospy.init_node('image', anonymous=True)
            self.hand           = None
            self.label          = None
            
        # Topic to read the image msg data
        self.image_sub          = rospy.Subscriber("camera", Image, self.image_callback)
        self.img                = None
        self.data               = data
        self.flag               = flag

    def image_callback(self, msg):
        self.img = ros_numpy.numpify(msg)
                
        if self.label == 'left_hand':
            self.hand.Left(self.img)
        elif self.label == 'right_hand':
            self.hand.Right(self.img)
        
        
        if self.flag == 1:
            self.showImage()
            #print(self.img)
        
        return self.img
    
    def showImage(self):
        
        if self.img is None:
            print("Could not read the image.")
        else:
            print(self.img)
            cv.imshow("Image Window", self.img)
            cv.waitKey(3) 
                    
    def getImg(self):
        return self.img
        
class SubLeft:
    def __init__(self):
        rospy.init_node('sub_left_hand', anonymous=True)
        sub                     = rospy.Subscriber('/Left', Hand, self.left_callback)
        self.data               = None
        
    def left_callback(self, data):
        self.data               = data
        print(data.level)
    
    def getData(self):
        return self.data
    
        
class SubRight:
    
    def __init__(self, flag = 0):
        rospy.init_node('sub_right_hand', anonymous=True)
        sub                     = rospy.Subscriber('/Right', Hand, self.right_callback)
        self.side               = ''
        self.fingers            = ''
        print(flag)
              
    def right_callback(self, data):
        self.side               = data.side
        self.fingers            = data.fingers
        
        
    def getSide(self):
        return self.side
    
    def getFingers(self):
        return self.fingers