import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('images.png')
cv2.namedWindow('image')
zoom2 = cv2.resize(img, None, fx=1, fy=1, interpolation=cv2.INTER_CUBIC)

cv2.createTrackbar('zoom', 'image',0,2,nothing)
#num = cv2.getTrackbarPos('zoom','image')
#cv2.imread('imag',img)
while(1):
	cv2.imshow('image',zoom2)

	k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

	#print(num)
	#zoom2 = cv2.resize(img, None, fx=num, fy=num, interpolation=cv2.INTER_CUBIC)
    
    


cv2.destroyAllWindows()