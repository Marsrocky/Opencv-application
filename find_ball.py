# coding=utf-8
# To find a ping-pong ball with high efficiency
# For strawberry Pi

import cv2
import numpy as np

def nothing(x):
	pass

cap = cv2.VideoCapture(0)

cv2.namedWindow('Result')
cv2.createTrackbar('min', 'Result', 50, 50, nothing)
cv2.createTrackbar('max', 'Result', 100, 200, nothing)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	min_radius = cv2.getTrackbarPos('min', 'Result')
	max_radius = cv2.getTrackbarPos('max', 'Result')
	all_circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=30, minRadius=min_radius, maxRadius=max_radius)

	if all_circles != None:
		# 转为二重数组
		circles = all_circles[0,:,:]
		# 取整
		circles = np.uint16(np.around(circles))
		for i in circles[:]:
			print 'Radius: ', i[2]
			print 'O: (', i[0], ', ', i[1], ')'
			print frame[i[1], i[0]]

			b, g, r = frame[i[1], i[0]]
			# R 230+  G 110 200  B 50 110
			if r >= 200 and b <= 110 and g >= 110:
				cv2.circle(frame,(i[0],i[1]),i[2],(255,0,0),5)#画圆
				cv2.circle(frame,(i[0],i[1]),2,(255,0,255),10)#画圆心

	cv2.imshow('Result', frame)
	cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()