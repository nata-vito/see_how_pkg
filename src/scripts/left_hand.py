#!/usr/bin/env python3
import rospy
import hands as Hands
from subscriber import ImgCon
     
if __name__ == "__main__":
    try:
        ic = ImgCon(Hands, 'left_hand')
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Shutting down")