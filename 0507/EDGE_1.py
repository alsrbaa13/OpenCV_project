# -*- coding: utf-8 -*-

import cv2 as cv
import os
import numpy as np

video = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(* 'XVID')
out = cv.VideoWriter('ball.avi', fourcc, 20.0,(1280,720))

while(video.isOpened()):
	ret, frame = video.read()
	frame1 = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
	ret, frame2 = cv.threshold(frame1, 80, 200, cv.THRESH_BINARY_INV)
	frame3 = cv.Canny(frame2, 0, 130, 3)
	frame4 = cv.HoughCircles(frame3, cv.HOUGH_GRADIENT, 1, 20,param1=50,param2=25,minRadius=0, maxRadius=0)
	cv.imshow('frame', frame4)
	if cv.waitKey(1) & 0xff == ord('q'):
		break
video.release()
cv.destroyAllWindows()