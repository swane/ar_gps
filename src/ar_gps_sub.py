#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from ar_gps.msg import GPS_data

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %d", GPS_data.num)
    rospy.loginfo(data.UTM_lat)
    rospy.loginfo(data.UTM_lon)
    rospy.loginfo(data.bearing)
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("argpschatter", GPS_data, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
