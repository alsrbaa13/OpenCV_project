import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('images.png',cv2.IMREAD_COLOR)
cv2.namedWindow('zoom image')

cv2.createTrackbar('zoom', 'zoom image',0,2,nothing)
cv2.setTrackbarPos('zoom','zoom image',1)

while(1):

	num = cv2.getTrackbarPos('zoom','image')
	cv2.imshow('zoom image',img)

	print(num)
	if cv2.waitKey(1) & 0xFF == ord('q'):  
		break;

cv2.destroyAllWindows()