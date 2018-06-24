
#! /usr/bin/env python
import rospy

class MoveBB8:
    def __init__(self, message):
        self.message = message
        
    def sendMessage(self):
        return self.message
