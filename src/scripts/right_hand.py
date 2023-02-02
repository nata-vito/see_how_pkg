#!/usr/local/bin/python3.9
import rospy
import hands as Hands
from subscriber import ImgCon
     
if __name__ == "__main__":
    try:
        ic = ImgCon(Hands, 'right_hand')
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Shutting down")