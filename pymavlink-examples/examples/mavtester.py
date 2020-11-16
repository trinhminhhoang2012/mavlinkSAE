#!/usr/bin/env python

'''
test mavlink messages
'''
from __future__ import print_function

from pymavlink import mavutil

from argparse import ArgumentParser

def wait_heartbeat(m):
    '''wait for a heartbeat so we know the target system IDs'''
    print("Waiting for APM heartbeat")
    msg = m.recv_match(type='HEARTBEAT', blocking=True)
    print("Heartbeat from APM (system %u component %u)" % (m.target_system, m.target_system))

# create a mavlink serial instance
master = mavutil.mavlink_connection("com9", baud=56200, source_system=255)

# wait for the heartbeat msg to find the system ID
wait_heartbeat(master)

print("Sending all message types")

