#! /usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

class MoveBB8:
    def __init__(self):
        #move the bb8 in square
        pub = rospy.Publisher('/cmd_vel', Twist, queue_size=4)
        
        #create the object to move
        my_vel=Twist()
        rate = rospy.Rate(2) #2 hz
        
        for i in range(4):
            my_vel.linear.x=0.4
            my_vel.angular.z=0
            
            #publishing the movements
            for i in range(3):
                pub.publish(my_vel)
                rate.sleep()
            
            my_vel.linear.x=0.2
            my_vel.angular.z=0.4
            
            #publishing the movementss
            for i in range(4):
                pub.publish(my_vel)
                rate.sleep()
        
        my_vel.linear.x=0.4
        my_vel.angular.z=0
        
        #publishing the movements
        for i in range(2):
            pub.publish(my_vel)
            rate.sleep()
            
        #stop the bb8
        my_vel.linear.x = 0
        my_vel.linear.y = 0
        my_vel.linear.z = 0
        my_vel.angular.z = 0
        pub.publish(my_vel)
        rate.sleep()