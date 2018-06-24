#! /usr/bin/env python
#server to be called for move in square
import rospy
from std_srvs.srv import Empty, EmptyResponse
from move_bb8 import MoveBB8

def squareCallback(request):
    msg = MoveBB8("Hi client, its a server response!")
    response = msg.sendMessage()
    print response
    return EmptyResponse()
    
def main():
    server_node = rospy.init_node("move_square_node")
    
    square_service = rospy.Service("/move_bb8_square", Empty, squareCallback)
    
    rospy.spin()

if __name__=='__main__':
    try:
        main()
    except:
        rospy.loginfo("Server couldnt be initialized.")