#!/usr/bin/env python
# license removed for brevity
import rospy
import serial
from std_msgs.msg import String
print("Starting serial")
s = serial.Serial()
s.port = "/dev/ttyACM0" #for arduino /dev/ttyACM0
s.baudrate = 9600

lat=54321.45
lon=987654.12
bearing=345
s.open()
st="opened"
print(st)
nmea=s.readline()
print(nmea)
while not rospy.is_shutdown():
       
	nmea=s.readline()
	print(nmea)
	rospy.loginfo(nmea)
	lat,lon,bearing=ar_data_split(nmea)
	rospy.loginfo(lat)
        rospy.loginfo(lon)
        rospy.loginfo(bearing)
        
        
