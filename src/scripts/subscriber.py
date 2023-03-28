#!/venv/bin/python
import rospy
import cv2 as cv
import ros_numpy
from mouse import Mouse
from see_how_pkg.msg import Hand
from sensor_msgs.msg import Image

# Subscriber of the image published by the '/camera' topic
class ImgCon:
    def __init__(self, obj = None, label = None, data = None, flag = 0):
        
        if obj and label != None:
            rospy.init_node(label, anonymous=True)
            self.hand           = obj.Hand()
            self.label          = label
            
        else:
            rospy.init_node('image', anonymous=True)
            self.hand           = None
            self.label          = label
            
        # Topic to read the image msg data
        self.image_sub          = rospy.Subscriber("camera", Image, self.image_callback)
        self.img                = None
        self.data               = data
        self.flag               = flag
    
    
    # Processing images and publishing the results
    def image_callback(self, msg):
        
        self.img = ros_numpy.numpify(msg)
        #print(self.label)
        
        if self.label == 'Mouse':
            mouse = Mouse(ros = True, cam = self.img)
            mouse.main()
            print('Olha o rato aq')
        
        if self.label == 'left_hand':
            self.hand.Left(self.img)
            #self.hand.bounding_box
            
        if self.label == 'right_hand':
            self.hand.Right(self.img)
            #self.hand.bounding_box
        
        if self.flag == 1:
            self.showImage()
            #print(self.img)
   
    
    def showImage(self):
        
        if self.img is None:
            print("Could not read the image.")
        else:
            cv.imshow("Image Window", self.img)      
            cv.waitKey(3)   
        
        
class SubLeft:
    def __init__(self):
        
        rospy.Subscriber('/Left', Hand, self.left_callback)
        self.data               = None
        
    def left_callback(self, data):
        
        self.data               = data
        #print(data)
    
    def getData(self):
        return self.data
    
        
class SubRight:
    def __init__(self):
        
        rospy.Subscriber('/Right', Hand, self.right_callback)
        self.data               = None
        
    def right_callback(self, data):
        
        self.data               = data
        #print(data)