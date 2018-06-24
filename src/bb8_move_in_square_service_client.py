#! /usr/bin/env python
#client gonna call the server
import rospy
from std_srvs.srv import Empty, EmptyRequest

"""
Client example:
#! /usr/bin/env python

import rospy
from gazebo_msgs.srv import DeleteModel, DeleteModelRequest # Import the service message used by the service /gazebo/delete_model
import sys 

rospy.init_node('service_client') # Initialise a ROS node with the name service_client
rospy.wait_for_service('/gazebo/delete_model') # Wait for the service client /gazebo/delete_model to be running
delete_model_service = rospy.ServiceProxy('/gazebo/delete_model', DeleteModel) # Create the connection to the service
kk = DeleteModelRequest() # Create an object of type DeleteModelRequest
kk.model_name = "bowl_1" # Fill the variable model_name of this object with the desired value
result = delete_model_service(kk) # Send through the connection the name of the object to be deleted by the service
print result # Print the result given by the service
"""

def main():
    rospy.init_node("bb8_activate_client")
    #waiting
    rospy.wait_for_service("/move_bb8_square")
    
    try:
        rospy.loginfo("Executing client...")
        
        #open the service client
        moving_robot = rospy.ServiceProxy('/move_bb8_square', Empty)
        
        #finally execute the request
        requestObject = EmptyRequest()
        moving_robot(requestObject)
        
    except:
        rospy.loginfo("An error occured in client")
        
if __name__=="__main__":
    try:
        main()
    except:
        rospy.loginfo("Client couldnt be initialized.")
