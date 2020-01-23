#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String

n = 0

def cb(message):
    global n
    n = message.data*2
def cb2(message):
    rospy.loginfo(message.data)

def cb3(message):
    rospy.loginfo(message.data)

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    sub3 = rospy.Subscriber('count_3', String, cb3)
    pub = rospy.Publisher('twice', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
    rospy.spin()
