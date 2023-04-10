#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8
from std_msgs.msg import Int8MultiArray
rospy.init_node('sum')
def callback(msg):
  mass = msg.data
  rospy.loginfo('Sum hears %s', mass)
  sumel = sum(mass)
  sum_msg = Int8()
  sum_msg.data = sumel
  rospy.loginfo('Sum tells %s', sum_msg.data)
  pub.publish(sum_msg)  
pub = rospy.Publisher('sumreq', Int8, queue_size=10)
rospy.Subscriber('polysum', Int8MultiArray, callback, queue_size=10)
rospy.spin()
