# bb8_moving_squareROS
Moving a BB8 robot in a square path using server-client ROS comunication.\
\
For executing the simulation:\
	roslaunch bb8_square_movement bb8_move_in_square_service_server.launch\
	roslaunch bb8_square_movement bb8_move_in_square_service_client.launch\

Second simulation: Dynamic square movement.\
NOTE: For this sumulation move the my_custom_srv_msg_pkg a folder above this and compile
in order to get the service message package for this simulation ready.\
For executing the second simulation:\
	roslaunch bb8_square_movement start_bb8_move_custom_service_server.launch\
	roslaunch bb8_square_movement call_bb8_move_in_square_custom_service_server.launch\
