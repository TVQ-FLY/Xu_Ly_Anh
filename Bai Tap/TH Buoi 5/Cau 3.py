import cv2
import numpy as np

image = cv2.imread('D:\Tran Quyen\Document\Image\kp.png')

if image is None:
    print('Error: Could not load image!')
    exit()
img = cv2.resize(image, (400, 500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
grad = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, np.ones((5,5),np.uint8))
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, np.ones((3,3),np.uint8))
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, np.ones((5,5),np.uint8))
sure_bg = cv2.dilate(opening,np.ones((3,3),np.uint8),iterations=2)
dist_transform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers+1
markers[unknown==255] = 0

markers = cv2.watershed(img,markers)
img[markers == -1] = [255,0,0]

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()