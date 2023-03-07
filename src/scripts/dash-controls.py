#!/usr/local/bin/python3.9

import rospy
from std_msgs.msg import String
from subscriber import SubRight

def commandListener():
    listener = SubRight(flag=1)             # To Start commands processing
    print(type(listener.getSide()))
    
    
if __name__ == "__main__":
    try:
        commandListener()
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Shutting down")