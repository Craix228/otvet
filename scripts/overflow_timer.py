#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int16
def callback(alr):
    rospy.loginfo("Overflow %d", alr.data)
rospy.init_node('overflow_timer')
rospy.Subscriber('overflow_topic', Int16, callback, queue_size=10)
rospy.spin()
