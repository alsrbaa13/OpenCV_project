import cv2
import numpy as np

img = cv2.imread('picture.jpg')

a = img.size
print(a)
cv2.imshow('picture.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()