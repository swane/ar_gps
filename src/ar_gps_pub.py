#!/usr/bin/env python
# license removed for brevity
import rospy
import serial
from std_msgs.msg import String
from ar_gps.msg import GPS_data
from ar_data_split import *

def talker():
    rospy.loginfo("talker started")
    s = serial.Serial()
    s.port = "/dev/ttyACM0" #for arduino /dev/ttyACM0
    s.baudrate = 9600
    pub = rospy.Publisher('argpschatter', GPS_data,queue_size=10)
    rospy.init_node('argpstalker', anonymous=True)
    rate = rospy.Rate(5) # 1hz
    msg = GPS_data()
    msg.UTM_lat=54321.45
    msg.UTM_lon=987654.12
    msg.bearing=345
    s.open()
    while not rospy.is_shutdown():
       
	nmea=s.readline()
	rospy.loginfo(nmea)
	msg.UTM_lat,msg.UTM_lon,msg.bearing=ar_data_split(nmea)
	rospy.loginfo(msg.UTM_lat)
        rospy.loginfo(msg.UTM_lon)
        rospy.loginfo(msg.bearing)
        
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



    
