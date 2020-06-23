#!/usr/bin/env python

#Node subscribe to /sim/camera/compressed


import rospy
from sensor_msgs.msg import CompressedImage
import cv2
import numpy as np
from cv_bridge import CvBridge
brg = CvBridge()
coun = 0
def callback(data):
    global coun
    im22 = brg.compressed_imgmsg_to_cv2(data)
    cv2.imwrite("data_set/img"+str(coun)+".png", im22)
    coun +=1


def suby():
    rospy.init_node('sub_cam', anonymous=True)

    rospy.Subscriber("sim/camera/compressed", CompressedImage, callback)
    #wait three seconds between the image and the other image
    rospy.sleep(3)
    rospy.spin()

if __name__ == '__main__':
    suby()