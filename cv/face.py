import cv2
from picamera import PiCamera
from time import sleep

camera = PiCamera()

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

cap = camera.start_preview()
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('test.avi',fourcc, 20.0, (640,480))

sleep(10)

while True:
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, 1.3,5)
	for(x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
	
	out.write(frame)
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		camera.stop_preview()
		break
cap.release()
out.release()
cv2.destroyAllWindows()