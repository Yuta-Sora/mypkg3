#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
from std_msgs.msg import String
from std_msgs.msg import Float32

def is_num2(s):
    try:
        float(s)
    except ValueError:
        x = 0
        return x
    else:
        x = 1
        return x

def input_process():
    ctrl = 0
    while ctrl == 0:
        s = raw_input()
        check =is_num2(s)
        if check == 0:
            print('re-enter')
        elif check == 1:
            ss = float(s)
            ctrl = 1
    return ss

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int32, queue_size=10)
pub2 = rospy.Publisher('count_2', String, queue_size=10)
pub3 = rospy.Publisher('count_3', String, queue_size=10)
pub4 = rospy.Publisher('count_4', Float32, queue_size=10)
pub5 = rospy.Publisher('count_5', Float32, queue_size=10)

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
    if word2 == '<+>':
        print('input x :x + y')
        num1 = input_process()
        print('input y :x + y')
        num2 = input_process()
        pub4.publish(num1)
        pub5.publish(num2)
    elif word2 == '<->':
        print('input x :x - y')
        num1 = input_process()
        print('input y :x - y')
        num2 = input_process()
        pub4.publish(num1)
        pub5.publish(num2)
    rate.sleep()

