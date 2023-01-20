#!/usr/bin/env python3
import rospy
import hands as Hands
from see_how_pkg.src.scripts.subscriber import ImgCon
     
if __name__ == "__main__":
    try:
        ic = ImgCon(Hands, 'right_hand')
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Shutting down")