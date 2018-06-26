# -*- coding: utf-8 -*-

import cv2 as cv
import os

video = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(* 'XVID')
out = cv.VideoWriter('ball.avi', fourcc, 20.0,(1280,720))

while(video.isOpened()):
	ret, frame = video.read()
	frame1 = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
	ret, frame2 = cv.threshold(frame1, 115, 255, cv.THRESH_BINARY_INV)
	frame3 = cv.Canny(frame2, 70, 200, 3)
	cv.imshow('frame', frame3)
	if cv.waitKey(1) & 0xff == ord('q'):
		break
video.release()
cv.destroyAllWindows()