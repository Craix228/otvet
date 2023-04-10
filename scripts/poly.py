#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int8MultiArray
rospy.init_node('poly')
def callback(msg):
 var = msg.data
 rospy.loginfo('Poly hears  %s', var)
 pol = [0, 0, 0]   
 for i in range(len(var)):
    pol[i] = var[i] ** (3 - i)  
 poly_msg = Int8MultiArray()
 poly_msg.data = pol
 rospy.loginfo('Poly tells %s', poly_msg.data)
 pub.publish(poly_msg)  
pub = rospy.Publisher('polysum', Int8MultiArray, queue_size=10)
rospy.Subscriber('reqpoly', Int8MultiArray, callback, queue_size=10)
rospy.spin()
