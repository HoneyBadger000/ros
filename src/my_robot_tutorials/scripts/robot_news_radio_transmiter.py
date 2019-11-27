#!/usr/bin/python

import rospy
from std_msgs.msg import String


def main():
        rospy.init_node('robot_news_radio_transmiter')

        pub = rospy.Publisher("/robot_news_radio", String, queue_size=10)

        # rate at 2Hertz, that is 2messages in 1sec
        rate = rospy.Rate(2)

        while not rospy.is_shutdown():
            msg = String()
            msg.data = "Hi , this is Dan from the Robot news radio !"
            pub.publish(msg)
            rate.sleep()

        rospy.loginfo("Node was stopped")


if __name__ == "__main__":
        main()

