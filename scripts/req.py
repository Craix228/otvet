#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8
from std_msgs.msg import Int8MultiArray
rospy.init_node('req')
pub = rospy.Publisher('reqpoly', Int8MultiArray, queue_size=10)
rate = rospy.Rate(1)

def callback(msg):
  rospy.loginfo('Sum hears %s', msg.data)
  rospy.Subscriber('sumreq' , Int8, callback, queue_size=10)
def Request():
  poly_msg = Int8MultiArray()
  var = [2, 4, 5]
  while not rospy.is_shutdown():
   poly_msg.data = var
   rospy.loginfo('Req tells %s', poly_msg.data)
   pub.publish(poly_msg)
   rate.sleep()
try:
  Request()
except (rospy.ROSInterruptException, KeyboardInterrupt):
  rospy.logerr('Exception catched')
