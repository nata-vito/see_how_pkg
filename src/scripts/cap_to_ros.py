#!/usr/bin/python

import cv2
import rospy
from socket_nucleus import SockCLient as sck
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


# CvBridge to work with ROS
bridge = CvBridge()

# Video capture -> webcam
cap = cv2.VideoCapture('http://192.168.49.1:8080/?action=stream')

# Verifying the camera input 
print(cap.isOpened())

# Publishing Camera Image in /camera ROS Topic
def talker():
    pub                 = rospy.Publisher('/camera', Image, queue_size = 1)
    rospy.init_node('image', anonymous=True)
    rate                = rospy.Rate(10)
    #sock                = sck(ip = '127.0.1.1', port = 9999)
    
    while not rospy.is_shutdown():
        while True:   
            ret, frame = cap.read()
            #print(frame)
            
            if not ret:
                break
            
            msg = bridge.cv2_to_imgmsg(frame, "bgr8")
            pub.publish(msg)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            if rospy.is_shutdown():
                cap.release()         
             
            """ sock.clientResponse()   
                     
            if sock.frame.all():    
                msg = bridge.cv2_to_imgmsg(sock.frame, "bgr8")
                pub.publish(msg)
        
            if cv2.waitKey(1) & 0xFF == ord('q'):
                sock.client_socket.close()
                break
            
            if rospy.is_shutdown():
                sock.client_socket.close()
                 """
if __name__ == "__main__":
    try:
        talker()
    except rospy.ROSInterruptException:
        pass