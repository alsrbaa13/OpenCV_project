import cv2 as cv
import os
import numpy as np

video = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(* 'XVID')
out = cv.VideoWriter('ball.avi', fourcc, 20.0,(1280,720))

while(video.isOpened()):
	ret, frame = video.read()
	frame = cv.medianBlur(frame,3)
	frame1 = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
	ret, frame2 = cv.threshold(frame1, 80, 200, cv.THRESH_BINARY_INV)
	frame3 = cv.Canny(frame2, 0, 130, 3)
	# frame4 = cv.HoughCircles(frame3, cv.HOUGH_GRADIENT, 1, 20,param1=50,param2=30,minRadius=5, maxRadius=0)
	#frame4 = np.uint16(np.around(frame4))

	#for i in frame4[0,:]:
    #		cv.circle(frame3,(i[0],i[1]),i[2],(255,255,255),2)
	cv.imshow('frame', frame3)
	if cv.waitKey(1) & 0xff == ord('q'):
		break
video.release()
cv.destroyAllWindows()