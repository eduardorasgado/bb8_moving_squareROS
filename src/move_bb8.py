
#! /usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import tf

class MoveBB8:

    def __init__(self, message):
        self.message = message
        
    def sendMessage(self):
        return self.message
        
    def moveinSquare(self, points):
        print len(points)
        print "This is moveinSquare function in class MoveBB8"
        
        