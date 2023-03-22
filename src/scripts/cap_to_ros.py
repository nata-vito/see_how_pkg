#!/usr/bin/python2

import cv2
import rospy
import base64
from socket_nucleus import SockCLient as sck
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


# CvBridge to work with ROS
bridge  = CvBridge()
cam_uri = 'http://172.17.52.190:8090/?action=stream'

# Video capture -> webcam
cap     = cv2.VideoCapture(0)

# Verifying the camera input 
print(cap.isOpened())

# Publishing Camera Image in /camera ROS Topic
def talker():
    pub_nparray         = rospy.Publisher('/camera', Image, queue_size = 1)
    rospy.init_node('image', anonymous=True)
    pub_base64         = rospy.Publisher('/camerabase64', Image, queue_size = 1)
    #rospy.init_node('image', anonymous=True)
    rate                = rospy.Rate(10)
    #sock                = sck(ip = '127.0.1.1', port = 9999)
    
    while not rospy.is_shutdown():
        while True:   
            ret, frame = cap.read()
            #print(frame)
            
            if not ret:
                break
            
            msg_np = bridge.cv2_to_imgmsg(frame, "bgr8")
            msg_64 = base64.b64encode(frame)
            
            pub_nparray.publish(msg_np)
            #pub_base64.publish(msg_64)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            if rospy.is_shutdown():
                cap.release()         
             
            
if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass