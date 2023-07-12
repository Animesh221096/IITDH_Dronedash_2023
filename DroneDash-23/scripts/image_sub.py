#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
import cv2
import numpy as np
from ros_numpy import numpify

class ImageSubscriber:
	def __init__(self):
		self.image_sub = rospy.Subscriber('/camera/depth/image_raw', Image, self.callback)

	def callback(self, msg):
		try:
			# Convert the image message to a NumPy array
			img_np = np.frombuffer(msg.data, dtype=np.float32).reshape(msg.height, msg.width, 1)
			return img_np
		except Exception as e:
			rospy.logerr(e)
			return

		# Display the image using OpenCV
		# cv2.imshow('Image', cv2.normalize(img_np, None, 1, 0, cv2.NORM_MINMAX, dtype=cv2.CV_32FC1))
		# cv2.waitKey(1)



if __name__ == '__main__':
	rospy.init_node('image_subscriber', anonymous=True)
	image_subscriber = ImageSubscriber()

	rospy.loginfo(image_subscriber.callback(Image))

	rospy.spin()
