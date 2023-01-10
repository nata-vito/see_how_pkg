#!/usr/bin/env python3
import rospy
from std_msgs.msg import Header
from see_how_pkg.msg import Hand

class Publisher:
    def __init__(self, fingers = None, side = None, countFingers = None, nodeName = None):
        
        rospy.init_node('left_hand', anonymous=True)
        self.fingers            = fingers
        self.side               = side
        self.countFingers       = countFingers
        self.nodeName           = nodeName
        self.timestamp          = rospy.get_time()
        self.pub = rospy.Publisher(self.nodeName, Hand, queue_size=10)

    def talker(self):
        rate = rospy.Rate(100)
        rate.sleep()
    
        # Message construction
        msg = Hand()
        msg.header = Header(stamp = rospy.Time.now(), frame_id = 'odom')
        msg.side = self.side
        msg.fingers = int(self.fingers)
        msg.countFingers = int(self.countFingers)
        msg.nodeName = self.nodeName
        
        print(self.fingers, self.side, self.countFingers, self.nodeName, self.timestamp)    
        
        self.pub.publish(msg)
        #rate.sleep()


