from __future__ import print_function

import numpy as np
import cv2
import sys
import math

cap = cv2.VideoCapture(0)

def extends(x1, y1, x2, y2, n):
	i = (y2-y1)/(x2-x1)
	#a = n
	b = i*n + y2
	return n, b

while(cap.isOpened()):
	
	s, img = cap.read()
	
	winName = "Movement Indicator"
	
	cv2.namedWindow(winName, cv2.WINDOW_AUTOSIZE)
	
	edges = cv2.Canny(img, 100, 300)
	cdst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

	if True: 
		
		lines = cv2.HoughLinesP(edges, 1, math.pi/180.0, 40, np.array([]), 80, 50)
		
		a,b,c = lines.shape		
		
		for i in range(a):
			x = 0
			j = 0
			while x==0 :
				if abs(lines[i][j][0] - lines[i][j][2])< 50:
					j+=1
				else :
					cv2.line(cdst, (lines[i][j][0], lines[i][j][1]), (lines[i][j][2], lines[i][j][3]), (0, 0, 255), 3, cv2.CV_AA)
					cv2.line(cdst, (lines[i][j+1][0], lines[i][j+1][1]), (lines[i][j+1][2], lines[i][j+1][3]), (0, 0, 255), 3, cv2.CV_AA)

					a1,b1 = extends(lines[i][j][0], lines[i][j][1], lines[i][j][2], lines[i][j][3],200)
					a2,b2 = extends(lines[i][j+1][0], lines[i][j+1][1], lines[i][j+1][2], lines[i][j+1][3],200)

					if lines[i][j][0] < lines[i][j][2] :
						cv2.line(cdst, (lines[i][j][0], lines[i][j][1]), (lines[i][j][2] + a1, b1), (0, 255, 0), 3, cv2.CV_AA)
					else:
						cv2.line(cdst, (lines[i][j][0]-a1, b1), (lines[i][j][2], lines[i][j][3]), (0, 255, 0), 3, cv2.CV_AA)

					if lines[i][j][0] > lines[i][j+1][2] :	
						cv2.line(cdst, (lines[i][j+1][0], lines[i][j+1][1]), (lines[i][j+1][2] + a2, b2), (0, 255, 0), 3, cv2.CV_AA)
					else:
						cv2.line(cdst, (lines[i][j+1][0]-a1, b1), (lines[i][j+1][2], lines[i][j+1][3]), (0, 255, 0), 3, cv2.CV_AA)
					x=1




			
    

	cv2.imshow('detected lines', cdst)

	if cv2.waitKey(50) & 0xff == ord('q'):
		break

cam.release()
cv2.destroyAllWindows()