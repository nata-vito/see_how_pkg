#!/venv/bin/python

import rospy
from subscriber import ImgCon

if __name__ == "__main__":
    try:
        imgSubToMouse = ImgCon(label = 'Mouse')
        rospy.spin()
    except rospy.ROSInterruptException:
        print("Shutting down")