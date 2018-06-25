#! /usr/bin/env python
#server to be called for move in square
import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from move_bb8 import MoveBB8

def squareCallback(request):
    rospy.loginfo("Lets initialize the robot move...")
    ##initializing our response object
    response = MyCustomServiceMessageResponse()
    
    #create the robot movement object
    square = MoveBB8()
    errors=0
    for i in range(request.repetitions):
        #movin with a side size
        try:
            square.movesinSquare(request.radius)
        except Exception as e:
            errors+=1
    if errors == 0:
        response.success = True
    else:
        response.success = False
    
    return response
    
def main():
    server_node = rospy.init_node("move_square_custom_node")
    
    square_service = rospy.Service("/move_bb8_in_square_custom", MyCustomServiceMessage, squareCallback)
    
    rospy.spin()

if __name__=='__main__':
    try:
        main()
    except:
        rospy.loginfo("Server couldnt be initialized.")