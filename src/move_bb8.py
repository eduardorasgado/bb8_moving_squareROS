#! /usr/bin/env python

import rospy
import time
from geometry_msgs.msg import Twist

class MoveBB8:
    def __init__(self):
        #move the bb8 in square
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=4)
        self.rate = rospy.Rate(2) #2 hz
    
    def do_a_move(self, timing, linearist, angularist):
        #create the object to move
        my_vel=Twist()
        #set the variables to move
        my_vel.linear.x= linearist
        my_vel.angular.z= angularist
        
        self.publish_cmd_vel(my_vel)
        
        #from time python library in seconds
        time.sleep(timing)
        
        #now stop the bb8 for avoiding action to continue
        self.stoptheBB8(my_vel)
    
    #just publish the actions
    def publish_cmd_vel(self, my_vel):
        
        #check if there are connections to publish
        connections = self.pub.get_num_connections()
        if connections > 0:
            try:
                #publishing the actions
                self.pub.publish(my_vel)
                rospy.loginfo("action published")
                return True
            except:
                pass
        else:
            #if no connections
            self.rate.sleep()
        
    #in case to stop the robot
    def stoptheBB8(self, my_vel):
        #stop the bb8
        my_vel.linear.x = 0
        my_vel.linear.y = 0
        my_vel.linear.z = 0
        my_vel.angular.z = 0
        
        self.pub.publish(my_vel)
        rospy.loginfo("BB8 stopped")
        self.rate.sleep()
        
    #make the loo to move the robot
    def movesinSquare(self):
        timeTo = 0
        while timeTo <= 4:
            # Move Forwards
            self.do_a_move(2.0, 0.2, 0.0)
            # Stop
            self.do_a_move(4.0, 0, 0.0)
            # Turn
            self.do_a_move(3.5, 0, 0.2)
            # Stop
            self.do_a_move(0.5, 0, 0.0)
            timeTo += 1
        