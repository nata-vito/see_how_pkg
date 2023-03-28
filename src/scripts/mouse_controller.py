#!/venv/bin/python

import rospy
import mouse as Mouse
from subscriber import ImgCon

if __name__ == "__main__":
    try:
        imgSubToMouse = ImgCon(obj = Mouse, label = 'Mouse')
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Shutting down")