cmake_minimum_required(VERSION 2.8.3)
project(my_custom_srv_msg_pkg)


find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  message_generation
  message_runtime
)


## Generate messages in the 'msg' folder
# add_message_files(
#   FILES
#   Message1.msg
#   Message2.msg
# )

## Generate services in the 'srv' folder
 add_service_files(
   FILES
   MyCustomServiceMessage.srv
 )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs  # Or other packages containing msgs
 )

## State here all the packages that will be needed by someone that executes something from your package.
## All the packages stated here must be in the package.xml as run_depend
catkin_package(
  CATKIN_DEPENDS rospy
)

####
# include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)