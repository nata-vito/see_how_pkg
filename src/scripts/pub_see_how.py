import rospy
from std_msgs.msg import Header
from see_how_pkg.msg import Hand

class Publisher:
    def __init__(self, fingers = 00000, side = 'None', countFingers = 0 , nodeName = 'Hand', level = 0, X = 0, Y = 0, St_X = 0, St_Y = 0):
        
        self.fingers            = fingers
        self.side               = side
        self.countFingers       = countFingers
        self.nodeName           = nodeName
        self.timestamp          = rospy.get_time()
        self.level              = int(level or 0)
        self.pub                = rospy.Publisher(self.nodeName, Hand, queue_size=10)
        self.pose_X             = X
        self.pose_Y             = Y
        self.pose_St_X          = St_X
        self.pose_St_Y          = St_Y
        
    def talker(self):
        rate = rospy.Rate(100)
        rate.sleep()
    
        # Message construction
        msg                     = Hand()
        msg.header              = Header(stamp = rospy.Time.now(), frame_id = 'odom')
        msg.side                = self.side
        msg.fingers             = self.fingers
        msg.countFingers        = int(self.countFingers)
        msg.nodeName            = self.nodeName  
        msg.level               = self.level
        msg.pose_X              = self.pose_X
        msg.pose_Y              = self.pose_Y
        msg.pose_St_X           = self.pose_St_X
        msg.pose_St_Y           = self.pose_St_Y
        
        if self.nodeName == self.side:
            self.pub.publish(msg)
        else:
            pass

