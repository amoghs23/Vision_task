#!/usr/bin/env python

import rospy
from ackermann_msgs.msg import AckermannDriveStamped

def callback(msg):
    # Extract speed and steering angle from the incoming message
    speed = msg.drive.speed
    steering_angle = msg.drive.steering_angle

    # Multiply both speed and steering angle by 3
    speed *= 3
    steering_angle *= 3

    # Create a new AckermannDriveStamped message with the modified values
    new_msg = AckermannDriveStamped()
    new_msg.drive.speed = speed
    new_msg.drive.steering_angle = steering_angle

    # Publish the new message to the drive_relay topic
    pub.publish(new_msg)

if __name__ == '__main__':
    rospy.init_node('relay', anonymous=True)
    
    # Subscribe to the drive topic
    rospy.Subscriber('drive', AckermannDriveStamped, callback)
    
    # Create a publisher for the drive_relay topic
    pub = rospy.Publisher('drive_relay', AckermannDriveStamped, queue_size=10)
    
    rospy.spin()



