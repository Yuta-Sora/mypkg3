#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
from std_msgs.msg import Float32
from std_msgs.msg import Float32
<<<<<<< HEAD
=======

>>>>>>> 98ece1436fdeac96f9db1b7668cdb2ce45fdbbdb
n = 0
m_ctrl = ''
x = 0
y = 0

def cb(message):
    global n
    n = message.data*2
def cb2(message):
    rospy.loginfo(message.data)

def cb3(message):
    global m_ctrl
    rospy.loginfo(message.data)
    m_ctrl = message.data

def cb4(message):
    global x
    x = message.data

def cb5(message):
    global y
    y = message.data
    if m_ctrl == '<+>':
        ans = x + y
        ans_w = str(x) + ' + ' + str(y) + ' = ' + str(ans)
        print(ans_w)
    elif m_ctrl == '<->':
        ans = x - y
        ans_w = str(x) + ' - ' + str(y) + ' = ' + str(ans)
        print(ans_w)

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int32, cb)
    sub3 = rospy.Subscriber('count_3', String, cb3)
    sub4 = rospy.Subscriber('count_4', Float32, cb4)
<<<<<<< HEAD
    sub5 = rospy.Subscriber('count_5', Float32 ,cb5)
=======
    sub5 = rospy.Subscriber('count_5', Float32, cb5)
    if m_ctrl == '<+>':
        ans = x + y;
        print('x' + ' + ' + 'y' + ' = ' + 'ans')
>>>>>>> 98ece1436fdeac96f9db1b7668cdb2ce45fdbbdb
    pub = rospy.Publisher('twice', Int32, queue_size=1)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
    rospy.spin()
