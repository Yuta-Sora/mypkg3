#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=1)
pub2 = rospy.Publisher('count_2', String, queue_size=10)
pub3 = rospy.Publisher('count_3', String, queue_size=10)
rate = rospy.Rate(10)
n = 0
a = 99
word = "Hello World"
while not rospy.is_shutdown():
    n += 1
    word2 = raw_input()
    pub.publish(n)
    pub2.publish(word)
    pub3.publish(word2)
    rate.sleep()

