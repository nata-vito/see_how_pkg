#!/venv/bin/python

import rospy
import hands as Hands
from subscriber import ImgCon
     
print('oi')     
if __name__ == "__main__":
    try:
        ic = ImgCon(Hands, 'left_hand')
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Shutting down")