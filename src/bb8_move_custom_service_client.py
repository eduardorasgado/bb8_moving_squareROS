#! /usr/bin/env python
#client gonna call the server
import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest


def main():
    rospy.init_node("call_move_square_custom_node")
    #waiting
    rospy.wait_for_service("/move_bb8_in_square_custom")

    try:
        rospy.loginfo("Executing client...")
        
        #open the service client
        moving_robot = rospy.ServiceProxy('/move_bb8_in_square_custom', MyCustomServiceMessage)
        
        #pack the request actions in the object
        actions = MyCustomServiceMessageRequest()
        actions.radius = 2.0
        actions.repetitions = 2
        
        #send the actions to the server
        result = moving_robot(actions)
        
        if result:
            rospy.loginfo("The mission is completed!")
            
        #pack the request actions in the object
        actions2 = MyCustomServiceMessageRequest()
        actions2.radius = 3.0
        actions2.repetitions = 1
        
        #send the actions to the server
        result2 = moving_robot(actions2)
        
        if result2:
            rospy.loginfo("The mission is completed!")
        
    except:
        rospy.loginfo("An error occured in client")
        
if __name__=="__main__":
    try:
        main()
    except:
        rospy.loginfo("Client couldnt be initialized.")
