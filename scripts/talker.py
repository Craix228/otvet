#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16

rospy.init_node('talker')
pub2 = rospy.Publisher('overflow_topic', Int16, queue_size=10)
pub = rospy.Publisher('listener_topic', Int16, queue_size=10)
rate = rospy.Rate(10)
def start_talker():
    msg = Int16()
    alr = Int16()
    x=0
    while not rospy.is_shutdown():
        x = int(x)
        rospy.loginfo(x)
        x= x+2 
        if x>100:
          x=0
          alr.data = x
          pub2.publish(alr)
        msg.data = x
        pub.publish(msg)
        rate.sleep()
try:
    start_talker()
except (rospy.ROSInterruptException, KeyboardInterrupt):
    rospy.logerr('Exception catched')
