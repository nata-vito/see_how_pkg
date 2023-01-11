#!/usr/bin/env python3
import os
import sys
import time
import rospy
import cv2 as cv
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class image_converter:
    def __init__(self):
        # To conver image-msg to Cv Type
        self.bridge = CvBridge()
        # Topic to read the image msg data
        self.image_sub = rospy.Subscriber("camera", Image, self.image_callback)
        self.img = None

    def image_callback(self, msg):
        try:
            self.img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
            #print(self.img)
        except CvBridgeError as e:
            rospy.logerr("CvBridge Error: {0}".format(e))
                
        self.showImage(0) 
    
    
    def showImage(self, hand_side):
        if self.img is None:
            print("Could not read the image.")
        else:  
            path = r'/home/rota2030/Documents/ws_see_how/src/see_how_pkg/src/scripts/img'
            os.chdir(path)
            cv.imwrite('imgTest.jpg', self.img)
            time.sleep(0.050)
            #cv.imshow("Image Window", self.img)      
            #cv.waitKey(3)
            
            #test.leftHand(self.img)
            return self.img
       
        
        
def main(args):
    ic = image_converter()
    rospy.init_node('image_converter', anonymous=True)
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down")
    
    #cv.destroyAllWindows()
    
if __name__ == "__main__":
    main(sys.argv)