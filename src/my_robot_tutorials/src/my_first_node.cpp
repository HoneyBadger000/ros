#include <ros/ros.h>

int main(int argc, char **argv)
{
    ros::init(argc, argv, "my_first_cpp_node");
    ros::NodeHandle nh;

    ROS_INFO("Node has been started");

    // Duration of 1sec
    // ros::Duration(1.0).sleep();

    ros::Rate rate(10);

    while(ros::ok()){
        ROS_INFO("Hello");
        rate.sleep();
    }

    ROS_INFO("Exit");

    return 0;
}