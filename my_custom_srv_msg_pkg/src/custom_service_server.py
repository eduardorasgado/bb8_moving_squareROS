#! /usr/bin/env python
import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse

def my_callback(request):
    print "Request Data => radius= "+str(request.radius)+", repetitions = "+str(request.repetitions)
    my_response = MyCustomServiceMessageResponse()
    if request.radius > 5.0:
        my_response.success = True
    else:
        my_response.success = False
    
    return my_response #the service response class
    
def main():
    rospy.init_node("service_client_node")
    
    #creating the service
    my_service = rospy.Service("/my_service", MyCustomServiceMessage, my_callback)
    
    #keep the service open
    rospy.spin()

if __name__=="__main__":
    main()