#!/usr/bin/python

import rospy
from socket_nucleus import SockServer  
rospy.init_node('socket_node', anonymous=True)   

a = SockServer(9999) 

if __name__ == '__main__':
    try:
        a.serverCore() 
    except rospy.ROSInterruptException:
        print("Shutting down")
