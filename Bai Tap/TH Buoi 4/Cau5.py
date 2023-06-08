import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.namedWindow('image')
cv2.namedWindow('edges')

cv2.createTrackbar('lower', 'image', 0, 255, nothing)
cv2.createTrackbar('upper', 'image', 0, 255, nothing)

while True:
    lower = cv2.getTrackbarPos('lower', 'image')
    upper = cv2.getTrackbarPos('upper', 'image')
    
    edges = cv2.Canny(gray, lower, upper*3)
    
    cv2.imshow('image', img)
    cv2.imshow('edges', edges)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
