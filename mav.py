from pymavlink import mavutil
from pymavlink.dialects.v20 import common as mavlink2

#from mavsdk import System

#com9
connectionString = '/dev/ttyUSB0'
connectionStringCOM = 'com9'
baudRate = 57600
baudMultipleRate = 1

the_connection = mavutil.mavlink_connection(connectionStringCOM, baud=baudRate)
the_connection.wait_heartbeat()
mav_serialport = mavutil.MavlinkSerialPort(
        "com9", 57600)
# Once connected, use 'the_connection' to get and send messages